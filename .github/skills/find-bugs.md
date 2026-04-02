---
name: Find bugs in a Python interpreter
description: End-to-end fuzzing campaign — generates tests, runs them, triages findings, and creates minimal reproducers
---

# Find Bugs in a Python Interpreter

You are an expert fuzzer. Your job is to find bugs in a Python interpreter by running an end-to-end campaign: generate tests, execute them, analyze results, minimize reproducers, and save findings. Do all of this autonomously.

## Step 0: Determine the target

Ask the user which Python interpreter to fuzz. Default is `python` on PATH. Then detect its version:

```bash
python --version
python -c "import sys; print(sys.version_info); print(sys.executable); print(sys.platform)"
```

Note the major.minor.micro — this determines which features and scripts apply.

## Step 1: Run the existing fuzzer scripts

Run all four fuzzers from `scripts/` against the target. Run them in parallel where possible. Each targets different bug classes:

```bash
# Main fuzzer — ~900 generated test cases run in subprocesses (crashes, fatal errors)
python scripts/run.py --python <target> --timeout 15 --output scripts/results

# Deep fuzzer — in-process tests for compile, AST, GC, descriptors, frame manipulation
python scripts/deep_fuzzer.py

# Semantic fuzzer — correctness: AST round-trip, error attributes, optimizer, monitoring API
python scripts/semantic_fuzzer.py

# Aggressive fuzzer — crash vectors: stack overflow, threading, monitoring callbacks, eval
python scripts/aggressive_fuzzer.py
```

Collect all output. Look for:
- `FINDING` / `CRASH` / `FATAL ERROR` / `SystemError` in stdout
- Abnormal exit codes (nonzero, especially negative or 0xC0000005-range on Windows)
- `"object address"` / `"lost sys.stderr"` in stderr (internal error dumps)
- Timeouts (possible hangs)
- `"Traceback"` where the error type is `SystemError`

## Step 2: Write new targeted tests

Based on the interpreter version, write **new** targeted test programs that go beyond what the scripts cover. Focus on:

### High-yield areas by version

**Python 3.13:** `sys.monitoring` (PEP 669) callback edge cases, FrameLocalsProxy (PEP 667), `__static_attributes__`/`__firstlineno__`, incremental GC, experimental JIT (if enabled)

**Python 3.12:** Type parameter syntax (PEP 695), f-string parser rewrite (nesting, backslashes), comprehension inlining, `sys.monitoring` initial impl, per-interpreter GIL (PEP 684)

**Python 3.11:** Exception groups (PEP 654) / `except*`, specializing interpreter (PEP 659), fine-grained error locations

**Python 3.10:** Pattern matching (PEP 634), parenthesized context managers

### General high-yield patterns (any version)
- **Re-entrancy:** callbacks/dunder methods that trigger the same mechanism (e.g., `__del__` during GC, monitoring callbacks that re-trigger events)
- **Feature interactions:** combine 2–3 features (e.g., generators + exception groups + tracing)
- **Error-path testing:** unusual inputs to `compile()`, `marshal.loads()`, `ast.parse()`
- **Protocol edge cases:** `__hash__` returning -1, `__len__` returning negative, `__bool__` raising

### How to run test code

For crash detection (subprocess — catches segfaults):
```python
import subprocess, sys, tempfile, os
code = "..."
with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    f.write(code); path = f.name
try:
    r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=15)
    unsigned = r.returncode & 0xFFFFFFFF if r.returncode < 0 else r.returncode
    if unsigned in (0xC0000005, 0xC0000409, 0xC000001D, 0xC00000FD, 0xC0000374):
        print(f"CRASH: {hex(unsigned)}")
    elif "fatal python error" in r.stderr.lower():
        print(f"FATAL: {r.stderr[:200]}")
    elif "systemerror" in r.stderr.lower():
        print(f"SystemError: {r.stderr[:200]}")
    elif "object address" in r.stderr.lower():
        print(f"Internal dump: {r.stderr[:200]}")
except subprocess.TimeoutExpired:
    print("HANG: timed out")
finally:
    os.unlink(path)
```

For fast in-process testing (compile/ast only):
```python
try:
    compile(source, "<test>", "exec")
except SyntaxError:
    pass
except SystemError as e:
    print(f"BUG: {e}")
```

## Step 3: Triage findings

For each finding from Steps 1–2:

1. **Classify** by type: crash, fatal error, internal error dump, SystemError, hang, exception bypass, incorrect result
2. **Deduplicate** — group findings with the same root cause (same error message, same code path, same API)
3. **Discard false positives** — `RecursionError`, `MemoryError`, `SyntaxError`, normal Python exceptions from user code, slow-but-not-hung tests

## Step 4: Minimize and save

For each unique bug:

1. **Minimize** the reproducer: remove unrelated code, simplify expressions, use literals, binary-search to find the minimal trigger. After each reduction, verify the bug still reproduces.

2. **Create a findings directory:**
```
findings/<interpreter>-<version>-<short-slug>/
  README.md
  reproducer.py
  reproducer_variant.py   # optional additional variants
```

3. **reproducer.py** must be self-contained (no imports from the repo) and include a docstring:
```python
"""
<Bug title>

<Description>

Interpreter: <name and version>
Expected: <what should happen>
Actual: <what actually happens>
"""
# minimal code
```

4. **README.md** should follow this template:
```markdown
# <Bug title>

**Interpreter:** <name and version>
**Status:** New

## Description
<What happens and why it's a bug>

## Expected Behavior
<What should happen>

## Actual Behavior
<What actually happens, with error output>

## Reproducer
\`\`\`bash
python reproducer.py
\`\`\`

## Versions Tested
- <version>: **affected**
```

5. **Update `findings/README.md`** — add the new bug to the table.

6. **Update `README.md`** — add the new bug to the Bug Hall of Fame table.

## Step 5: Commit and push

Stage all new/changed files and commit:

```bash
git add -A
git commit -m "<short description of bugs found>

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push
```

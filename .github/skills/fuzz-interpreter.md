---
name: Fuzz a Python interpreter
description: Run a fuzzing campaign against a Python interpreter to find crashes, internal errors, and semantic bugs
---

# Fuzz a Python Interpreter

You are a fuzzing expert. Your job is to find bugs in a Python interpreter by generating and executing diverse test programs.

## Inputs

Ask the user for:
1. **Target interpreter** — the command to invoke the interpreter (default: `python`)
2. **Focus areas** — which areas to prioritize (or "all" for a broad campaign). Options include:
   - `parser` — PEG parser edge cases, deeply nested syntax, unusual source encodings
   - `compiler` — compile(), ast.parse(), optimization levels, bytecode generation
   - `runtime` — object protocols, GC, closures, generators, async, descriptors, metaclasses
   - `monitoring` — sys.monitoring (PEP 669), sys.settrace, sys.setprofile
   - `typing` — type parameters (PEP 695), generics, type aliases
   - `exceptions` — exception groups (PEP 654), except*, chaining, traceback
   - `stdlib` — standard library modules (collections, struct, re, pickle, marshal, etc.)
   - `threading` — concurrent access, GIL edge cases
   - `all` — run everything

## Workflow

### Step 1: Determine the interpreter version

```bash
<target> --version
<target> -c "import sys; print(sys.version_info); print(sys.executable)"
```

Note the major/minor/micro version — this determines which language features are available.

### Step 2: Run the existing fuzzer scripts

The repo has several fuzzer scripts in `scripts/`. Run them against the target interpreter:

```bash
# Main fuzzer — generates ~900 test cases and runs them in subprocesses
<target> scripts/run.py --python <target> --timeout 15 --output findings/results

# Deep fuzzer — in-process targeted tests (compile, AST, GC, descriptors, etc.)
<target> scripts/deep_fuzzer.py

# Semantic fuzzer — correctness tests (AST round-trip, error attrs, optimizer, etc.)
<target> scripts/semantic_fuzzer.py

# Aggressive fuzzer — crash-focused tests (stack overflow, threading, monitoring, etc.)
<target> scripts/aggressive_fuzzer.py
```

Review the output for any findings (crashes, internal errors, SystemError, hangs).

### Step 3: Write targeted fuzz tests

Based on the interpreter version and focus areas, write **new** targeted test programs. The most productive areas for finding bugs are:

- **New or recently-changed features** — these have had less testing
- **Interaction between features** — e.g., monitoring + generators + exception groups
- **Error/edge-case handling** — unusual inputs, boundary values, error recovery
- **Re-entrancy** — callbacks that trigger the same callback mechanism

When writing tests, use this pattern for subprocess execution:

```python
import subprocess, sys, tempfile, os

code = '''
# ... test code here ...
'''

with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    f.write(code)
    path = f.name

try:
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=15)
    exit_code = result.returncode
    # Check for crashes: on Windows, 0xC0000005 = access violation
    unsigned = exit_code & 0xFFFFFFFF if exit_code < 0 else exit_code
    if unsigned in (0xC0000005, 0xC0000409, 0xC000001D, 0xC00000FD, 0xC0000374):
        print(f"CRASH: exit code {hex(unsigned)}")
    elif "fatal python error" in result.stderr.lower():
        print(f"FATAL ERROR in stderr")
    elif "systemerror" in result.stderr.lower():
        print(f"SystemError in stderr")
    elif exit_code != 0:
        pass  # Normal Python exception — not a bug
except subprocess.TimeoutExpired:
    print("TIMEOUT — possible hang")
finally:
    os.unlink(path)
```

For in-process tests (compile/ast only — safe, fast):

```python
try:
    compile(source, "<test>", "exec")
except SyntaxError:
    pass  # expected
except SystemError as e:
    print(f"BUG: SystemError during compile: {e}")
```

### Step 4: Investigate findings

For each finding:
1. **Minimize** — reduce to the smallest reproducer
2. **Classify** — crash / fatal error / SystemError / incorrect behavior / hang / exception bypass
3. **Verify** — run the reproducer multiple times to confirm it's deterministic
4. **Check scope** — does it affect other Python versions?

### Step 5: Save findings

For each confirmed bug, create a subdirectory under `findings/`:

```
findings/<interpreter>-<version>-<short-slug>/
  README.md        — Description, expected vs actual, versions tested
  reproducer.py    — Minimal self-contained reproducer
```

The `README.md` should follow this template:

```markdown
# <Bug title>

**Interpreter:** CPython 3.13.12
**Status:** Open

## Description
<What happens and why it's a bug>

## Expected Behavior
<What should happen>

## Actual Behavior
<What actually happens, including any error output>

## Reproducer
Run `reproducer.py` with the affected interpreter:
\`\`\`bash
python reproducer.py
\`\`\`

## Versions Tested
- CPython 3.13.12: **affected**
- CPython 3.12.x: <unknown / not affected>
```

## Key Areas for Each Python Version

### Python 3.13
- `sys.monitoring` (PEP 669) — callback exception handling
- Incremental GC
- `__static_attributes__`, `__firstlineno__`
- PEP 667 (`locals()` semantics via FrameLocalsProxy)
- Experimental JIT (if enabled)

### Python 3.12
- Type parameter syntax (PEP 695) — `class C[T]`, `type Alias = ...`
- f-string parser rewrite — unlimited nesting, backslashes
- Comprehension inlining
- `sys.monitoring` (PEP 669) — initial implementation
- Per-interpreter GIL (PEP 684)

### Python 3.11
- Exception groups (PEP 654) — `except*`, `ExceptionGroup`
- Specializing interpreter (PEP 659)
- Fine-grained error locations in tracebacks

### Python 3.10
- Pattern matching (PEP 634) — `match`/`case`
- Parenthesized context managers

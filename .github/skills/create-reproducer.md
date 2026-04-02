---
name: Create a minimal reproducer
description: Reduce a fuzzer finding to a minimal, self-contained reproducer script
---

# Create a Minimal Bug Reproducer

You are a bug minimization expert. Your job is to take a fuzzer finding and produce the smallest possible self-contained script that demonstrates the bug.

## Inputs

Ask the user for:
1. **The finding** — the code, error output, or description of the bug
2. **Target interpreter** — the command to invoke the affected interpreter (default: `python`)

## Workflow

### Step 1: Understand the bug

Analyze the finding to understand:
- What type of bug it is (crash, fatal error, SystemError, wrong result, hang, exception bypass)
- What code triggers it
- What the expected vs. actual behavior is

### Step 2: Minimize

Apply these reduction strategies in order:

1. **Remove unrelated code** — delete imports, functions, classes that aren't needed
2. **Simplify expressions** — replace complex expressions with simpler ones that still trigger the bug
3. **Remove loops** — if a loop isn't needed, remove it or reduce iterations
4. **Inline functions** — replace function calls with their bodies if it helps
5. **Remove error handling** — if try/except isn't part of the bug, remove it
6. **Use literals** — replace variables with literal values
7. **Binary search** — if the input is large, try removing halves to find the minimal trigger

After each reduction, **verify** the bug still reproduces.

### Step 3: Verify

Run the reproducer multiple times to confirm:
```bash
# Run 3 times to check determinism
python reproducer.py
python reproducer.py
python reproducer.py
```

For hangs, use a timeout:
```bash
# On Windows (PowerShell)
$proc = Start-Process python -ArgumentList reproducer.py -NoNewWindow -PassThru
if (-not $proc.WaitForExit(5000)) { Stop-Process -Id $proc.Id -Force; echo "HUNG" }

# On Linux
timeout 5 python reproducer.py
```

### Step 4: Document

Create the reproducer file with this structure:

```python
"""
<Bug title>

<One paragraph description of the bug>

Interpreter: <name and version>
Expected: <what should happen>
Actual: <what actually happens>

WARNING: <if the script hangs or crashes, note it here>
"""

# <minimal code that triggers the bug>
```

### Step 5: Save

Save the reproducer and create a README in the findings directory:

```
findings/<interpreter>-<version>-<short-slug>/
  README.md
  reproducer.py
  reproducer_variant.py   # (optional) additional variants
```

The README.md should include:
- Bug title and description
- Severity classification
- Expected vs. actual behavior
- How to run the reproducer
- Python versions tested
- Any known workarounds

## Quality Checklist

A good reproducer should:
- [ ] Be **self-contained** — no imports from the repo, no external dependencies
- [ ] Be **minimal** — removing any line breaks the reproduction
- [ ] Be **deterministic** — reproduces every time (or document the flakiness)
- [ ] Have a **clear docstring** explaining the bug
- [ ] Exit with **non-zero status** when the bug is present (if possible)
- [ ] Work on a **fresh Python install** — no special setup needed

# `sys.monitoring` JUMP/BRANCH exceptions bypass `try/except`

**Interpreter:** CPython 3.13.12
**Severity:** MEDIUM
**Status:** New

## Description

When a `sys.monitoring` callback for `JUMP` or `BRANCH` events raises an exception, the exception is raised but **bypasses enclosing `try/except` handlers**. The exception propagates directly to the top level as an unhandled exception, even when there is a matching `except` clause.

## Expected Behavior

The `ValueError` raised by the JUMP/BRANCH callback should be caught by the enclosing `try/except ValueError` handler.

## Actual Behavior

The exception bypasses the handler and crashes the program:

```
Traceback (most recent call last):
  File "reproducer_jump.py", line 33, in <module>
    pass
  File "reproducer_jump.py", line 25, in <lambda>
    lambda *args: (_ for _ in ()).throw(ValueError("jump_boom")),
ValueError: jump_boom
```

Note that line 33 (`pass`) is inside a `try` block with `except ValueError`, but the exception is not caught.

## Reproducer

```bash
python reproducer_jump.py     # JUMP variant (for loops)
python reproducer_branch.py   # BRANCH variant (if/else)
```

## Root Cause

The instrumented bytecode for JUMP and BRANCH events does not properly consult the exception handler table when propagating exceptions from monitoring callbacks. The exception is raised at the bytecode level in a way that skips the normal exception-handler lookup.

## Versions Tested

- CPython 3.13.12: **affected**

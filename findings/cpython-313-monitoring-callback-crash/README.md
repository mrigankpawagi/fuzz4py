# `sys.monitoring` LINE/CALL/INSTRUCTION callback exceptions bypass `try/except`

**Interpreter:** CPython 3.13.12
**Status:** New

## Description

When a `sys.monitoring` callback for `LINE`, `CALL`, or `INSTRUCTION` events raises an exception, the exception **bypasses enclosing `try/except` handlers** instead of being caught normally.

This is the same class of bug as the JUMP/BRANCH bypass (see `cpython-313-monitoring-exception-bypass/`), but affects different event types. On some machines, this may additionally produce an internal `_PyObject_Dump` and `"lost sys.stderr"` instead of a normal traceback.

This affects any tool using `sys.monitoring` (PEP 669) — debuggers, profilers, coverage tools — if a callback raises an exception (intentionally or due to a bug in the tool).

## Expected Behavior

The exception from the callback should be caught by the `try/except ValueError` handler, just as it is for `PY_START` events (which work correctly — see the control test in `reproducer.py`).

## Actual Behavior

The `ValueError` bypasses the `try/except` and propagates as an unhandled exception:

```
Traceback (most recent call last):
  File "reproducer.py", line 46, in <module>
  File "reproducer.py", line 37, in line_cb
ValueError: from LINE
```

On some machines, this instead produces an internal error dump:

```
object address  : 0x...
object refcount : 3
object type     : 0x...
object type name: ValueError
object repr     : ValueError('boom')
lost sys.stderr
```

## Reproducer

Run `reproducer.py` which includes a control test (PY_START, works correctly) followed by the buggy test (LINE, exception bypasses handler):

```bash
python reproducer.py
```

The CALL variant (`reproducer_call.py`) demonstrates the same bug with CALL events.

## Root Cause

Events that are "local" to the bytecode interpreter loop (LINE, CALL, INSTRUCTION, JUMP, BRANCH) do not properly consult the exception handler table when propagating exceptions from monitoring callbacks.

Events that go through the function-call dispatch path (PY_START, PY_RETURN, PY_RESUME, PY_UNWIND, RAISE) handle callback exceptions correctly.

## Versions Tested

- CPython 3.13.12: **affected**

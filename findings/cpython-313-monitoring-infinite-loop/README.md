# `sys.monitoring` EXCEPTION_HANDLED infinite loop

**Interpreter:** CPython 3.13.12
**Severity:** HIGH
**Status:** New

## Description

When a `sys.monitoring` callback for the `EXCEPTION_HANDLED` event raises an exception, the new exception is itself "handled" by the `except` clause, which triggers another `EXCEPTION_HANDLED` event, which invokes the callback again, creating an **infinite loop** that hangs the interpreter.

## Expected Behavior

The exception from the callback should be propagated to the caller, or the callback should not be invoked re-entrantly for exceptions caused by the callback itself.

## Actual Behavior

The process hangs indefinitely and must be killed. The cycle is:

```
except clause handles exception
  → EXCEPTION_HANDLED event fires
    → callback raises new exception
      → except clause handles that exception
        → EXCEPTION_HANDLED event fires
          → callback raises again
            → ... (infinite loop)
```

## Reproducer

**WARNING: This script will hang indefinitely. Run with a timeout.**

```bash
# PowerShell
$p = Start-Process python -ArgumentList reproducer.py -NoNewWindow -PassThru
if (-not $p.WaitForExit(5000)) { Stop-Process -Id $p.Id -Force; echo "HUNG" }

# Linux/macOS
timeout 5 python reproducer.py
```

## Root Cause

There is no re-entrancy guard on `EXCEPTION_HANDLED` callbacks. When the callback raises, the resulting exception is caught by the same `except` clause, which fires `EXCEPTION_HANDLED` again, invoking the callback in an infinite cycle.

## Versions Tested

- CPython 3.13.12: **affected**

"""
Bug 1: sys.monitoring LINE/CALL/INSTRUCTION callback crash
==========================================================

When a sys.monitoring callback for LINE, CALL, or INSTRUCTION events raises
an exception, and the exception handling code triggers the same event type
again (causing the callback to raise again), CPython crashes with an internal
_PyObject_Dump output and "lost sys.stderr" instead of properly handling the
exception.

Affected events: LINE, CALL, INSTRUCTION
Not affected: PY_START, PY_RETURN, PY_RESUME, PY_UNWIND, RAISE

Python version: 3.13.12 (CPython)
Platform: Windows (likely also Linux/macOS)

Root cause: Re-entrant exception from monitoring callback during exception
handling is not properly handled by the interpreter.

Expected behavior: The exception should be propagated normally and be
catchable by try/except, OR the second callback invocation should be
suppressed during exception handling.

Actual behavior: CPython prints an internal object dump:
    object address  : 0x...
    object refcount : 3
    object type     : 0x...
    object type name: ValueError
    object repr     : ValueError('boom')
    lost sys.stderr
And exits with code 1.
"""

import sys

# ======== Minimal reproducer ========

sys.monitoring.use_tool_id(0, "repro")
sys.monitoring.register_callback(
    0,
    sys.monitoring.events.LINE,
    lambda code, line: (_ for _ in ()).throw(ValueError("boom")),
)
sys.monitoring.set_events(0, sys.monitoring.events.LINE)

try:
    x = 1  # LINE callback raises -> crash
except ValueError:
    print("This is never reached")

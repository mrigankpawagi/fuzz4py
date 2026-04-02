"""
Bug 3: sys.monitoring EXCEPTION_HANDLED callback causes infinite loop
=====================================================================

When an EXCEPTION_HANDLED monitoring callback raises an exception, the new
exception triggers another EXCEPTION_HANDLED event (since an exception is
being "handled"), which raises again, causing an infinite loop that hangs
the interpreter.

Python version: 3.13.12 (CPython)

Expected behavior: The exception from the callback should be propagated
to the caller, or the callback should not be invoked re-entrantly.

Actual behavior: Infinite loop - the process hangs and must be killed.

WARNING: This script will hang indefinitely. Run with a timeout:
    timeout 5 python bug3_monitoring_infinite_loop.py
"""

import sys

sys.monitoring.use_tool_id(0, "repro")

sys.monitoring.register_callback(
    0,
    sys.monitoring.events.EXCEPTION_HANDLED,
    lambda code, offset: (_ for _ in ()).throw(ZeroDivisionError("boom")),
)
sys.monitoring.set_events(0, sys.monitoring.events.EXCEPTION_HANDLED)

try:
    raise RuntimeError("trigger")
except RuntimeError:
    pass  # EXCEPTION_HANDLED fires -> callback raises -> EXCEPTION_HANDLED fires -> infinite loop

"""
sys.monitoring EXCEPTION_HANDLED callback causes infinite loop

When an EXCEPTION_HANDLED callback raises, the new exception is "handled"
by the except clause, which fires EXCEPTION_HANDLED again, looping forever.

Interpreter: CPython 3.13
Expected: The exception from the callback is propagated to the caller.
Actual: Infinite loop — the process hangs and must be killed.

WARNING: This script will hang indefinitely. Run with a timeout:
    timeout 5 python reproducer.py          (Linux/macOS)
    Start-Process python reproducer.py ...  (Windows, see README)
"""

import sys

TOOL_ID = 0

def callback(code, offset):
    raise ZeroDivisionError("boom")

sys.monitoring.use_tool_id(TOOL_ID, "repro")
sys.monitoring.register_callback(
    TOOL_ID, sys.monitoring.events.EXCEPTION_HANDLED, callback
)
sys.monitoring.set_events(TOOL_ID, sys.monitoring.events.EXCEPTION_HANDLED)

try:
    raise RuntimeError("trigger")
except RuntimeError:
    pass  # EXCEPTION_HANDLED fires → callback raises → repeat forever

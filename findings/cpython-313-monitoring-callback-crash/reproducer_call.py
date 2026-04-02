"""
sys.monitoring CALL callback exception bypasses try/except

Same root cause as the LINE variant: exceptions from CALL monitoring
callbacks bypass try/except handlers.

Interpreter: CPython 3.13
Expected: The ValueError is caught by the except clause.
Actual: The ValueError bypasses try/except (may also produce internal dump).
"""

import sys

print(f"Python {sys.version}")

def callback(code, offset, callable_obj, arg0):
    raise ValueError("boom")

sys.monitoring.use_tool_id(0, "repro")
sys.monitoring.register_callback(0, sys.monitoring.events.CALL, callback)
sys.monitoring.set_events(0, sys.monitoring.events.CALL)

try:
    len([1, 2, 3])  # triggers CALL callback → ValueError bypasses this handler
except ValueError:
    print("BUG NOT PRESENT: ValueError was caught by try/except")
    sys.monitoring.set_events(0, 0)
    sys.monitoring.free_tool_id(0)

print("Done")

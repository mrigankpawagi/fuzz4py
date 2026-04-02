"""
sys.monitoring BRANCH callback exception bypasses try/except

When a BRANCH monitoring callback raises an exception, the exception bypasses
enclosing try/except handlers and propagates as unhandled.

Interpreter: CPython 3.13
Expected: The ValueError is caught by the except clause.
Actual: The ValueError propagates as an unhandled exception.
"""

import sys

TOOL_ID = 0

def callback(code, instruction_offset, target_offset):
    raise ValueError("branch_boom")

sys.monitoring.use_tool_id(TOOL_ID, "repro")
sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.BRANCH, callback)
sys.monitoring.set_events(TOOL_ID, sys.monitoring.events.BRANCH)

x = True  # variable so the branch isn't constant-folded

try:
    if x:  # BRANCH event fires here
        result = 1
    else:
        result = 2
except ValueError as e:
    print(f"Caught: {e}")  # This is never reached
finally:
    sys.monitoring.set_events(TOOL_ID, 0)
    sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.BRANCH, None)
    sys.monitoring.free_tool_id(TOOL_ID)

print("Test complete")

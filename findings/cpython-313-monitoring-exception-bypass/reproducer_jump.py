"""
sys.monitoring JUMP callback exception bypasses try/except

When a JUMP monitoring callback raises an exception, the exception bypasses
enclosing try/except handlers and propagates as unhandled.

Interpreter: CPython 3.13
Expected: The ValueError is caught by the except clause.
Actual: The ValueError propagates as an unhandled exception, bypassing try/except.
"""

import sys

TOOL_ID = 0

def callback(code, instruction_offset, target_offset):
    raise ValueError("jump_boom")

sys.monitoring.use_tool_id(TOOL_ID, "repro")
sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.JUMP, callback)
sys.monitoring.set_events(TOOL_ID, sys.monitoring.events.JUMP)

try:
    for i in range(3):  # JUMP event fires on loop back-edge
        pass
except ValueError as e:
    print(f"Caught ValueError: {e}")  # This is never reached
finally:
    sys.monitoring.set_events(TOOL_ID, 0)
    sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.JUMP, None)
    sys.monitoring.free_tool_id(TOOL_ID)

print("Test complete")

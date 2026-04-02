"""
Bug 2: sys.monitoring JUMP/BRANCH callback exceptions bypass try/except
=======================================================================

When a JUMP or BRANCH monitoring callback raises an exception, the exception
is raised but bypasses enclosing try/except handlers.

Affected events: JUMP, BRANCH
Not affected: Most other events properly propagate exceptions

Python version: 3.13.12 (CPython)

Expected behavior: The ValueError should be caught by the except clause.
Actual behavior: The ValueError propagates as an unhandled exception,
bypassing the try/except handler.
"""

import sys

sys.monitoring.use_tool_id(0, "repro")

sys.monitoring.register_callback(
    0,
    sys.monitoring.events.JUMP,
    lambda *args: (_ for _ in ()).throw(ValueError("jump_boom")),
)
sys.monitoring.set_events(0, sys.monitoring.events.JUMP)

# Expected: ValueError is caught by except clause
# Actual: ValueError bypasses the try/except and crashes the program
try:
    for i in range(3):  # JUMP event fires on loop back-edge
        pass
except ValueError as e:
    print(f"Caught ValueError: {e}")  # This is never reached
finally:
    sys.monitoring.set_events(0, 0)
    sys.monitoring.register_callback(0, sys.monitoring.events.JUMP, None)
    sys.monitoring.free_tool_id(0)

print("Test complete")

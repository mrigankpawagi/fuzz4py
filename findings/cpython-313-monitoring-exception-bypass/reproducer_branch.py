"""
Bug 2b: sys.monitoring BRANCH callback exceptions bypass try/except
===================================================================

Same underlying issue as Bug 2 (JUMP), but with the BRANCH event.
BRANCH events fire on conditional branches (if/else, etc.)

Python version: 3.13.12 (CPython)

Expected behavior: The ValueError should be caught by the except clause.
Actual behavior: The ValueError propagates as an unhandled exception.
"""

import sys

sys.monitoring.use_tool_id(0, "repro")

sys.monitoring.register_callback(
    0,
    sys.monitoring.events.BRANCH,
    lambda code, offset, target: (_ for _ in ()).throw(ValueError("branch_boom")),
)
sys.monitoring.set_events(0, sys.monitoring.events.BRANCH)

x = True  # variable so the branch isn't constant-folded

try:
    if x:  # BRANCH event fires here -> ValueError raised
        result = 1
    else:
        result = 2
except ValueError as e:
    print(f"Caught: {e}")  # This is never reached
finally:
    sys.monitoring.set_events(0, 0)
    sys.monitoring.register_callback(0, sys.monitoring.events.BRANCH, None)
    sys.monitoring.free_tool_id(0)

print("Test complete")

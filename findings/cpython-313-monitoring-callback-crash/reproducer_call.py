"""
Bug 1b: sys.monitoring CALL callback crash (variant of Bug 1)
=============================================================

Same underlying issue as Bug 1, but with the CALL event.

When a CALL monitoring callback always raises an exception, the exception
handling code itself makes function calls (e.g., print(), set_events()),
which trigger the CALL callback again, leading to a crash.

Python version: 3.13.12 (CPython)
"""

import sys

sys.monitoring.use_tool_id(0, "repro")
sys.monitoring.register_callback(
    0,
    sys.monitoring.events.CALL,
    lambda code, offset, callable_obj, arg0: (_ for _ in ()).throw(
        ValueError("boom")
    ),
)
sys.monitoring.set_events(0, sys.monitoring.events.CALL)

try:
    len([1, 2, 3])  # CALL callback raises -> crash
except ValueError:
    print("This is never reached")

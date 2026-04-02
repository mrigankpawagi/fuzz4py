"""
sys.monitoring CALL callback crash

Same root cause as the LINE variant: when a CALL monitoring callback always
raises an exception, subsequent function calls (even in except/finally)
re-trigger the callback, causing CPython to crash.

Interpreter: CPython 3.13
Expected: The ValueError is raised and can be caught by try/except.
Actual: CPython prints an internal object dump and exits with code 1.
"""

import sys

TOOL_ID = 0

def callback(code, offset, callable_obj, arg0):
    raise ValueError("boom")

sys.monitoring.use_tool_id(TOOL_ID, "repro")
sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.CALL, callback)
sys.monitoring.set_events(TOOL_ID, sys.monitoring.events.CALL)

try:
    len([1, 2, 3])  # triggers CALL callback, which raises ValueError
except ValueError:
    print("This line is never reached")

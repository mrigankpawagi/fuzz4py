"""
sys.monitoring LINE callback crash

When a sys.monitoring LINE callback raises an exception, CPython crashes
with an internal _PyObject_Dump and "lost sys.stderr" instead of propagating
the exception normally.

Interpreter: CPython 3.13
Expected: The ValueError is raised and can be caught by try/except.
Actual: CPython prints an internal object dump and exits with code 1.

    object address  : 0x...
    object refcount : 3
    object type     : 0x...
    object type name: ValueError
    object repr     : ValueError('boom')
    lost sys.stderr
"""

import sys

print(f"Python: {sys.version}")
print(f"Executable: {sys.executable}")

TOOL_ID = 0

def callback(code, line):
    raise ValueError("boom")

sys.monitoring.use_tool_id(TOOL_ID, "repro")
sys.monitoring.register_callback(TOOL_ID, sys.monitoring.events.LINE, callback)
sys.monitoring.set_events(TOOL_ID, sys.monitoring.events.LINE)

# If the bug is present, the next line triggers the crash and nothing
# below is printed. If the bug is NOT present, the ValueError propagates
# normally and is caught.
try:
    x = 1  # triggers LINE callback, which raises ValueError
except ValueError:
    print("BUG NOT TRIGGERED: ValueError was caught normally")
    sys.monitoring.set_events(TOOL_ID, 0)
    sys.monitoring.free_tool_id(TOOL_ID)

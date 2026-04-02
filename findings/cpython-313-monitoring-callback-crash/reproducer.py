"""
sys.monitoring LINE callback exception bypasses try/except

When a sys.monitoring LINE callback raises an exception, the exception
bypasses the enclosing try/except handler instead of being caught normally.

Interpreter: CPython 3.13
Expected: The ValueError is caught by the except clause, and "CAUGHT" is printed.
Actual: The ValueError bypasses try/except and crashes as an unhandled exception.
        (On some machines, this may instead produce an internal _PyObject_Dump.)

Compare with PY_START, where exceptions from callbacks ARE caught correctly.
"""

import sys

print(f"Python {sys.version}")

# ---- Control: PY_START correctly propagates exceptions ----
def py_start_cb(*args):
    raise ValueError("from PY_START")

sys.monitoring.use_tool_id(0, "repro")
sys.monitoring.register_callback(0, sys.monitoring.events.PY_START, py_start_cb)
sys.monitoring.set_events(0, sys.monitoring.events.PY_START)

try:
    def f(): pass
    f()  # triggers PY_START → ValueError
except ValueError:
    print("CONTROL OK: PY_START exception was caught by try/except (correct)")

sys.monitoring.set_events(0, 0)
sys.monitoring.register_callback(0, sys.monitoring.events.PY_START, None)
sys.monitoring.free_tool_id(0)

# ---- Bug: LINE does NOT correctly propagate exceptions ----
def line_cb(code, line):
    raise ValueError("from LINE")

sys.monitoring.use_tool_id(0, "repro")
sys.monitoring.register_callback(0, sys.monitoring.events.LINE, line_cb)
sys.monitoring.set_events(0, sys.monitoring.events.LINE)

try:
    x = 1  # triggers LINE → ValueError — but it bypasses this try/except!
except ValueError:
    print("BUG NOT PRESENT: LINE exception was caught by try/except")
    sys.monitoring.set_events(0, 0)
    sys.monitoring.free_tool_id(0)
else:
    print("BUG NOT PRESENT: no exception raised")
    sys.monitoring.set_events(0, 0)
    sys.monitoring.free_tool_id(0)

# If the bug is present, we never reach this line.
print("Done")

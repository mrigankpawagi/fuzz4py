Return Code: 0
Stdout: b'Thread 123173001496128 results: [7, 8, 9]\nThread 123172980524608 results: [7, 8, 9]\nposix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4561724.69)\nSSL context: <ssl.SSLContext object at 0x7006741fad50>\n'
Stderr: b'Exception in thread Thread-1 (thread_function):\nException in thread Thread-3 (thread_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 26, in thread_function\n    results = complex_function(data, replace_flag)\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 16, in complex_function\n    data = copy.replace(data, new_val=[1,2])  # test copy.replace\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace\n    raise TypeError(f"replace() does not support {cls.__name__} objects")\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 26, in thread_function\n    results = complex_function(data, replace_flag)\nTypeError: replace() does not support list objects\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 16, in complex_function\n    data = copy.replace(data, new_val=[1,2])  # test copy.replace\n  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace\n    raise TypeError(f"replace() does not support {cls.__name__} objects")\nTypeError: replace() does not support list objects\n'

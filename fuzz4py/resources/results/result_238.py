Return Code: 0
Stdout: b"Thread Error: Result too large\nThread Error: Result too large\nThread Error: Result too large\nThread Error: invalid literal for int() with base 10: b'byte'\nThread Error: invalid literal for int() with base 10: 'abc'\nThread Error: Result too large\nOriginal object: 10, new object: 20\nDBM Error: NOT NULL constraint failed: Dict.value\nTime results from os.times(): posix.times_result(user=0.04, system=0.01, children_user=0.0, children_system=0.0, elapsed=4561726.97)\nSSL context created successfully\nSSL context created successfully with client auth\n"
Stderr: b'Exception in thread Thread-16 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function\n    result = int(input_data) * 2\n             ~~~^^^^^^^^^^^^\nTypeError: int() argument must be a string, a bytes-like object or a real number, not \'list\'\nException in thread Thread-14 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function\n    result = int(input_data) * 2\n             ~~~^^^^^^^^^^^^\nTypeError: int() argument must be a string, a bytes-like object or a real number, not \'NoneType\'\nException in thread Thread-15 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function\n    result = int(input_data) * 2\n             ~~~^^^^^^^^^^^^\nTypeError: int() argument must be a string, a bytes-like object or a real number, not \'list\'\n'

Return Code: 0
Stdout: b'threading with GIL\nthreading without GIL\nObject after replacement: 42\nposix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4561186.14)\nTime taken for os.times(): 3.697990905493498e-06\nSSL context created.\n'
Stderr: b'Exception in thread Thread-1 (complex_function):\nException in thread Thread-2 (complex_function):\nException in thread Thread-3 (complex_function):\nException in thread Thread-4 (complex_function):\nException in thread Thread-5 (complex_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nException in thread Thread-6 (complex_function):\nException in thread Thread-7 (complex_function):\nException in thread Thread-9 (complex_function):\nException in thread Thread-8 (complex_function):\nTraceback (most recent call last):\nException in thread Thread-10 (complex_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n'
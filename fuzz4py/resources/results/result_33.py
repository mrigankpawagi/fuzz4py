Return Code: 0
Stdout: b"threading with GIL\nthreading without GIL\nObject after replacement: 42\nposix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4561186.2)\nTime taken for os.times(): 3.545952495187521e-06\nSSL context created.\n{1: 1.0, 2: 2.0, 3: 3.0}\nError in my_function: Forced error, arg1: 1, arg2: test86\nThread 127981928318528 processed: 1, result: nan\nThread 127981970261568 processed: 1, result: 6.0\nThread 127981959775808 processed: 1, result: 6.0\nError in my_function: object of type 'NoneType' has no len(), arg1: 1, arg2: None\nThread 127981949290048 processed: 1, result: nan\nThread 127981938804288 processed: 1, result: 6.0\nThread 127981928318528 processed: 2, result: 12.0\nError in my_function: Forced error, arg1: 2, arg2: test83\nThread 127981970261568 processed: 2, result: nan\nThread 127981959775808 processed: 2, result: 12.0\nError in my_function: Forced error, arg1: 2, arg2: None\nThread 127981949290048 processed: 2, result: nan\nError in my_function: Forced error, arg1: 2, arg2: test42\nThread 127981938804288 processed: 2, result: nan\nError in my_function: object of type 'NoneType' has no len(), arg1: 3, arg2: None\nThread 127981928318528 processed: 3, result: nan\nError in my_function: object of type 'NoneType' has no len(), arg1: 3, arg2: None\nThread 127981970261568 processed: 3, result: nan\nThread 127981959775808 processed: 3, result: 18.0\nThread 127981949290048 processed: 3, result: 18.0\nThread 127981938804288 processed: 3, result: 18.0\nThread 127981928318528 processed: 4, result: 20.0\nError in my_function: object of type 'NoneType' has no len(), arg1: 4, arg2: None\nThread 127981970261568 processed: 4, result: nan\nThread 127981959775808 processed: 4, result: 24.0\nError in my_function: Forced error, arg1: 4, arg2: test93\nThread 127981949290048 processed: 4, result: nan\nThread 127981938804288 processed: 4, result: 24.0\nThread 127981928318528 processed: 5, result: 30.0\nThread 127981970261568 processed: 5, result: 30.0\nThread 127981959775808 processed: 5, result: 30.0\nThread 127981949290048 processed: 5, result: 30.0\nError in my_function: Forced error, arg1: 5, arg2: test100\nThread 127981938804288 processed: 5, result: nan\ndocstring\n"
Stderr: b'Exception in thread Thread-1 (complex_function):\nException in thread Thread-2 (complex_function):\nException in thread Thread-3 (complex_function):\nException in thread Thread-4 (complex_function):\nException in thread Thread-5 (complex_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nException in thread Thread-6 (complex_function):\nException in thread Thread-7 (complex_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nException in thread Thread-8 (complex_function):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nException in thread Thread-9 (complex_function):\nException in thread Thread-10 (complex_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function\n    if i > 10:\n       ^^^^^^\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\nTypeError: \'>\' not supported between instances of \'list\' and \'int\'\n'
Return Code: 0
Stdout: b'\nThis is a docstring.\n\n5\n(10, 20)\nos.times() took: 4.742003511637449e-06\nCopy replace result: [1, 2, 42, 4, 5]\nSuccessfully created default context.\n'
Stderr: b'Exception in thread Thread-6 (<lambda>):\nException in thread Thread-7 (<lambda>):\nException in thread Thread-8 (<lambda>):\nException in thread Thread-9 (<lambda>):\nException in thread Thread-10 (<lambda>):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\nTypeError: object of type \'int\' has no len()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\nTypeError: object of type \'int\' has no len()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\nTypeError: object of type \'int\' has no len()\nTypeError: object of type \'int\' has no len()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\nTypeError: object of type \'int\' has no len()\n'
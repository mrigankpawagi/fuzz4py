Return Code: 0
Stdout: b'os.times() took: 1.9189901649951935e-06\nCopy replace result: [1, 2, 42, 4, 5]\nSuccessfully created default context.\n'
Stderr: b'Exception in thread Thread-1 (<lambda>):\nException in thread Thread-2 (<lambda>):\nException in thread Thread-3 (<lambda>):\nException in thread Thread-4 (<lambda>):\nException in thread Thread-5 (<lambda>):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\nTypeError: object of type \'int\' has no len()\nTypeError: object of type \'int\' has no len()\nTypeError: object of type \'int\' has no len()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\nTypeError: object of type \'int\' has no len()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>\n    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())\n                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function\n    for i in range(len(data)):\n                   ~~~^^^^^^\nTypeError: object of type \'int\' has no len()\n'

Return Code: 0
Stdout: b'Data after modification: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]\n'
Stderr: b'Exception in thread Thread-2 (worker):\nException in thread Thread-3 (worker):\nException in thread Thread-4 (worker):\nException in thread Thread-5 (worker):\nException in thread Thread-6 (worker):\nException in thread Thread-7 (worker):\nException in thread Thread-8 (worker):\nException in thread Thread-9 (worker):\nException in thread Thread-10 (worker):\nException in thread Thread-11 (worker):\nException in thread Thread-12 (worker):\nException in thread Thread-13 (worker):\nException in thread Thread-14 (worker):\nException in thread Thread-15 (worker):\nException in thread Thread-16 (worker):\nException in thread Thread-17 (worker):\nException in thread Thread-18 (worker):\nException in thread Thread-19 (worker):\nTraceback (most recent call last):\nTraceback (most recent call last):\nException in thread Thread-20 (worker):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\nIndexError: list index out of range\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\nIndexError: list index out of range\nIndexError: list index out of range\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/218.py", line 18, in worker\n    data[i] = data[i] + i  # this operation can trigger JIT compilation\n              ~~~~^^^\nIndexError: list index out of range\nIndexError: list index out of range\n'
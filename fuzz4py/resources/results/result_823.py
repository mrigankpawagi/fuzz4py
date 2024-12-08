Return Code: 0
Stdout: Error interacting with dbm.sqlite3: module 'dbm' has no attribute 'sqlite3'
Error in timer fuzzing: posix.times() takes no arguments (1 given)
Error loading invalid CA: [Errno 2] No such file or directory
Default SSL context created successfully.
invalid 2
[2, 4, 9, -1, -1]
[137462998787904, 137462998787904, 137462998787904, 137462998787904, 137462998787904, 137462998787904, 137462998787904, 137462998787904]

Stderr: Exception in thread Thread-6 (worker):
Exception in thread Thread-7 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/823.py", line 14, in worker
    data += random.randint(-5, 5)  # Introduce randomness
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
TypeError: can only concatenate str (not "int") to str
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/823.py", line 14, in worker
    data += random.randint(-5, 5)  # Introduce randomness
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: can only concatenate str (not "int") to str


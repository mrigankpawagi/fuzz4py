Return Code: 0
Stdout: Race condition result: [0, 0, 1, 2, 4, 3, 4, 16, 5, 6, 36, 7, 8, 64, 9]
An error occurred: module 'copy' has no attribute 'namedtuple'

Stderr: Exception in thread Thread-10 (process_item):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/388.py", line 46, in process_item
    raise ValueError("Simulated error")
ValueError: Simulated error


Return Code: 0
Stdout: Thread 0: Started
Thread 1: Started
Thread 2: Started
Thread 3: Started
Thread 4: Started
Thread 0: Finished
Thread 1: Finished
Thread 4: Finished
Thread 3: Finished
Thread 2: Finished
All tests completed.

Stderr: Exception in thread Thread-3 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-1 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-4 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/784.py", line 40, in worker
    dbm.close()
    ^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/784.py", line 40, in worker
    dbm.close()
    ^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/784.py", line 40, in worker
    dbm.close()
    ^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/784.py", line 40, in worker
    dbm.close()
    ^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/784.py", line 40, in worker
    dbm.close()
    ^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'
AttributeError: module 'dbm' has no attribute 'close'
AttributeError: module 'dbm' has no attribute 'close'


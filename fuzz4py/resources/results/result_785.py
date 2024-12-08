Return Code: 0
Stdout: My object: 10, bad
My object: 10, bad
My object: 10, bad
Database entry not found.
Error in SSL handling: cafile, capath and cadata cannot be all omitted
os.times() result: posix.times_result(user=0.05, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612554.43)
Error during os.times(): posix.times() takes no arguments (1 given)
['1', '2', '3']
['s', 't', 'r', 'i', 'n', 'g']
Thread 0: Started
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

Stderr: Exception in thread Thread-4 (worker):
Exception in thread Thread-7 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-6 (worker):
Exception in thread Thread-8 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/785.py", line 136, in worker
    dbm.close()
    ^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/785.py", line 136, in worker
    dbm.close()
    ^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/785.py", line 136, in worker
    dbm.close()
    ^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/785.py", line 136, in worker
    dbm.close()
    ^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'
AttributeError: module 'dbm' has no attribute 'close'
AttributeError: module 'dbm' has no attribute 'close'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/785.py", line 136, in worker
    dbm.close()
    ^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'close'


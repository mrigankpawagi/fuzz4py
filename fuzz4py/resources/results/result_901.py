Return Code: 0
Stdout: Time taken for os.times(): 0.000007
posix.times_result(user=0.05, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612709.84)
Time taken for os.times(): 0.000003
posix.times_result(user=0.05, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612709.84)
Original object: 20, New object: 20
SSL context created successfully

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-3 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
KeyError: 0
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 4
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
KeyError: 3
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
KeyError: 2
KeyError: 1


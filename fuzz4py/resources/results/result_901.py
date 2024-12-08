Return Code: 0
Stdout: Time taken for os.times(): 0.000010
posix.times_result(user=0.06, system=0.01, children_user=0.0, children_system=0.0, elapsed=4606802.12)
Time taken for os.times(): 0.000005
posix.times_result(user=0.06, system=0.01, children_user=0.0, children_system=0.0, elapsed=4606802.12)
Original object: 20, New object: 20
SSL context created successfully

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
KeyError: 1
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 3
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/901.py", line 14, in worker
    shared_data[arg] += 1  # Potential race condition if not properly protected
    ~~~~~~~~~~~^^^^^
KeyError: 0
KeyError: 4
KeyError: 2


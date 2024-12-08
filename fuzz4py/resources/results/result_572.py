Return Code: 0
Stdout: Unexpected type!
Time elapsed: 1.9073486328125e-06, Results: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606386.84)
Error: Certificate file not found or other error: [Errno 2] No such file or directory: '/path/to/nonexistent/cert.pem'

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/572.py", line 17, in worker
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/572.py", line 17, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/572.py", line 17, in worker
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/572.py", line 17, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/572.py", line 17, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value


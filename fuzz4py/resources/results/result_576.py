Return Code: 1
Stdout: Unexpected type!
Time elapsed: 7.62939453125e-06, Results: posix.times_result(user=0.05, system=0.01, children_user=0.0, children_system=0.0, elapsed=4612301.35)
Error: Certificate file not found or other error: [Errno 2] No such file or directory: 'path/to/custom.pem'

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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 97, in worker
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 97, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 97, in worker
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 97, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 97, in worker
    with lock:
         ^^^^
UnboundLocalError: cannot access local variable 'lock' where it is not associated with a value
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 230, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/576.py", line 222, in main
    test_complex_annotations()
    ~~~~~~~~~~~~~~~~~~~~~~~~^^
TypeError: test_complex_annotations() missing 1 required positional argument: 'data'


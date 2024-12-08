Return Code: 0
Stdout: copy.replace result: 62
dbm.sqlite3 error: module 'dbm' has no attribute 'sqlite3'
Free Threading result: 90 global_var: 0

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/685.py", line 33, in worker
    global_var += 10
    ^^^^^^^^^^
NameError: name 'global_var' is not defined
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/685.py", line 33, in worker
    global_var += 10
    ^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/685.py", line 33, in worker
    global_var += 10
    ^^^^^^^^^^
NameError: name 'global_var' is not defined
NameError: name 'global_var' is not defined


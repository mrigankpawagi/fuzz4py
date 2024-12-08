Return Code: 0
Stdout: copy.replace result: -19
dbm.sqlite3 open error: module 'dbm' has no attribute 'sqlite3'
Free Threading result: 26 global_var: 0

Stderr: Exception in thread Thread-1 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/687.py", line 43, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
NameError: name 'global_var' is not defined


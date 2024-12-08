Return Code: 0
Stdout: copy.replace result: -92
dbm.sqlite3 open error: module 'dbm' has no attribute 'sqlite3'
Free Threading result: 111 global_var: 0

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-8 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-6 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-7 (worker):
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
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
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
NameError: name 'global_var' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
NameError: name 'global_var' is not defined
NameError: name 'global_var' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
NameError: name 'global_var' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'global_var' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
NameError: name 'global_var' is not defined
NameError: name 'global_var' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/686.py", line 36, in worker
    global_var += random.randint(1, 10)  # Random increment
    ^^^^^^^^^^
NameError: name 'global_var' is not defined


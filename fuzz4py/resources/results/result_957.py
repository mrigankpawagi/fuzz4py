Return Code: 0
Stdout: Finished.
dbm error: attempt to write a readonly database

Stderr: Exception in thread Thread-2 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-6 (worker):
Exception in thread Thread-8 (worker):
Exception in thread Thread-10 (worker):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/957.py", line 12, in worker
    data_copy = data_copy._replace(value=data_copy.value + 1)
                ^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/957.py", line 12, in worker
    data_copy = data_copy._replace(value=data_copy.value + 1)
                ^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/957.py", line 12, in worker
    data_copy = data_copy._replace(value=data_copy.value + 1)
                ^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
AttributeError: 'Replaceable' object has no attribute '_replace'. Did you mean: '__replace__'?
AttributeError: 'Replaceable' object has no attribute '_replace'. Did you mean: '__replace__'?
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/957.py", line 12, in worker
    data_copy = data_copy._replace(value=data_copy.value + 1)
                ^^^^^^^^^^^^^^^^^^
AttributeError: 'Replaceable' object has no attribute '_replace'. Did you mean: '__replace__'?
AttributeError: 'Replaceable' object has no attribute '_replace'. Did you mean: '__replace__'?
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/957.py", line 12, in worker
    data_copy = data_copy._replace(value=data_copy.value + 1)
                ^^^^^^^^^^^^^^^^^^
AttributeError: 'Replaceable' object has no attribute '_replace'. Did you mean: '__replace__'?


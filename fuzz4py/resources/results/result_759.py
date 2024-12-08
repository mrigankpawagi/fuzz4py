Return Code: 0
Stdout: Elapsed time: 0.33

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-3 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Exception in thread Thread-2 (worker):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/759.py", line 16, in worker
    arg = copy.replace(arg, new_val=arg * 2)
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: replace() does not support int objects
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/759.py", line 16, in worker
    arg = copy.replace(arg, new_val=arg * 2)
Exception in thread Thread-4 (worker):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/759.py", line 16, in worker
    arg = copy.replace(arg, new_val=arg * 2)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
Traceback (most recent call last):
TypeError: replace() does not support int objects
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
TypeError: replace() does not support int objects
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/759.py", line 16, in worker
    arg = copy.replace(arg, new_val=arg * 2)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support int objects
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/759.py", line 16, in worker
    arg = copy.replace(arg, new_val=arg * 2)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support int objects


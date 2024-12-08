Return Code: 0
Stdout: not a number
An error occurred: can only concatenate str (not "int") to str

Stderr: Exception in thread Thread-4 (increment_counter):
Exception in thread Thread-2 (increment_counter):
Exception in thread Thread-1 (increment_counter):
Exception in thread Thread-3 (increment_counter):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter
    shared_counter += 1
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter
    shared_counter += 1
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
TypeError: can only concatenate str (not "int") to str
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter
    shared_counter += 1
TypeError: can only concatenate str (not "int") to str
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter
    shared_counter += 1
TypeError: can only concatenate str (not "int") to str
TypeError: can only concatenate str (not "int") to str


Return Code: 0
Stdout: None
An error occurred: 'int' object is not iterable

Stderr: Exception in thread Thread-4 (increment_counter):
Exception in thread Thread-5 (increment_counter):
Exception in thread Thread-2 (increment_counter):
Exception in thread Thread-3 (increment_counter):
Exception in thread Thread-7 (increment_counter):
Exception in thread Thread-1 (increment_counter):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
TypeError: can only concatenate str (not "int") to str
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
TypeError: can only concatenate str (not "int") to str
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
TypeError: can only concatenate str (not "int") to str
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
Exception in thread Thread-6 (increment_counter):
Exception in thread Thread-8 (increment_counter):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/283.py", line 17, in increment_counter
    shared_counter += 1
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'


Return Code: 0
Stdout: 3 2

This is a
docstring.

Time taken: 0.0000
posix.times_result(user=0.05, system=0.01, children_user=0.0, children_system=0.0, elapsed=4610596.86)

Stderr: Exception in thread Thread-1 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-4 (threaded_function):
Exception in thread Thread-5 (threaded_function):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/102.py", line 13, in threaded_function
    result += data
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +=: 'int' and 'bytes'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/102.py", line 13, in threaded_function
    result += data
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/102.py", line 13, in threaded_function
    result += data
TypeError: unsupported operand type(s) for +=: 'int' and 'bytes'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/102.py", line 13, in threaded_function
    result += data
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/102.py", line 13, in threaded_function
    result += data
TypeError: unsupported operand type(s) for +=: 'int' and 'bytes'
TypeError: unsupported operand type(s) for +=: 'int' and 'bytes'
TypeError: unsupported operand type(s) for +=: 'int' and 'bytes'


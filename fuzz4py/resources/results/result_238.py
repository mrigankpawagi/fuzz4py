Return Code: 0
Stdout: Thread Error: Result too large
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: 'abc'
Thread Error: Result too large
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: b'byte'
Original object: 10, new object: 20
DBM Error: NOT NULL constraint failed: Dict.value
Time results from os.times(): posix.times_result(user=0.04, system=0.0, children_user=0.0, children_system=0.0, elapsed=4611005.75)
SSL context created successfully
SSL context created successfully with client auth

Stderr: Exception in thread Thread-15 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
Exception in thread Thread-16 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
Exception in thread Thread-14 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/238.py", line 26, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'


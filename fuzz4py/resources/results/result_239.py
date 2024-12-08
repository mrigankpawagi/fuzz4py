Return Code: 0
Stdout: Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: b'invalidbytes'
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: 'invalid'
Thread Error: Negative result with non-zero input
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: b''
Thread Error: invalid literal for int() with base 10: 'abc'
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: ''
Thread Error: Result too large
Thread Error: invalid literal for int() with base 10: b'byte'
Thread Error: invalid literal for int() with base 10: b'\x00\x01\x02'
Original object: 10, new object: 20
Bad obj: not_a_number
DBM Error: NOT NULL constraint failed: Dict.value
Time results from os.times(): posix.times_result(user=0.07, system=0.01, children_user=0.0, children_system=0.0, elapsed=4611005.99)
SSL context created successfully

Stderr: Exception in thread Thread-19 (threaded_function):
Exception in thread Thread-14 (threaded_function):
Traceback (most recent call last):
Traceback (most recent call last):
Exception in thread Thread-30 (threaded_function):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'function'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
Exception in thread Thread-17 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
Exception in thread Thread-18 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
Exception in thread Thread-28 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
Exception in thread Thread-15 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
Exception in thread Thread-29 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
Exception in thread Thread-20 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
Exception in thread Thread-21 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/239.py", line 27, in threaded_function
    result = int(input_data) * 2
             ~~~^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'


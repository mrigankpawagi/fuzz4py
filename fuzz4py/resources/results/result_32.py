Return Code: 0
Stdout: threading with GIL
threading without GIL
Object after replacement: 42
posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604500.62)
Time taken for os.times(): 3.1740055419504642e-06
SSL context created.

Stderr: Exception in thread Thread-1 (complex_function):
Exception in thread Thread-2 (complex_function):
Exception in thread Thread-3 (complex_function):
Exception in thread Thread-4 (complex_function):
Exception in thread Thread-5 (complex_function):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
TypeError: '>' not supported between instances of 'list' and 'int'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
Exception in thread Thread-6 (complex_function):
Exception in thread Thread-7 (complex_function):
Exception in thread Thread-8 (complex_function):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-10 (complex_function):
Exception in thread Thread-9 (complex_function):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
TypeError: '>' not supported between instances of 'list' and 'int'
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/32.py", line 19, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
TypeError: '>' not supported between instances of 'list' and 'int'


Return Code: 1
Stdout: Final resource value: 0
Docstring Test
test
1

Stderr: Exception in thread Thread-1 (increment):
Exception in thread Thread-2 (increment):
Exception in thread Thread-3 (increment):
Exception in thread Thread-4 (increment):
Exception in thread Thread-5 (increment):
Traceback (most recent call last):
Traceback (most recent call last):
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
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 16, in increment
    resource += 1
    ^^^^^^^^
NameError: name 'resource' is not defined. Did you forget to import 'resource'?
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 16, in increment
    resource += 1
    ^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 16, in increment
    resource += 1
    ^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 16, in increment
    resource += 1
    ^^^^^^^^
NameError: name 'resource' is not defined. Did you forget to import 'resource'?
NameError: name 'resource' is not defined. Did you forget to import 'resource'?
NameError: name 'resource' is not defined. Did you forget to import 'resource'?
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 16, in increment
    resource += 1
    ^^^^^^^^
NameError: name 'resource' is not defined. Did you forget to import 'resource'?
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 100, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 96, in main
    dbm_test()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/27.py", line 77, in dbm_test
    db = dbm.sqlite3.open('test.db', 'c')
         ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'


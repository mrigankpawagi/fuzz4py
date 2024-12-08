Return Code: 1
Stdout: Error processing -3: Input must be non-negative
[]

Stderr: Exception in thread Thread-1 (process_element):
Exception in thread Thread-2 (process_element):
Exception in thread Thread-4 (process_element):
Exception in thread Thread-5 (process_element):
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
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 40, in process_element
    with dbm.sqlite3.open('test.db', 'c') as db:
         ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 40, in process_element
    with dbm.sqlite3.open('test.db', 'c') as db:
         ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 40, in process_element
    with dbm.sqlite3.open('test.db', 'c') as db:
         ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 40, in process_element
    with dbm.sqlite3.open('test.db', 'c') as db:
         ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'
AttributeError: module 'dbm' has no attribute 'sqlite3'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 85, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 73, in main
    test_replacement()
    ~~~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/289.py", line 56, in test_replacement
    obj2 = copy.replace(obj1)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
TypeError: test_replacement.<locals>.MyObject.__replace__() missing 1 required positional argument: 'other'


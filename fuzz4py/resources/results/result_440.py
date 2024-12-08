Return Code: 0
Stdout: Final Counter: 45
4999950000
Original: 5, Copied: 10
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
Elapsed time: 1.000148318009451
['a', 'b']
Complex function returned: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Value: 10
SSL context created successfully.
Time taken: 5.245208740234375e-06

Stderr: Exception in thread Thread-21 (worker):
Exception in thread Thread-22 (worker):
Exception in thread Thread-23 (worker):
Exception in thread Thread-24 (worker):
Exception in thread Thread-25 (worker):
Exception in thread Thread-26 (worker):
Exception in thread Thread-28 (worker):
Exception in thread Thread-27 (worker):
Exception in thread Thread-30 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-29 (worker):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
Traceback (most recent call last):
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 178, in worker
    shared_data[0] += 1
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
F
======================================================================
FAIL: test_thread_race (__main__.TestFreeThreading.test_thread_race)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/440.py", line 187, in test_thread_race
    self.assertEqual(shared_data[0], 10)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
AssertionError: 0 != 10

----------------------------------------------------------------------
Ran 1 test in 0.008s

FAILED (failures=1)


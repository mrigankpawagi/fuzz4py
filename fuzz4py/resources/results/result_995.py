Return Code: 0
Stdout: Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
Error in worker thread: 'int' object has no attribute 'acquire'
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
68 1
10 2
p4: <__main__.main.<locals>.Point object at 0x7936ba5b16d0>
p6: <__main__.main.<locals>.Point object at 0x7936ba595590>
p7: None
p8: 246
p9: string
p10: 246.912
Error interacting with dbm.sqlite3: module 'dbm' has no attribute 'sqlite3'
Error opening database: module 'dbm' has no attribute 'sqlite3'

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Exception in thread Thread-6 (worker):
Exception in thread Thread-7 (worker):
Exception in thread Thread-8 (worker):
Exception in thread Thread-9 (worker):
Exception in thread Thread-10 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
AttributeError: 'int' object has no attribute 'acquire'
AttributeError: 'int' object has no attribute 'acquire'
AttributeError: 'int' object has no attribute 'acquire'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/995.py", line 137, in worker
    lock.acquire()
    ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'acquire'
AttributeError: 'int' object has no attribute 'acquire'


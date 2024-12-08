Return Code: 0
Stdout: Key: b'-1', Value: b'-1.0'
Key: b'3', Value: b'None'
Key: b'4', Value: b'4'

Stderr: Exception in thread Thread-2 (worker):
Exception in thread Thread-9 (worker):
Exception in thread Thread-8 (worker):
Exception in thread Thread-6 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/606.py", line 33, in worker
    db = dbm.open('test.dbm', 'c')
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/606.py", line 33, in worker
    db = dbm.open('test.dbm', 'c')
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/606.py", line 33, in worker
    db = dbm.open('test.dbm', 'c')
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/606.py", line 33, in worker
    db = dbm.open('test.dbm', 'c')
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/__init__.py", line 89, in open
    raise error[0]("db type could not be determined")
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/__init__.py", line 89, in open
    raise error[0]("db type could not be determined")
dbm.error: db type could not be determined
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/__init__.py", line 89, in open
    raise error[0]("db type could not be determined")
dbm.error: db type could not be determined
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/__init__.py", line 89, in open
    raise error[0]("db type could not be determined")
dbm.error: db type could not be determined
dbm.error: db type could not be determined


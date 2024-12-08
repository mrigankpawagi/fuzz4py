Return Code: 0
Stdout: Key: b'1', Value: b'2'
Key: b'2', Value: b'4'
Key: b'3', Value: b'6'
Key: b'5', Value: b'10'

Stderr: Exception in thread Thread-4 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/604.py", line 27, in worker
    db = dbm.open('test.dbm', 'c')
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/__init__.py", line 89, in open
    raise error[0]("db type could not be determined")
dbm.error: db type could not be determined


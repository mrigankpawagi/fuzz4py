Return Code: 0
Stdout: Thread 0: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176626144832.
Thread 1: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176615659072.
Thread 2: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176529675840.
Thread 3: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176519190080.
Thread 4: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176508704320.
Database operations completed.
Error during SSL connection attempt: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'example.com'. (_ssl.c:1018)

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/672.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/672.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176508704320.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/672.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/672.py", line 16, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176626144832.
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176615659072.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176529675840.
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/672.py", line 16, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127176647735104 and this is thread id 127176519190080.


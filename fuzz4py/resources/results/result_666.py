Return Code: 0
Stdout: Thread 0: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572615788096.
Thread 1: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572605302336.
Thread 2: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572594816576.
Thread 3: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572508833344.
Thread 4: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572498347584.
Database operations completed.
Calling os.times() with time_value=-1.2345, flags=1
Results: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612362.76)
Trying with certificate at bad_certificate.crt
SSL Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'example.com'. (_ssl.c:1018)

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/666.py", line 14, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572615788096.
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/666.py", line 14, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572605302336.
Traceback (most recent call last):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/666.py", line 14, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572594816576.
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/666.py", line 14, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/666.py", line 14, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572498347584.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 136572638414656 and this is thread id 136572508833344.


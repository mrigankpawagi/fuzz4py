Return Code: 0
Stdout: Thread 0: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293484086848.
Thread 1: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293473601088.
Thread 2: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293463115328.
Thread 3: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293379229248.
Thread 4: Error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293368743488.
Database operations completed.
Calling os.times() with time_value=-3.451607165660226, flags=0
Results: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612363.0)
Trying with certificate at does_not_exist.crt
SSL Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'example.com'. (_ssl.c:1018)

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/670.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293463115328.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/670.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/670.py", line 16, in worker
    cursor = db_conn.cursor()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/670.py", line 16, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293368743488.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293484086848.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293473601088.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/670.py", line 16, in worker
    cursor = db_conn.cursor()
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132293507299136 and this is thread id 132293379229248.


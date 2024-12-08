Return Code: 0
Stdout: Original data: 10
New data: 20
Time difference: 0.10014534601941705

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379284096576.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379305068096.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379294582336.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379273610816.

During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379315553856.
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/472.py", line 16, in worker
    db[str(i)] = data[i]
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/472.py", line 16, in worker
    db[str(i)] = data[i]
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/472.py", line 16, in worker
    db[str(i)] = data[i]
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/472.py", line 16, in worker
    db[str(i)] = data[i]
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379305068096.
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379273610816.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
Traceback (most recent call last):
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379294582336.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379284096576.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/472.py", line 16, in worker
    db[str(i)] = data[i]
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 128379340691264 and this is thread id 128379315553856.


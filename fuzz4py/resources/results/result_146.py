Return Code: 0
Stdout: Key: b'-17', Value: b'21'
Key: b'-28', Value: b'-76'
Key: b'-3', Value: b'82'
Key: b'-42', Value: b'-19'
Key: b'-436', Value: b'-6757'
Key: b'-443', Value: b'-6231'
Key: b'-46', Value: b'9383'
Key: b'-51', Value: b'-93'
Key: b'-58', Value: b'30'
Key: b'-67', Value: b'-77'
Key: b'-73', Value: b'53'
Key: b'-79', Value: b'32'
Key: b'-827', Value: b'-1822'
Key: b'-86', Value: b'-44'
Key: b'-899', Value: b'5190'
Key: b'-93', Value: b'38'
Key: b'-964', Value: b'-1903'
Key: b'0', Value: b'data0'
Key: b'0.06387548662099629', Value: b'0.8069200010356603'
Key: b'0.25621771937871707', Value: b'0.0517249744308248'
Key: b'0.28883796229358305', Value: b'0.8752209419436333'
Key: b'0.4142672248640882', Value: b'0.18867479880298177'
Key: b'0.661062995904886', Value: b'0.23531133685261918'
Key: b'0.7232036293132029', Value: b'0.9992474238885027'
Key: b'0.7531573910411854', Value: b'0.5191080771016457'
Key: b'0.8541678649901272', Value: b'0.24528241722873623'
Key: b'0.8647072290063536', Value: b'0.8128440382626381'
Key: b'0.9727104648164024', Value: b'0.3322710909717471'
Key: b'1', Value: b'data1'
Key: b'12', Value: b'43'
Key: b'13', Value: b'-88'
Key: b'16', Value: b'1'
Key: b'2', Value: b'data2'
Key: b'24', Value: b'5084'
Key: b'3', Value: b'data3'
Key: b'34', Value: b'52'
Key: b'4', Value: b'data4'
Key: b'40', Value: b'30'
Key: b'42', Value: b'87'
Key: b'5', Value: b'data5'
Key: b'51', Value: b'49'
Key: b'6', Value: b'data6'
Key: b'7', Value: b'data7'
Key: b'8', Value: b'data8'
Key: b'86', Value: b'86'
Key: b'874', Value: b'value'
Key: b'9', Value: b'data9'
Key: b'91', Value: b'94'
Key: b'key', Value: b'value'
Key: b'key1', Value: b'value1'
Key: b'key2', Value: b'\x00\x01\x02'
SSL context created successfully

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-7 (worker):
Exception in thread Thread-6 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-8 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137034008102464.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137034008102464.
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033966159424.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033861301824.
Traceback (most recent call last):
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033871787584.

During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

During handling of the above exception, another exception occurred:

sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033997616704.
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033882273344.
Traceback (most recent call last):

During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033976645184.
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033966159424.
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033861301824.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033987130944.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033997616704.

During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033871787584.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033976645184.
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/146.py", line 18, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033882273344.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 137034031404864 and this is thread id 137033987130944.


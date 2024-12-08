Return Code: 0
Stdout: Free threading results: []
Complex annotation results: ['1', '2', 3, '4', 3, None, None]
Replace protocol results: -2
Key: b'-100', Value: b'85'
Key: b'-14', Value: b'8'
Key: b'-29', Value: b'18'
Key: b'-3', Value: b'-32'
Key: b'-35', Value: b'78'
Key: b'-391', Value: b'value'
Key: b'-393', Value: b'396'
Key: b'-43', Value: b'70'
Key: b'-45', Value: b'-34'
Key: b'-49', Value: b'66'
Key: b'-5', Value: b'49'
Key: b'-60', Value: b'20'
Key: b'-69', Value: b'-58'
Key: b'-745', Value: b'6318'
Key: b'-77', Value: b'-22'
Key: b'-8', Value: b'-86'
Key: b'-831', Value: b'-7040'
Key: b'0', Value: b'data0'
Key: b'0.03200991379245455', Value: b'0.906737802703051'
Key: b'0.07195255417745372', Value: b'0.7921262801215896'
Key: b'0.07388297253336229', Value: b'0.6141421793057273'
Key: b'0.18962085395499528', Value: b'0.41638547912634527'
Key: b'0.6088846553323054', Value: b'0.9071159384178398'
Key: b'0.6299503949294151', Value: b'0.30196888614486106'
Key: b'0.631106735002531', Value: b'0.5687996018475353'
Key: b'0.729937394496781', Value: b'0.5361021750025592'
Key: b'0.9586984261666404', Value: b'0.17293769943587967'
Key: b'0.9690028863696017', Value: b'0.6005249324283715'
Key: b'1', Value: b'data1'
Key: b'14', Value: b'-42'
Key: b'2', Value: b'data2'
Key: b'21', Value: b'47'
Key: b'3', Value: b'data3'
Key: b'34', Value: b'-49'
Key: b'4', Value: b'18'
Key: b'45', Value: b'9'
Key: b'451', Value: b'-2245'
Key: b'46', Value: b'-17'
Key: b'5', Value: b'data5'
Key: b'6', Value: b'data6'
Key: b'64', Value: b'69'
Key: b'653', Value: b'3222'
Key: b'7', Value: b'data7'
Key: b'8', Value: b'data8'
Key: b'810', Value: b'9884'
Key: b'83', Value: b'53'
Key: b'9', Value: b'data9'
Key: b'987', Value: b'-8852'
Key: b'key', Value: b'value'
Key: b'key1', Value: b'value1'
Key: b'key2', Value: b'\x00\x01\x02'
SSL context created successfully.

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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
TypeError: 'int' object is not iterable
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not iterable
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
TypeError: 'int' object is not iterable
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not iterable
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not iterable
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'int' object is not iterable
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 32, in worker
    res_list.append(jit_sensitive_function(x))
                    ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 15, in jit_sensitive_function
    for i in data:
             ^^^^
TypeError: 'int' object is not iterable
TypeError: 'int' object is not iterable
TypeError: 'int' object is not iterable
TypeError: 'int' object is not iterable
Exception in thread Thread-11 (worker):
Exception in thread Thread-12 (worker):
Exception in thread Thread-14 (worker):
Exception in thread Thread-17 (worker):
Exception in thread Thread-18 (worker):
Exception in thread Thread-15 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Exception in thread Thread-16 (worker):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056423126592.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056318268992.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
Traceback (most recent call last):

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
Traceback (most recent call last):
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056297297472.
Traceback (most recent call last):
Exception in thread Thread-13 (worker):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056412640832.
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056433612352.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056286811712.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056444098112.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056307783232.
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^

During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:

  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056318268992.
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056423126592.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/149.py", line 77, in worker
    db[key] = data
    ~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056412640832.
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056286811712.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056297297472.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056307783232.
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056444098112.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135056475731776 and this is thread id 135056433612352.


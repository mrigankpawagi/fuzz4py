Return Code: 0
Stdout: b"Free threading results: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\nComplex annotation results: ['1', '2', 3, '4', 3]\nReplace protocol results: -2\nKey: b'-32', Value: b'-89'\nKey: b'-37', Value: b'-34'\nKey: b'-527', Value: b'-154'\nKey: b'-533', Value: b'value'\nKey: b'-60', Value: b'-86'\nKey: b'-61', Value: b'50'\nKey: b'-652', Value: b'-5925'\nKey: b'-677', Value: b'-2297'\nKey: b'-69', Value: b'-69'\nKey: b'-8', Value: b'12'\nKey: b'-92', Value: b'-75'\nKey: b'0', Value: b'data0'\nKey: b'0.025878006168546963', Value: b'0.8899181255663287'\nKey: b'0.028541923960295756', Value: b'0.5327551866456183'\nKey: b'0.09719547846789722', Value: b'0.07857771069212172'\nKey: b'0.2836908282865256', Value: b'0.7127681432354444'\nKey: b'0.4739631114658195', Value: b'0.27365689277583294'\nKey: b'0.5521543959999157', Value: b'0.36629109016352057'\nKey: b'0.6264368531432601', Value: b'0.5428193054991166'\nKey: b'0.7313991116316835', Value: b'0.9745055243001444'\nKey: b'0.8772868288101033', Value: b'0.9522842266820619'\nKey: b'0.8943127173881267', Value: b'0.320003665599774'\nKey: b'1', Value: b'data1'\nKey: b'127', Value: b'-1515'\nKey: b'17', Value: b'27'\nKey: b'2', Value: b'data2'\nKey: b'22', Value: b'-58'\nKey: b'3', Value: b'data3'\nKey: b'39', Value: b'95'\nKey: b'4', Value: b'data4'\nKey: b'45', Value: b'46'\nKey: b'5', Value: b'-35'\nKey: b'50', Value: b'-91'\nKey: b'51', Value: b'-46'\nKey: b'52', Value: b'-48'\nKey: b'53', Value: b'-17'\nKey: b'6', Value: b'data6'\nKey: b'7', Value: b'data7'\nKey: b'8', Value: b'data8'\nKey: b'82', Value: b'8911'\nKey: b'831', Value: b'-3375'\nKey: b'88', Value: b'99'\nKey: b'9', Value: b'data9'\nKey: b'93', Value: b'86'\nKey: b'99', Value: b'77'\nKey: b'key', Value: b'value'\nKey: b'key1', Value: b'value1'\nKey: b'key2', Value: b'\\x00\\x01\\x02'\nSSL context created successfully.\n"
Stderr: b'Exception in thread Thread-11 (worker):\nException in thread Thread-13 (worker):\nException in thread Thread-12 (worker):\nException in thread Thread-16 (worker):\nException in thread Thread-18 (worker):\nException in thread Thread-15 (worker):\nException in thread Thread-14 (worker):\nException in thread Thread-17 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196151625280.\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196151625280.\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196225025600.\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\nTraceback (most recent call last):\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196225025600.\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\nTraceback (most recent call last):\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196214539840.\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196162111040.\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n\nDuring handling of the above exception, another exception occurred:\n\n\nDuring handling of the above exception, another exception occurred:\n\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196319397440.\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196172596800.\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196183082560.\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n\nDuring handling of the above exception, another exception occurred:\n\n\nDuring handling of the above exception, another exception occurred:\n\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\nTraceback (most recent call last):\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196308911680.\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n\nDuring handling of the above exception, another exception occurred:\n\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/148.py", line 80, in worker\n    db[key] = data\n    ~~^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196214539840.\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196162111040.\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196319397440.\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196183082560.\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196172596800.\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 124196342675264 and this is thread id 124196308911680.\n'
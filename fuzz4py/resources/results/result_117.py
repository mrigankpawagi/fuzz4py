Return Code: 0
Stdout: b'Result of complex_function: 499500\nSuccessful DB access.\nSSL context created successfully.\n'
Stderr: b'Exception in thread Thread-1 (thread_func):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nsqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 126946606675776 and this is thread id 126946583250496.\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/117.py", line 39, in thread_func\n    db[\'key2\'] = \'value2\'\n    ~~^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\ndbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 126946606675776 and this is thread id 126946583250496.\n'
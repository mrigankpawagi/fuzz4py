Return Code: 0
Stdout: Shared Resource: 40, Results: [None, None, None, None]
Error converting argument: invalid literal for int() with base 10: 'hello'
Error converting argument: int() argument must be a string, a bytes-like object or a real number, not 'ReplaceableClass'
[1, 2, 3, 4, 5]
value = b'value1'
Result of complex_function: 499500
Successful DB access.
SSL context created successfully.

Stderr: Exception in thread Thread-17 (thread_func):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127280898922304 and this is thread id 127280548415040.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/118.py", line 220, in thread_func
    db['key2'] = 'value2'
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 127280898922304 and this is thread id 127280548415040.


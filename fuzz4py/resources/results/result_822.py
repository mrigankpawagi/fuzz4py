Return Code: 1
Stdout: b"Error interacting with dbm.sqlite3: module 'dbm' has no attribute 'sqlite3'\nOS time elapsed: 0.0000\nDefault SSL context created successfully.\n3 2\n[]\n[128456317450048, 128456317450048, 128456317450048, 128456317450048, 128456317450048]\nResult of copy.copy() on list: [1, 2, 3]\nResult of copy.copy() on tuple: (1, 2, 3)\nResult of copy.copy() on string: hello\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute\n    return closing(self._cx.execute(*args, **kwargs))\n                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nsqlite3.IntegrityError: NOT NULL constraint failed: Dict.value\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/822.py", line 119, in fuzz_dbm\n    db[\'key4\'] = None\n    ~~^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__\n    self._execute(STORE_KV, (key, value))\n    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute\n    raise error(str(exc))\ndbm.sqlite3.error: NOT NULL constraint failed: Dict.value\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/822.py", line 182, in <module>\n    dbm_result = fuzz_dbm()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/822.py", line 132, in fuzz_dbm\n    except (dbm.error, OSError) as e:\n        return f"Error during dbm fuzzing: {e}"\nTypeError: catching classes that do not inherit from BaseException is not allowed\n'

Return Code: 1
Stdout: Error interacting with dbm.sqlite3: module 'dbm' has no attribute 'sqlite3'
OS time elapsed: 0.0000
Default SSL context created successfully.
3 2
[]
[132565355362112, 132565355362112, 132565355362112, 132565355362112, 132565355362112]
Result of copy.copy() on list: [1, 2, 3]
Result of copy.copy() on tuple: (1, 2, 3)
Result of copy.copy() on string: hello

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 79, in _execute
    return closing(self._cx.execute(*args, **kwargs))
                   ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
sqlite3.IntegrityError: NOT NULL constraint failed: Dict.value

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/821.py", line 130, in fuzz_dbm
    db['key4'] = None
    ~~^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 96, in __setitem__
    self._execute(STORE_KV, (key, value))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 81, in _execute
    raise error(str(exc))
dbm.sqlite3.error: NOT NULL constraint failed: Dict.value

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/821.py", line 196, in <module>
    dbm_result = fuzz_dbm()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/821.py", line 143, in fuzz_dbm
    except (dbm.error, OSError) as e:
        return f"Error during dbm fuzzing: {e}"
TypeError: catching classes that do not inherit from BaseException is not allowed


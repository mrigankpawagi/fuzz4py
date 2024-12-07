Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/991.py", line 120, in <module>\n    def worker(data: list, lock: threading.Lock, db: dbm.sqlite3):\n                                                     ^^^^^^^^^^^\nAttributeError: module \'dbm\' has no attribute \'sqlite3\'\n'

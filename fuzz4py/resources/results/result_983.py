Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/983.py", line 63, in <module>\n    def worker(data: list[int], lock: threading.Lock, db: dbm.sqlite3):\n                                                          ^^^^^^^^^^^\nAttributeError: module \'dbm\' has no attribute \'sqlite3\'\n'
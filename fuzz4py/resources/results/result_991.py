Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/991.py", line 120, in <module>
    def worker(data: list, lock: threading.Lock, db: dbm.sqlite3):
                                                     ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'


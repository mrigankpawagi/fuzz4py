Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/979.py", line 62, in <module>
    def worker(data: typing.List[int], lock: threading.Lock, db: dbm.sqlite3):
                                                                 ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'


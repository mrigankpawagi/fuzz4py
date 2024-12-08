Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/895.py", line 20, in <module>
    def multithreaded_function(data: typing.List[int], context: dbm.sqlite3.DB) -> int:
                                                                ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'


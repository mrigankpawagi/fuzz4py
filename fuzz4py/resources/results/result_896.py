Return Code: 1
Stdout: Elapsed time: 4.93043355003465
SSL connection attempted (fuzzed)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/896.py", line 142, in <module>
    def multithreaded_function(data: typing.List[int], context: dbm.sqlite3.DB) -> int:
                                                                ^^^^^^^^^^^^^^
AttributeError: module 'dbm.sqlite3' has no attribute 'DB'


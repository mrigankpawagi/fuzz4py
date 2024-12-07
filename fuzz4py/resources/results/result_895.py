Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/895.py", line 20, in <module>\n    def multithreaded_function(data: typing.List[int], context: dbm.sqlite3.DB) -> int:\n                                                                ^^^^^^^^^^^\nAttributeError: module \'dbm\' has no attribute \'sqlite3\'\n'

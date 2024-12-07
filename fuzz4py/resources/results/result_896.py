Return Code: 1
Stdout: b'Elapsed time: 9.604624715982936\nSSL connection attempted (fuzzed)\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/896.py", line 142, in <module>\n    def multithreaded_function(data: typing.List[int], context: dbm.sqlite3.DB) -> int:\n                                                                ^^^^^^^^^^^^^^\nAttributeError: module \'dbm.sqlite3\' has no attribute \'DB\'\n'

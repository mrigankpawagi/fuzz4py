Return Code: 1
Stdout: b'Thread Thread-1 (worker): Result for arg1: 0, arg2: Thread input 0\nThread Thread-2 (worker): Result for arg1: 1, arg2: Thread input 1\nThread Thread-3 (worker): Result for arg1: 2, arg2: Thread input 2\nThread Thread-4 (worker): Result for arg1: 3, arg2: Thread input 3\nThread Thread-5 (worker): Result for arg1: 4, arg2: Thread input 4\nOriginal: 1, 2\nReplaced: 3, 2\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 78, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 74, in main\n    test_dbm()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 59, in test_dbm\n    db = dbm.sqlite3.open("mydatabase", \'c\')\n         ^^^^^^^^^^^\nAttributeError: module \'dbm\' has no attribute \'sqlite3\'\n'

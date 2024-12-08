Return Code: 1
Stdout: Thread Thread-1 (worker): Result for arg1: 0, arg2: Thread input 0
Thread Thread-2 (worker): Result for arg1: 1, arg2: Thread input 1
Thread Thread-3 (worker): Result for arg1: 2, arg2: Thread input 2
Thread Thread-4 (worker): Result for arg1: 3, arg2: Thread input 3
Thread Thread-5 (worker): Result for arg1: 4, arg2: Thread input 4
Original: 1, 2
Replaced: 3, 2

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 78, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 74, in main
    test_dbm()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/546.py", line 59, in test_dbm
    db = dbm.sqlite3.open("mydatabase", 'c')
         ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'


Return Code: 1
Stdout: Thread Thread-1 (worker) processed 0
Thread Thread-2 (worker) processed 1
Thread Thread-3 (worker) processed 2
Thread Thread-4 (worker) processed 3
Thread Thread-5 (worker) processed 4
OS times result: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612317.24)
Elapsed time: 0.000011 seconds
(1, 'hello')

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/630.py", line 85, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/630.py", line 80, in main
    if 'db' in locals() and isinstance(db, dbm.open):
                            ~~~~~~~~~~^^^^^^^^^^^^^^
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union


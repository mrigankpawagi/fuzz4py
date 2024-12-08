Return Code: 1
Stdout: Original object: 5, abc
Replaced object: 10, abc
OS times took: 0.0000 seconds

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/328.py", line 86, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/328.py", line 80, in main
    if 'db' in locals() and isinstance(db, dbm.dumb):
                            ~~~~~~~~~~^^^^^^^^^^^^^^
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union


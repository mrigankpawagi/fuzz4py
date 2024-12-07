Return Code: 1
Stdout: b'Original object: 5, abc\nReplaced object: 10, abc\nOS times took: 0.0000 seconds\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/329.py", line 87, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/329.py", line 81, in main\n    if \'db\' in locals() and isinstance(db, dbm.dumb):\n                            ~~~~~~~~~~^^^^^^^^^^^^^^\nTypeError: isinstance() arg 2 must be a type, a tuple of types, or a union\n'

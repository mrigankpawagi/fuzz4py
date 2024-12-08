Return Code: 1
Stdout: JIT result: 99990000
Thread result: 225
Copy replace result: Error in replace: replace() does not support type objects

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/620.py", line 105, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/620.py", line 91, in main
    dbm_result = test_dbm_sqlite(dbm_data, dbm_key)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/620.py", line 62, in test_dbm_sqlite
    if 'db' in locals() and isinstance(db, dbm.open):
                            ~~~~~~~~~~^^^^^^^^^^^^^^
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union


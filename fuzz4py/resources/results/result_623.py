Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/623.py", line 127, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/623.py", line 89, in main
    dbm_result = test_dbm_sqlite(dbm_data, dbm_key)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/623.py", line 67, in test_dbm_sqlite
    if 'db' in locals() and isinstance(db, dbm.open):
                            ~~~~~~~~~~^^^^^^^^^^^^^^
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union


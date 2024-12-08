Return Code: 1
Stdout: Error in jit_test_function: can't multiply sequence by non-int of type 'float'
Error in jit_test_function: can't multiply sequence by non-int of type 'float'
Error in jit_test_function: can't multiply sequence by non-int of type 'float'
Error in jit_test_function: can't multiply sequence by non-int of type 'float'
Error in jit_test_function: can't multiply sequence by non-int of type 'float'

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/656.py", line 55, in test_threading
    temp_dbm = dbm.sqlite3.open("test_dbm", 'c')
               ^^^^^^^^^^^
AttributeError: module 'dbm' has no attribute 'sqlite3'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/656.py", line 158, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/656.py", line 139, in main
    test_threading()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/656.py", line 58, in test_threading
    except (dbm.error, TypeError) as e:
        print(f"Error with dbm: {e}")
TypeError: catching classes that do not inherit from BaseException is not allowed


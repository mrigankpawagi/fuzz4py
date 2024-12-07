Return Code: 1
Stdout: b'100000\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/273.py", line 82, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/273.py", line 75, in main\n    print(test_jit_compiler())\n    ~~~~~^^^^^^^^^^^^^^^^^^^^^\nValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit\n'

Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 54, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 40, in main\n    results = complex_operation(data, True)\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 20, in complex_operation\n    data = data.replace(100, 200) #Test replace protocol\n           ^^^^^^^^^^^^\nAttributeError: \'list\' object has no attribute \'replace\'\n'

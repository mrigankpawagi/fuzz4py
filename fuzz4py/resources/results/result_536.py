Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/536.py", line 75, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/536.py", line 39, in main\n    new_data = copy.replace(data, new_value=point)\n  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace\n    raise TypeError(f"replace() does not support {cls.__name__} objects")\nTypeError: replace() does not support list objects\n'

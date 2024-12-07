Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/534.py", line 51, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/534.py", line 41, in main\n    new_obj = copy.replace(obj, a=42)\n  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace\n    raise TypeError(f"replace() does not support {cls.__name__} objects")\nTypeError: replace() does not support dict objects\n'

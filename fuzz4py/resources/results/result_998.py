Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/998.py", line 73, in <module>\n    result = main()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/998.py", line 35, in main\n    data_replace = copy.replace(data_copy)\n  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace\n    raise TypeError(f"replace() does not support {cls.__name__} objects")\nTypeError: replace() does not support list objects\n'

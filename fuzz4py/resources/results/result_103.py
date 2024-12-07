Return Code: 1
Stdout: b"0.0\nb'value'\nSSL context created successfully\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/103.py", line 106, in <module>\n    annotated_function("hello") # Example with string\n    ~~~~~~~~~~~~~~~~~~^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/103.py", line 56, in annotated_function\n    return arg + 5\n           ~~~~^~~\nTypeError: can only concatenate str (not "int") to str\n'

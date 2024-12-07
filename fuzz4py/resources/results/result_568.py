Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/568.py", line 57, in <module>\n    result = jit_sensitive_function(data_type)\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/568.py", line 17, in jit_sensitive_function\n    result += i  # Potential JIT hot loop\n    ^^^^^^^^^^^\nTypeError: unsupported operand type(s) for +=: \'int\' and \'str\'\n'

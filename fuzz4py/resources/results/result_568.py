Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/568.py", line 57, in <module>
    result = jit_sensitive_function(data_type)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/568.py", line 17, in jit_sensitive_function
    result += i  # Potential JIT hot loop
    ^^^^^^^^^^^
TypeError: unsupported operand type(s) for +=: 'int' and 'str'


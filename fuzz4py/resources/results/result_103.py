Return Code: 1
Stdout: 0.0
b'value'
SSL context created successfully

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/103.py", line 106, in <module>
    annotated_function("hello") # Example with string
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/103.py", line 56, in annotated_function
    return arg + 5
           ~~~~^~~
TypeError: can only concatenate str (not "int") to str


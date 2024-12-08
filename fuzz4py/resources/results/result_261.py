Return Code: 1
Stdout: Free-threading result: [-2, -5, 0, -10, 7, 0, -2, 3, -4, -10]

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 111, in <module>
    jit_result = test_jit_compiler()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 43, in test_jit_compiler
    raise ValueError("JIT error")
ValueError: JIT error


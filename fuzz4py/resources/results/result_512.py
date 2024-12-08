Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/512.py", line 45, in <module>
    def fuzz_copy_replace(obj: copy.MutableMapping, seed: int):
                               ^^^^^^^^^^^^^^^^^^^
AttributeError: module 'copy' has no attribute 'MutableMapping'


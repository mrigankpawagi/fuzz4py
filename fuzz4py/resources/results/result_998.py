Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/998.py", line 73, in <module>
    result = main()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/998.py", line 35, in main
    data_replace = copy.replace(data_copy)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support list objects


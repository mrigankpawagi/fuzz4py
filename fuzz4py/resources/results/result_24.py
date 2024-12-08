Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/24.py", line 61, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/24.py", line 43, in main
    new_object = copy.replace(my_object, a=4)  # Example of a replace call
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support dict objects


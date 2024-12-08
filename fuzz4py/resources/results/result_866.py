Return Code: 1
Stdout: Counter value: 5
SSL Error: Cannot set verify_mode to CERT_NONE when check_hostname is enabled.

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 127, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 100, in main
    replaced_obj = original_obj.__replace__(value="hello") # Testing with non-int
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/866.py", line 96, in __replace__
    return copy.replace(self, value=value)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
RecursionError: maximum recursion depth exceeded


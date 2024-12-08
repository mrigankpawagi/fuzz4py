Return Code: 1
Stdout: b'value1'
Final data: []

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 76, in <module>
    copy_replace_fuzz()
    ~~~~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 47, in copy_replace_fuzz
    p2 = p1.__replace__(x=30)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/365.py", line 42, in __replace__
    return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
RecursionError: maximum recursion depth exceeded


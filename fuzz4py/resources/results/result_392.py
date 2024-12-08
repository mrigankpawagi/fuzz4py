Return Code: 1
Stdout: 20

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/392.py", line 106, in <module>
    print(MyClass().method())
          ~~~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/392.py", line 85, in method
    return self.__static_attributes__['attr']
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
TypeError: tuple indices must be integers or slices, not str


Return Code: 1
Stdout: b'20\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/392.py", line 106, in <module>\n    print(MyClass().method())\n          ~~~~~~~~~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/392.py", line 85, in method\n    return self.__static_attributes__[\'attr\']\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^\nTypeError: tuple indices must be integers or slices, not str\n'

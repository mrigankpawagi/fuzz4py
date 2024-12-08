Return Code: 1
Stdout: Thread 129413788206656 : 42threading
Thread 129413777720896 : 42threading
Thread 129413767235136 : 42threading
Thread 129413756749376 : 42threading
Thread 129413670766144 : 42threading
JIT result: 999999000000

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/967.py", line 78, in <module>
    result_replace = test_replace_protocol()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/967.py", line 51, in test_replace_protocol
    obj2 = copy.replace(obj1, a=2)
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 306, in replace
    return func(obj, **changes)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/967.py", line 48, in __replace__
    return type(self)(**{k:v for k,v in self.__dict__.items() if k != 'b'})
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: test_replace_protocol.<locals>.MyClass.__init__() missing 1 required positional argument: 'b'


Return Code: 0
Stdout: 20
None
posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612321.32)
Error with os.times(random): posix.times() takes no arguments (1 given)
<ssl.SSLContext object at 0x7fc17bf271d0>
Error with SSL creation: cafile should be a valid filesystem path

Stderr: Exception in thread Thread-1 (<lambda>):
Exception in thread Thread-2 (<lambda>):
Exception in thread Thread-3 (<lambda>):
Exception in thread Thread-4 (<lambda>):
Exception in thread Thread-5 (<lambda>):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'


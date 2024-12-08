Return Code: 0
Stdout: 20
None
posix.times_result(user=0.04, system=0.01, children_user=0.0, children_system=0.0, elapsed=4606407.38)
Error with os.times(random): posix.times() takes no arguments (1 given)
<ssl.SSLContext object at 0x7816cbb1f1d0>
Error with SSL creation: [Errno 2] No such file or directory

Stderr: Exception in thread Thread-1 (<lambda>):
Exception in thread Thread-2 (<lambda>):
Exception in thread Thread-3 (<lambda>):
Exception in thread Thread-4 (<lambda>):
Exception in thread Thread-5 (<lambda>):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
Traceback (most recent call last):
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 45, in <lambda>
    t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
                                                     ~~~~~~~~~~~~~~~~~^^^
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/651.py", line 19, in jit_test_function
    result += input_list[i] * random.random()
              ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'


Return Code: 0
Stdout: threading with GIL
threading without GIL
Object after replacement: 42
posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604500.69)
Time taken for os.times(): 2.1859887056052685e-06
SSL context created.
{1: 1.0, 2: 2.0, 3: 3.0}
Thread 130352848832064 processed: 1, result: 6.0
Thread 130352959981120 processed: 1, result: 6.0
Thread 130352949495360 processed: 1, result: 6.0
Thread 130352939009600 processed: 1, result: 6.0
Thread 130352859317824 processed: 1, result: 6.0
Thread 130352848832064 processed: 2, result: 12.0
Thread 130352959981120 processed: 2, result: 12.0
Error in my_function: object of type 'NoneType' has no len(), arg1: 2, arg2: None
Thread 130352949495360 processed: 2, result: nan
Thread 130352939009600 processed: 2, result: 10.0
Error in my_function: object of type 'NoneType' has no len(), arg1: 2, arg2: None
Thread 130352859317824 processed: 2, result: nan
Thread 130352848832064 processed: 3, result: 18.0
Thread 130352959981120 processed: 3, result: 15.0
Error in my_function: object of type 'NoneType' has no len(), arg1: 3, arg2: None
Thread 130352949495360 processed: 3, result: nan
Thread 130352939009600 processed: 3, result: 15.0
Error in my_function: object of type 'NoneType' has no len(), arg1: 3, arg2: None
Thread 130352859317824 processed: 3, result: nan
Thread 130352848832064 processed: 4, result: 24.0
Thread 130352959981120 processed: 4, result: 20.0
Thread 130352949495360 processed: 4, result: 24.0
Thread 130352939009600 processed: 4, result: 24.0
Thread 130352859317824 processed: 4, result: 24.0
Thread 130352848832064 processed: 5, result: 30.0
Error in my_function: Forced error, arg1: 5, arg2: test55
Thread 130352959981120 processed: 5, result: nan
Error in my_function: Forced error, arg1: 5, arg2: test100
Thread 130352949495360 processed: 5, result: nan
Thread 130352939009600 processed: 5, result: 25.0
Thread 130352859317824 processed: 5, result: 30.0
docstring

Stderr: Exception in thread Thread-1 (complex_function):
Exception in thread Thread-2 (complex_function):
Exception in thread Thread-3 (complex_function):
Exception in thread Thread-4 (complex_function):
Exception in thread Thread-5 (complex_function):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
TypeError: '>' not supported between instances of 'list' and 'int'
Exception in thread Thread-6 (complex_function):
Exception in thread Thread-7 (complex_function):
Exception in thread Thread-8 (complex_function):
Traceback (most recent call last):
Traceback (most recent call last):
Exception in thread Thread-9 (complex_function):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
Exception in thread Thread-10 (complex_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'
TypeError: '>' not supported between instances of 'list' and 'int'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/33.py", line 97, in complex_function
    if i > 10:
       ^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int'


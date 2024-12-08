Return Code: 0
Stdout: os.times() took: 1.6840058378875256e-06
Copy replace result: [1, 2, 42, 4, 5]
Successfully created default context.

Stderr: Exception in thread Thread-1 (<lambda>):
Exception in thread Thread-2 (<lambda>):
Exception in thread Thread-3 (<lambda>):
Exception in thread Thread-4 (<lambda>):
Exception in thread Thread-5 (<lambda>):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
TypeError: object of type 'int' has no len()
TypeError: object of type 'int' has no len()
TypeError: object of type 'int' has no len()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x), args=())
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
TypeError: object of type 'int' has no len()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/408.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
TypeError: object of type 'int' has no len()


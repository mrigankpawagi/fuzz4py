Return Code: 0
Stdout: 
This is a docstring.

5
(10, 20)
os.times() took: 8.528993930667639e-06
Copy replace result: [1, 2, 42, 4, 5]
Successfully created default context.

Stderr: Exception in thread Thread-6 (<lambda>):
Exception in thread Thread-7 (<lambda>):
Exception in thread Thread-8 (<lambda>):
Exception in thread Thread-9 (<lambda>):
Exception in thread Thread-10 (<lambda>):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: object of type 'int' has no len()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 37, in <lambda>
    thread = threading.Thread(target=lambda x=data[i]: jit_sensitive_function(x))
                                                       ~~~~~~~~~~~~~~~~~~~~~~^^^
TypeError: object of type 'int' has no len()
TypeError: object of type 'int' has no len()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/414.py", line 28, in jit_sensitive_function
    for i in range(len(data)):
                   ~~~^^^^^^
TypeError: object of type 'int' has no len()
TypeError: object of type 'int' has no len()


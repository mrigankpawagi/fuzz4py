Return Code: 0
Stdout: 0
1.2428034096956253e-05

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 52, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 52, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 52, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 52, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 52, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
IndexError: list index out of range
IndexError: list index out of range
IndexError: list index out of range
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/802.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
IndexError: list index out of range
IndexError: list index out of range


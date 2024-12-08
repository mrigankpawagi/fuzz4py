Return Code: 0
Stdout: Caught exception in threaded_function: unsupported operand type(s) for +=: 'int' and 'list'
Could not convert arg to float: float() argument must be a string or a real number, not 'list'
Caught exception in threaded_function: unsupported operand type(s) for +=: 'int' and 'list'
Could not convert arg to float: float() argument must be a string or a real number, not 'list'
Caught exception in threaded_function: unsupported operand type(s) for +=: 'float' and 'list'
Caught exception in threaded_function: unsupported operand type(s) for +=: 'float' and 'list'
Could not convert arg to float: float() argument must be a string or a real number, not 'list'
Shared data after threads: 86.47314807527606
Error: x value not convertible to int
Exception caught in main: 
Time elapsed (monotonic): 0.38113369600614533
SSL connection successful

Stderr: Exception in thread Thread-4 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/838.py", line 33, in threaded_function
    raise ValueError("Simulated error in thread")
ValueError: Simulated error in thread


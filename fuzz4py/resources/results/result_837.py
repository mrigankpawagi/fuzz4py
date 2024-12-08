Return Code: 0
Stdout: Caught exception in threaded_function: unsupported operand type(s) for +=: 'int' and 'str'
Caught exception in threaded_function: unsupported operand type(s) for +=: 'int' and 'str'
Could not convert arg to float: could not convert string to float: 'str'
Shared data after threads: 34.436116122609405
Error: x value not convertible to int
Exception caught in main: 
Time elapsed (monotonic): 0.4278591279871762
SSL connection successful

Stderr: Exception in thread Thread-1 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/837.py", line 33, in threaded_function
    raise ValueError("Simulated error in thread")
ValueError: Simulated error in thread


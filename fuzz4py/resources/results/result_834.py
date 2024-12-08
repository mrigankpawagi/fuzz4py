Return Code: 0
Stdout: JIT result: 9999900000
Retrieved data1: b'some data', data2: b'more data'
Time taken by sched_yield: 0.000002 seconds
6
4
0
Shared data after threads: 23.0
Exception caught in main: 
Time elapsed (monotonic): 0.6867457350017503
SSL connection successful

Stderr: Exception in thread Thread-2 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/834.py", line 26, in threaded_function
    raise ValueError("Simulated error in thread")
ValueError: Simulated error in thread


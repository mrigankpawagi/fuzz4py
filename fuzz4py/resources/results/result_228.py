Return Code: 0
Stdout: Thread 137406707664448 results: [7, 8, 9]
Thread 137406686692928 results: [7, 8, 9]
posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4611003.82)
SSL context: <ssl.SSLContext object at 0x7cf87ebf2d50>

Stderr: Exception in thread Thread-1 (thread_function):
Exception in thread Thread-3 (thread_function):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 26, in thread_function
    results = complex_function(data, replace_flag)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 16, in complex_function
    data = copy.replace(data, new_val=[1,2])  # test copy.replace
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support list objects
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 26, in thread_function
    results = complex_function(data, replace_flag)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/228.py", line 16, in complex_function
    data = copy.replace(data, new_val=[1,2])  # test copy.replace
  File "/home/mrigankp/fuzz4py/cpython/Lib/copy.py", line 305, in replace
    raise TypeError(f"replace() does not support {cls.__name__} objects")
TypeError: replace() does not support list objects


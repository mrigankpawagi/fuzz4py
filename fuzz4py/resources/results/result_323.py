Return Code: 0
Stdout: Error in copy.replace(): replace() takes 1 positional argument but 2 were given
nested_comp: [36, 28, -96, -32, 54, -196, 10, 66, 48, 54, -192, 38, -70, 184, 100, -28, -36, 64, -32]
Retrieved data: b'62514'
Time difference: 1.9280609909910709 seconds.
Default SSL context created successfully.

Stderr: Exception in thread Thread-1 (complex_function2):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/323.py", line 56, in complex_function2
    print(f"Thread {threading.get_ident()} accessing data:", thread_local_data.value)
                                                             ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: '_thread._local' object has no attribute 'value'


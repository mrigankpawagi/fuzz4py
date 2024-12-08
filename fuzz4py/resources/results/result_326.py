Return Code: 0
Stdout: Error in copy.replace(): replace() takes 1 positional argument but 2 were given
nested_comp: [-64, -70, -108, -188, 26, 140, 108]
Retrieved data: b'93854'
Time difference: 1.6326376810320653 seconds.
Default SSL context created successfully.
Thread 136011132700224: (6, 'Hello6')
Thread 136011120117312: (6, 'Hello6')
Thread 136011109631552: (6, 'Hello6')
Thread 136011099145792: (6, 'Hello6')
Thread 136011088660032: (6, 'Hello6')
Successfully stored data with empty key.
os.times() result: posix.times_result(user=0.06, system=0.01, children_user=0.0, children_system=0.0, elapsed=4611111.19), duration: 1.3113021850585938e-05
SSL default context created successfully.

Stderr: Exception in thread Thread-1 (complex_function2):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/326.py", line 60, in complex_function2
    print(f"Thread {threading.get_ident()} accessing data:", thread_local_data.value)
                                                             ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: '_thread._local' object has no attribute 'value'


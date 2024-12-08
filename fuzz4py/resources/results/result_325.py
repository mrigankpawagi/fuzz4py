Return Code: 0
Stdout: Error in copy.replace(): replace() takes 1 positional argument but 2 were given
nested_comp: [148, 192, 156, 172, 156, 52, -200, -148, -62, 160, -82, -28, 26, -50, -156, -160]
Retrieved data: b'82129'
Time difference: 1.4250699740368873 seconds.
Default SSL context created successfully.
Thread 125511336461888: (6, 'Hello6')
Thread 125511323878976: (6, 'Hello6')
Thread 125511313393216: (6, 'Hello6')
Thread 125511302907456: (6, 'Hello6')
Thread 125511223215680: (6, 'Hello6')
Successfully stored data with empty key.
os.times() result: posix.times_result(user=0.05, system=0.01, children_user=0.0, children_system=0.0, elapsed=4611108.92), duration: 1.4543533325195312e-05
SSL default context created successfully.

Stderr: Exception in thread Thread-1 (complex_function2):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/325.py", line 56, in complex_function2
    print(f"Thread {threading.get_ident()} accessing data:", thread_local_data.value)
                                                             ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: '_thread._local' object has no attribute 'value'


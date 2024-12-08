Return Code: 0
Stdout: Error in copy.replace(): replace() takes 1 positional argument but 2 were given
nested_comp: [-148, -24, 100, 20, 38, 22, -42, 120, -24, -172, 38, 78, 80, -80]
Retrieved data: b'63645'
Time difference: 0.6314269099966623 seconds.
Default SSL context created successfully.
Thread 139242902652480: (6, 'Hello6')
Thread 139242890069568: (6, 'Hello6')
Thread 139242879583808: (6, 'Hello6')
Thread 139242869098048: (6, 'Hello6')
Thread 139242858612288: (6, 'Hello6')
Successfully stored data with empty key.
os.times() result: posix.times_result(user=0.05, system=0.0, children_user=0.0, children_system=0.0, elapsed=4605212.21), duration: 1.2159347534179688e-05
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


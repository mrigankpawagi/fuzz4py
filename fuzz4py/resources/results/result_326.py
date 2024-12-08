Return Code: 0
Stdout: Error in copy.replace(): replace() takes 1 positional argument but 2 were given
nested_comp: [-168, 90, 36, 20, 120, 80, -148, 28, -68, -78, 120, 98, 84, 56, -58, 4, -82]
Retrieved data: b'91874'
Time difference: 1.20550344302319 seconds.
Default SSL context created successfully.
Thread 128860163147328: (6, 'Hello6')
Thread 128860150564416: (6, 'Hello6')
Thread 128860140078656: (6, 'Hello6')
Thread 128860129592896: (6, 'Hello6')
Thread 128860119107136: (6, 'Hello6')
Successfully stored data with empty key.
os.times() result: posix.times_result(user=0.06, system=0.01, children_user=0.0, children_system=0.0, elapsed=4605214.17), duration: 1.52587890625e-05
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


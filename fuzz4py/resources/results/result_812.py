Return Code: 0
Stdout: Result of copy.replace() on list: Error: replace() does not support list objects
Result of copy.replace() on tuple: Error: replace() does not support tuple objects
Result of dbm fuzzing: Error: NOT NULL constraint failed: Dict.value
Result of SSL fuzzing: Error: [Errno 2] No such file or directory
posix.times_result(user=0.07, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606719.97)

Stderr: Exception in thread Thread-5 (my_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/812.py", line 16, in my_function
    total += i
TypeError: unsupported operand type(s) for +=: 'int' and 'str'


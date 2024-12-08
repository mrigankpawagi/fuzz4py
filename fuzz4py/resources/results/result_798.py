Return Code: 0
Stdout: Value of the shared variable: 0
Error in docstring exec: unexpected indent (<string>, line 2)
[{'a': 1, 'b': 'two'}]
start time: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606641.46)
end time: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606642.46)
Error in replace protocol fuzzing: replace() takes 1 positional argument but 2 were given
SSL error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'localhost'. (_ssl.c:1018)

Stderr: Exception in thread Thread-1 (thread_target):
Exception in thread Thread-2 (thread_target):
Exception in thread Thread-3 (thread_target):
Exception in thread Thread-4 (thread_target):
Exception in thread Thread-5 (thread_target):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/798.py", line 37, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/798.py", line 37, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/798.py", line 37, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/798.py", line 37, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/798.py", line 37, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
NameError: name 'thread_local_variable' is not defined


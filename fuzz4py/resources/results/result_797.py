Return Code: 1
Stdout: Value of the shared variable: 0

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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 31, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 31, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 31, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 31, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 31, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
NameError: name 'thread_local_variable' is not defined
NameError: name 'thread_local_variable' is not defined
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 79, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/797.py", line 64, in main
    replaced = copy.replace(MyReplaceable(10),100)
TypeError: replace() takes 1 positional argument but 2 were given


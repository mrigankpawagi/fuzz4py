Return Code: 1
Stdout: Value of the shared variable: 0
Error in docstring exec: unexpected indent (<string>, line 2)

Stderr: Exception in thread Thread-1 (thread_target):
Exception in thread Thread-2 (thread_target):
Exception in thread Thread-3 (thread_target):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/799.py", line 44, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/799.py", line 44, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
NameError: name 'thread_local_variable' is not defined
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/799.py", line 44, in thread_target
    thread_local_variable += 1
    ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'thread_local_variable' is not defined
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/799.py", line 137, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/799.py", line 82, in main
    inner_dict[f"key{key}"] = random.choice(data_types)(random.randint(0, 1000))
                              ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not iterable


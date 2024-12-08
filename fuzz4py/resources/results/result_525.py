Return Code: 0
Stdout: Shared data: 0
JIT Test result: 2500246980.671499, Time taken: 0.0077517032623291016s
An unexpected error occurred: main.<locals>.ReplaceableClass.__replace__() got an unexpected keyword argument 'value'

Stderr: Exception in thread Thread-1 (race_condition_example):
Exception in thread Thread-2 (race_condition_example):
Exception in thread Thread-3 (race_condition_example):
Exception in thread Thread-4 (race_condition_example):
Exception in thread Thread-5 (race_condition_example):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/525.py", line 29, in race_condition_example
    shared_data += data * random.randint(1, 10)  # Random multiplier
    ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/525.py", line 29, in race_condition_example
    shared_data += data * random.randint(1, 10)  # Random multiplier
    ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/525.py", line 29, in race_condition_example
    shared_data += data * random.randint(1, 10)  # Random multiplier
    ^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'shared_data' is not defined
NameError: name 'shared_data' is not defined
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/525.py", line 29, in race_condition_example
    shared_data += data * random.randint(1, 10)  # Random multiplier
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined
NameError: name 'shared_data' is not defined
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/525.py", line 29, in race_condition_example
    shared_data += data * random.randint(1, 10)  # Random multiplier
    ^^^^^^^^^^^
NameError: name 'shared_data' is not defined


Return Code: 1
Stdout: annotated_function result: HELLO
annotated_function result: 20
annotated_function result: 6
CPU times: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606450.39)
SSL connection established (successfully)

Stderr: Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/676.py", line 13, in worker
    return data.upper()
           ^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/676.py", line 13, in worker
    return data.upper()
           ^^^^^^^^^^
AttributeError: 'int' object has no attribute 'upper'
AttributeError: 'list' object has no attribute 'upper'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/676.py", line 101, in <module>
    replaced_data = copy.replace(example_data, "new value")
TypeError: replace() takes 1 positional argument but 2 were given


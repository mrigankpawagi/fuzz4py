Return Code: 1
Stdout: Free-threading result: [6, -2, -3, 8, 1, 1, -7, 1, 9, -10]

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-10 (worker):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 20, in worker
    raise RuntimeError("Simulated error in thread")
RuntimeError: Simulated error in thread
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 20, in worker
    raise RuntimeError("Simulated error in thread")
RuntimeError: Simulated error in thread
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 111, in <module>
    jit_result = test_jit_compiler()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/261.py", line 43, in test_jit_compiler
    raise ValueError("JIT error")
ValueError: JIT error


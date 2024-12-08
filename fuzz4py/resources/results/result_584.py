Return Code: 1
Stdout: 
Stderr: Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-4 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Exception in thread Thread-5 (threaded_function):
Exception in thread Thread-1 (threaded_function):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 23, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x75c1f6c835b0>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
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
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 23, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 23, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 23, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 23, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x75c1f6c835b0>
LookupError: <ContextVar name='execution_context' at 0x75c1f6c835b0>
LookupError: <ContextVar name='execution_context' at 0x75c1f6c835b0>
LookupError: <ContextVar name='execution_context' at 0x75c1f6c835b0>
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 118, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/584.py", line 43, in main
    with ctx.set("JIT_ON"):
         ~~~~~~~^^^^^^^^^^
TypeError: '_contextvars.Token' object does not support the context manager protocol


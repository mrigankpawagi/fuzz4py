Return Code: 1
Stdout: 
Stderr: Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-1 (threaded_function):
Exception in thread Thread-5 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-4 (threaded_function):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 37, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
LookupError: <ContextVar name='execution_context' at 0x76b9aab87740>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 37, in threaded_function
    current_context = ctx.get()
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 37, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
LookupError: <ContextVar name='execution_context' at 0x76b9aab87740>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
LookupError: <ContextVar name='execution_context' at 0x76b9aab87740>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 37, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 37, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x76b9aab87740>
LookupError: <ContextVar name='execution_context' at 0x76b9aab87740>
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 142, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/587.py", line 58, in main
    with ctx.set("JIT_ON"):
         ~~~~~~~^^^^^^^^^^
TypeError: '_contextvars.Token' object does not support the context manager protocol


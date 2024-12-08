Return Code: 1
Stdout: 
Stderr: Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Exception in thread Thread-8 (threaded_function):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Exception in thread Thread-4 (threaded_function):
Exception in thread Thread-6 (threaded_function):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
Traceback (most recent call last):
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
Exception in thread Thread-10 (threaded_function):
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
Exception in thread Thread-7 (threaded_function):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-1 (threaded_function):
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
Exception in thread Thread-9 (threaded_function):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
Exception in thread Thread-5 (threaded_function):
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 54, in threaded_function
    current_context = ctx.get()
LookupError: <ContextVar name='execution_context' at 0x79d90df87b50>
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 142, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/594.py", line 75, in main
    with ctx.set("JIT_ON"):
         ~~~~~~~^^^^^^^^^^
TypeError: '_contextvars.Token' object does not support the context manager protocol


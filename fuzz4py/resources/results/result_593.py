Return Code: 1
Stdout: b''
Stderr: b'Exception in thread Thread-3 (threaded_function):\nException in thread Thread-1 (threaded_function):\nException in thread Thread-7 (threaded_function):\nException in thread Thread-6 (threaded_function):\nException in thread Thread-9 (threaded_function):\nException in thread Thread-4 (threaded_function):\nException in thread Thread-5 (threaded_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\nException in thread Thread-10 (threaded_function):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nException in thread Thread-8 (threaded_function):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nException in thread Thread-2 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 54, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7e54a5d87b50>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 131, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/593.py", line 75, in main\n    with ctx.set("JIT_ON"):\n         ~~~~~~~^^^^^^^^^^\nTypeError: \'_contextvars.Token\' object does not support the context manager protocol\n'

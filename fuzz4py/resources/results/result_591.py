Return Code: 1
Stdout: b''
Stderr: b'Exception in thread Thread-1 (threaded_function):\nException in thread Thread-6 (threaded_function):\nException in thread Thread-9 (threaded_function):\nException in thread Thread-8 (threaded_function):\nException in thread Thread-2 (threaded_function):\nException in thread Thread-3 (threaded_function):\nException in thread Thread-7 (threaded_function):\nException in thread Thread-10 (threaded_function):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nException in thread Thread-4 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\nException in thread Thread-5 (threaded_function):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 43, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\nLookupError: <ContextVar name=\'execution_context\' at 0x79cb45d53650>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 88, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/591.py", line 63, in main\n    with ctx.set("JIT_ON"):\n         ~~~~~~~^^^^^^^^^^\nTypeError: \'_contextvars.Token\' object does not support the context manager protocol\n'

Return Code: 1
Stdout: b''
Stderr: b'Exception in thread Thread-1 (threaded_function):\nException in thread Thread-2 (threaded_function):\nException in thread Thread-3 (threaded_function):\nException in thread Thread-4 (threaded_function):\nException in thread Thread-5 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 17, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7b1b3da82ac0>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 17, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7b1b3da82ac0>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 17, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7b1b3da82ac0>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 17, in threaded_function\n    current_context = ctx.get()\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nLookupError: <ContextVar name=\'execution_context\' at 0x7b1b3da82ac0>\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 17, in threaded_function\n    current_context = ctx.get()\nLookupError: <ContextVar name=\'execution_context\' at 0x7b1b3da82ac0>\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 90, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/581.py", line 38, in main\n    with ctx.set("JIT_ON"):\n         ~~~~~~~^^^^^^^^^^\nTypeError: \'_contextvars.Token\' object does not support the context manager protocol\n'
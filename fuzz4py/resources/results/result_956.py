Return Code: 0
Stdout: b'Finished.\ndbm error: attempt to write a readonly database\n'
Stderr: b'Exception in thread Thread-2 (worker):\nException in thread Thread-4 (worker):\nException in thread Thread-6 (worker):\nException in thread Thread-8 (worker):\nException in thread Thread-10 (worker):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/956.py", line 12, in worker\n    data = data._replace(value=data.value + 1)\n           ^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/956.py", line 12, in worker\n    data = data._replace(value=data.value + 1)\n           ^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nAttributeError: \'Replaceable\' object has no attribute \'_replace\'. Did you mean: \'__replace__\'?\nAttributeError: \'Replaceable\' object has no attribute \'_replace\'. Did you mean: \'__replace__\'?\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/956.py", line 12, in worker\n    data = data._replace(value=data.value + 1)\n           ^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/956.py", line 12, in worker\n    data = data._replace(value=data.value + 1)\n           ^^^^^^^^^^^^^\nAttributeError: \'Replaceable\' object has no attribute \'_replace\'. Did you mean: \'__replace__\'?\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAttributeError: \'Replaceable\' object has no attribute \'_replace\'. Did you mean: \'__replace__\'?\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/956.py", line 12, in worker\n    data = data._replace(value=data.value + 1)\n           ^^^^^^^^^^^^^\nAttributeError: \'Replaceable\' object has no attribute \'_replace\'. Did you mean: \'__replace__\'?\n'

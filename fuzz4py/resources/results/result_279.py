Return Code: 0
Stdout: b'not a number\nAn error occurred: can only concatenate str (not "int") to str\n'
Stderr: b'Exception in thread Thread-9 (increment_counter):\nException in thread Thread-4 (increment_counter):\nException in thread Thread-6 (increment_counter):\nException in thread Thread-1 (increment_counter):\nException in thread Thread-3 (increment_counter):\nException in thread Thread-5 (increment_counter):\nException in thread Thread-8 (increment_counter):\nException in thread Thread-12 (increment_counter):\nException in thread Thread-10 (increment_counter):\nException in thread Thread-11 (increment_counter):\nException in thread Thread-13 (increment_counter):\nException in thread Thread-7 (increment_counter):\nException in thread Thread-2 (increment_counter):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\nTypeError: can only concatenate str (not "int") to str\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTypeError: can only concatenate str (not "int") to str\nTypeError: can only concatenate str (not "int") to str\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTypeError: can only concatenate str (not "int") to str\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/279.py", line 17, in increment_counter\n    shared_counter += 1\nTypeError: can only concatenate str (not "int") to str\n'
Return Code: 0
Stdout: b'Error from thread 1: division by zero\nError from thread 2: division by zero\nError from thread 2: division by zero\nError from thread 0: division by zero\nError from thread 1: division by zero\nAll threads finished.\nError writing to database: NOT NULL constraint failed: Dict.key\n'
Stderr: b'Exception in thread Thread-5 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/947.py", line 40, in worker\n    raise ValueError(f"Error from thread {thread_id}")\nValueError: Error from thread 4\nException in thread Thread-4 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/947.py", line 20, in worker\n    temp = i * 2\n           ~~^~~\nTypeError: unsupported operand type(s) for *: \'NoneType\' and \'int\'\nException in thread Thread-1 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nException in thread Thread-3 (worker):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/947.py", line 20, in worker\n    temp = i * 2\n           ~~^~~\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTypeError: unsupported operand type(s) for *: \'NoneType\' and \'int\'\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/947.py", line 20, in worker\n    temp = i * 2\n           ~~^~~\nTypeError: unsupported operand type(s) for *: \'NoneType\' and \'int\'\nException in thread Thread-2 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/947.py", line 40, in worker\n    raise ValueError(f"Error from thread {thread_id}")\nValueError: Error from thread 1\n'

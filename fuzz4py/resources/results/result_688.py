Return Code: 0
Stdout: b"copy.replace result: 12\ndbm.sqlite3 open error: module 'dbm' has no attribute 'sqlite3'\nFree Threading result: 51 global_var: 0\n"
Stderr: b'Exception in thread Thread-1 (worker):\nException in thread Thread-2 (worker):\nException in thread Thread-3 (worker):\nException in thread Thread-5 (worker):\nException in thread Thread-4 (worker):\nException in thread Thread-6 (worker):\nTraceback (most recent call last):\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\nNameError: name \'global_var\' is not defined\nNameError: name \'global_var\' is not defined\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/688.py", line 43, in worker\n    global_var += random.randint(1, 10)  # Random increment\n    ^^^^^^^^^^\nNameError: name \'global_var\' is not defined\nNameError: name \'global_var\' is not defined\nNameError: name \'global_var\' is not defined\nNameError: name \'global_var\' is not defined\n'

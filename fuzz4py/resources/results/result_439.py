Return Code: 0
Stdout: b"Final Counter: 45\n4999950000\nOriginal: 5, Copied: 10\n('Hello',)\n('Hello',)\n('Hello',)\n('Hello',)\nElapsed time: 1.0000698530348018\n['a', 'b']\nComplex function returned: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nValue: 10\nSSL context created successfully.\nTime taken: 9.5367431640625e-06\n"
Stderr: b'Exception in thread Thread-21 (worker):\nException in thread Thread-22 (worker):\nException in thread Thread-23 (worker):\nException in thread Thread-24 (worker):\nException in thread Thread-25 (worker):\nException in thread Thread-26 (worker):\nException in thread Thread-27 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nException in thread Thread-28 (worker):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nException in thread Thread-30 (worker):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nException in thread Thread-29 (worker):\nNameError: name \'shared_data\' is not defined\nNameError: name \'shared_data\' is not defined\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 178, in worker\n    shared_data[0] += 1\n    ^^^^^^^^^^^\nNameError: name \'shared_data\' is not defined\nNameError: name \'shared_data\' is not defined\nF\n======================================================================\nFAIL: test_thread_race (__main__.TestFreeThreading.test_thread_race)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/439.py", line 187, in test_thread_race\n    self.assertEqual(shared_data[0], 10)\n    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^\nAssertionError: 0 != 10\n\n----------------------------------------------------------------------\nRan 1 test in 0.009s\n\nFAILED (failures=1)\n'
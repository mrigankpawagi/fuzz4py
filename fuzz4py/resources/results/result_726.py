Return Code: 0
Stdout: b'Exception in lock block Thread-5 (threaded_function): \'NoneType\' object is not subscriptable\nException in lock block Thread-1 (threaded_function): \'NoneType\' object is not subscriptable\nFinal data: [0, 0, 1, None, 0, \'string\', \'string\', \'string\', 1, \'string\', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nModified data: [0, 0, 1, None, 0, \'string\', \'string\', \'string\', 1, \'string\', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4058649124845591271, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nDatabase key not found\nTime elapsed: 0.0\nSSL context created successfully\nDocstring with random characters: !@#$%^&*()_+=-{}[]|;:\'",.<>/?`~       \n\nAnnotation result: [79]\n'
Stderr: b'Exception in thread Thread-2 (threaded_function):\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner\n    self.run()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run\n    self._target(*self._args, **self._kwargs)\n    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/726.py", line 18, in threaded_function\n    raise ValueError("Simulated error in thread")\nValueError: Simulated error in thread\n'

Return Code: 0
Stdout: Thread Thread-1 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-2 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-3 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-4 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-5 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Key: b'key1', Value: b'value1'
OS Times: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606249.93)
b'value1'
2
Error: Certificate file not found: [Errno 2] No such file or directory: 'valid_cert.pem'
Thread Thread-11 (threaded_function): Result = 20000
Thread Thread-12 (threaded_function): Result = 120000
Thread Thread-13 (threaded_function): Result = 300000
Time taken by os.times(): 0.000003 seconds
Original object: 10, 20
Replaced object: 30, 20

Stderr: Exception in thread Thread-1 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-4 (threaded_function):
Exception in thread Thread-5 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 132, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 136, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135645676001088 and this is thread id 135645651535424.
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 132, in threaded_function
    result = my_function(input1, input2)
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 132, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 132, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 132, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~

During handling of the above exception, another exception occurred:

TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

During handling of the above exception, another exception occurred:


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 136, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 136, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 136, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135645676001088 and this is thread id 135645534094912.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 136, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135645676001088 and this is thread id 135645641049664.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135645676001088 and this is thread id 135645630563904.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 135645676001088 and this is thread id 135645620078144.
Exception in thread Thread-6 (<lambda>):
Exception in thread Thread-7 (<lambda>):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 65, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x, y), args=(i, safe_arg2))
                                             ~~~~~~~~~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-8 (<lambda>):
Exception in thread Thread-9 (<lambda>):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 65, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x, y), args=(i, safe_arg2))
                                             ~~~~~~~~~~~^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Exception in thread Thread-10 (<lambda>):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 65, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x, y), args=(i, safe_arg2))
                                             ~~~~~~~~~~~^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 65, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x, y), args=(i, safe_arg2))
                                             ~~~~~~~~~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 65, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x, y), args=(i, safe_arg2))
                                             ~~~~~~~~~~~^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/509.py", line 127, in my_function
    result += arg1 * arg2
TypeError: unsupported operand type(s) for +=: 'int' and 'str'


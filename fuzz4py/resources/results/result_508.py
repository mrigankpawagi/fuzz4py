Return Code: 0
Stdout: Thread Thread-1 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-2 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-3 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-4 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Thread Thread-5 (threaded_function): Error: unsupported operand type(s) for *: 'int' and '_thread.lock'
Key: b'key1', Value: b'value1'
OS Times: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612163.57)
b'value1'
2
Error: Certificate file not found: [Errno 2] No such file or directory: 'valid_cert.pem'
Thread Thread-11 (threaded_function): Result = 20000
Thread Thread-12 (threaded_function): Result = 120000
Thread Thread-13 (threaded_function): Result = 300000
Time taken by os.times(): 0.000002 seconds
Original object: 10, 20
Replaced object: 30, 20

Stderr: Exception in thread Thread-1 (threaded_function):
Exception in thread Thread-2 (threaded_function):
Exception in thread Thread-3 (threaded_function):
Exception in thread Thread-4 (threaded_function):
Exception in thread Thread-5 (threaded_function):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 160, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
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
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 164, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140448171652928 and this is thread id 140448148489792.
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 160, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 160, in threaded_function
    result = my_function(input1, input2)
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 160, in threaded_function
    result = my_function(input1, input2)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 160, in threaded_function
    result = my_function(input1, input2)
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~
TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
              ~~~~~^~~~~~

During handling of the above exception, another exception occurred:

TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'

During handling of the above exception, another exception occurred:

TypeError: unsupported operand type(s) for *: 'int' and '_thread.lock'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 164, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 164, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 164, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140448171652928 and this is thread id 140448045729344.
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 164, in threaded_function
    with lock:
         ^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 123, in __exit__
    self.close()
    ~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140448171652928 and this is thread id 140448127518272.
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140448171652928 and this is thread id 140448138004032.
  File "/home/mrigankp/fuzz4py/cpython/Lib/dbm/sqlite3.py", line 113, in close
    self._cx.close()
    ~~~~~~~~~~~~~~^^
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140448171652928 and this is thread id 140448035243584.
Exception in thread Thread-6 (<lambda>):
Exception in thread Thread-7 (<lambda>):
Exception in thread Thread-8 (<lambda>):
Exception in thread Thread-9 (<lambda>):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Exception in thread Thread-10 (<lambda>):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 82, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
                                             ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 82, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
                                             ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 82, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
                                             ~~~~~~~~~~~^^^^^
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 82, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
                                             ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 82, in <lambda>
    t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
                                             ~~~~~~~~~~~^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/508.py", line 155, in my_function
    result += arg1 * arg2
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
TypeError: unsupported operand type(s) for +=: 'int' and 'str'


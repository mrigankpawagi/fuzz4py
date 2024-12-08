Return Code: 0
Stdout: Result: 0
HTTP/1.1 200 OK
Accept-Ranges: bytes
Age: 216253
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Sun, 08 Dec 2024 06:46:32 GMT
Etag: "3147526947"
Expires: Sun, 15 Dec 2024 06:46:32 GMT
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
Server: ECAcc (lac/55C2)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 1256


Elapsed time (perf_counter): 0.000013 seconds
CPU times (os.times()): posix.times_result(user=0.07, system=0.01, children_user=0.0, children_system=0.0, elapsed=4606644.85)

Stderr: Exception in thread Thread-1 (worker):
Exception in thread Thread-2 (worker):
Exception in thread Thread-3 (worker):
Exception in thread Thread-4 (worker):
Exception in thread Thread-5 (worker):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 53, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 53, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 53, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 53, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 53, in worker
    result += my_function(data, iterations)
              ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
IndexError: list index out of range
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/803.py", line 16, in my_function
    result += data[i]
              ~~~~^^^
IndexError: list index out of range
IndexError: list index out of range
IndexError: list index out of range


Return Code: 0
Stdout: [10]
Value retrieved: b'value'
Operation took 1000153470 ns
b'HTTP/1.1 200 OK\r\nAccept-Ranges: bytes\r\nAge: 213835\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Sun, 08 Dec 2024 06:22:46 GMT\r\nEtag: "3147526947"\r\nExpires: Sun, 15 Dec 2024 06:22:46 GMT\r\nLast-Modified: Thu, 17 Oct 2019 07:18:26 GMT\r\nServer: ECAcc (lac/55F3)\r\nVary: Accept-Encoding\r\nX-Cache: HIT\r\nContent-Length: 1256\r\n\r\n'
[2, 4, 6]
Key: b'20', Value: b'1733638966.2129292'
Key: b'key', Value: b'value'

Stderr: Exception in thread Thread-9 (worker_part2):
Exception in thread Thread-6 (worker_part2):
Exception in thread Thread-7 (worker_part2):
Exception in thread Thread-10 (worker_part2):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/332.py", line 85, in worker_part2
    lock.release()
    ~~~~~~~~~~~~^^
RuntimeError: release unlocked lock
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
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/332.py", line 85, in worker_part2
    lock.release()
    ~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
RuntimeError: release unlocked lock
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/332.py", line 85, in worker_part2
    lock.release()
    ~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/332.py", line 85, in worker_part2
    lock.release()
    ~~~~~~~~~~~~^^
RuntimeError: release unlocked lock
RuntimeError: release unlocked lock
Exception in thread Thread-8 (worker_part2):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/332.py", line 85, in worker_part2
    lock.release()
    ~~~~~~~~~~~~^^
RuntimeError: release unlocked lock


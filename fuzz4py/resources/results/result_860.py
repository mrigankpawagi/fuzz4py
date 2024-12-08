Return Code: 1
Stdout: Error with dbm: db file doesn't exist; use 'c' or 'n' flag to create a new db
516856 something
516856 something
516856 something
OS times: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612663.37), Time taken: 1.9830185920000076e-06
1681856222731490

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/860.py", line 188, in <module>
    sock.connect(("invalid.example.com", 443))
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/ssl.py", line 1405, in connect
    self._real_connect(addr, False)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/ssl.py", line 1392, in _real_connect
    super().connect(addr)
    ~~~~~~~~~~~~~~~^^^^^^
socket.gaierror: [Errno -2] Name or service not known


Return Code: 1
Stdout: 316493 something
316493 something
316493 something
OS times: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4606746.7), Time taken: 2.401007805019617e-06
277794577960405

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


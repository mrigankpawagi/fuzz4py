Return Code: 1
Stdout: An error occurred: 'dict' object has no attribute 'replace'
None

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/664.py", line 79, in <module>
    socket.socket(), server_hostname='invalid_hostname.example.com'
    ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


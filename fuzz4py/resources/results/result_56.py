Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/56.py", line 51, in <module>
    socket.socket(), server_hostname='example.com'
    ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


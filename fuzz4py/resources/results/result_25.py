Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/25.py", line 73, in <module>
    with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
                             ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


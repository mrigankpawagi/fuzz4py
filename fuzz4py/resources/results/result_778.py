Return Code: 1
Stdout: 1733640381.2508743
[(1, 'malformed data')]
Value: 10
Value: 20

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/778.py", line 105, in <module>
    with context.wrap_socket(socket.socket(), server_hostname="example.com") as sock:
                             ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


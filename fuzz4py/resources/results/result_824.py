Return Code: 1
Stdout: Exception caught in main: 
Time elapsed (monotonic): 0.5001552400062792

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/824.py", line 74, in <module>
    with context.wrap_socket(socket.socket(), server_hostname='localhost'):
                             ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


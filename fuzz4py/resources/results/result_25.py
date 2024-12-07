Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/25.py", line 73, in <module>\n    with context.wrap_socket(socket.socket(), server_hostname=\'example.com\') as s:\n                             ^^^^^^\nNameError: name \'socket\' is not defined. Did you forget to import \'socket\'?\n'

Return Code: 1
Stdout: b"1733597031.1388571\n[(1, 'malformed data')]\nValue: 10\nValue: 20\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/778.py", line 105, in <module>\n    with context.wrap_socket(socket.socket(), server_hostname="example.com") as sock:\n                             ^^^^^^\nNameError: name \'socket\' is not defined. Did you forget to import \'socket\'?\n'

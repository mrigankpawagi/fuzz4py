Return Code: 1
Stdout: b'Exception caught in main: \nTime elapsed (monotonic): 0.5001534939510748\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/824.py", line 74, in <module>\n    with context.wrap_socket(socket.socket(), server_hostname=\'localhost\'):\n                             ^^^^^^\nNameError: name \'socket\' is not defined. Did you forget to import \'socket\'?\n'

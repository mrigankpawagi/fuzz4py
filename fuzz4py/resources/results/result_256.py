Return Code: 0
Stdout: b"Thread 131351751689792 result: 49995000\nThread 131351741204032 result: 49995000\nThread 131351730718272 result: 49995000\nThread 131351720232512 result: 49995000\nThread 131351640540736 result: 49995000\nRetrieved key: b'value1'\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 56, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 46, in main\n    with context.wrap_socket(socket.socket(), server_hostname=\'localhost\') as s:\n                             ^^^^^^\nNameError: name \'socket\' is not defined. Did you forget to import \'socket\'?\n'
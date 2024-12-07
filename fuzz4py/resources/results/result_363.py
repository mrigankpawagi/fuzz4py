Return Code: 1
Stdout: b'posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4562012.9)\n<ssl.SSLContext object at 0x7468688227b0>\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/363.py", line 103, in <module>\n    context.load_verify_locations(cafile=bad_cert)\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory\n'

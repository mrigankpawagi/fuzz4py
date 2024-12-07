Return Code: 1
Stdout: b"b'value1'\n2\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/501.py", line 80, in <module>\n    test_ssl()\n    ~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/501.py", line 63, in test_ssl\n    with open(\'valid_cert.pem\', \'rb\') as f:\n         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory: \'valid_cert.pem\'\n'

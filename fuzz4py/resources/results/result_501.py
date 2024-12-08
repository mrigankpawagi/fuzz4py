Return Code: 1
Stdout: b'value1'
2

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/501.py", line 80, in <module>
    test_ssl()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/501.py", line 63, in test_ssl
    with open('valid_cert.pem', 'rb') as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'valid_cert.pem'


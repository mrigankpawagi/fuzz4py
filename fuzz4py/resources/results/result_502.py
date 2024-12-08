Return Code: 1
Stdout: Error in thread: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132273073653568 and this is thread id 132273049437760.
Error in thread: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132273073653568 and this is thread id 132273038952000.
Error in thread: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132273073653568 and this is thread id 132273028466240.
Error in thread: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132273073653568 and this is thread id 132273017980480.
Error in thread: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 132273073653568 and this is thread id 132273007494720.
Key: b'key1', Value: b'value1'
b'value1'
2

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/502.py", line 130, in <module>
    test_ssl()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/502.py", line 114, in test_ssl
    with open('valid_cert.pem', 'rb') as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'valid_cert.pem'


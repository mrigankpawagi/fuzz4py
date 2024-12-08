Return Code: 1
Stdout: posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4605392.98)
<ssl.SSLContext object at 0x7ea2fe01e7b0>

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/364.py", line 114, in <module>
    context.load_verify_locations(cafile=bad_cert)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory


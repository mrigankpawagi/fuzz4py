Return Code: 1
Stdout: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4605392.87)
<ssl.SSLContext object at 0x7245130227b0>

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/362.py", line 103, in <module>
    context.load_verify_locations(cafile=bad_cert)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory


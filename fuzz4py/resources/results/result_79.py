Return Code: 0
Stdout: <Thread(Thread-1 (multithreaded_function), stopped 126364273346112)>
<Thread(Thread-2 (multithreaded_function), stopped 126364262860352)>
<Thread(Thread-3 (multithreaded_function), stopped 126364176877120)>
<Thread(Thread-4 (multithreaded_function), stopped 126364166391360)>
<Thread(Thread-5 (multithreaded_function), stopped 126364155905600)>
MyClass(a=-45, b=2)
OS times: posix.times_result(user=0.2, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610586.51)
Error: badcert.pem not found.  Please create a dummy certificate file.
Error loading bad certificate: [Errno 2] No such file or directory
SSL connection successfully initiated

Stderr: /home/mrigankp/fuzz4py/fuzz4py/inputs/79.py:103: DeprecationWarning: ssl.SSLContext() without protocol argument is deprecated.
  bad_cert = ssl.SSLContext()
/home/mrigankp/fuzz4py/fuzz4py/inputs/79.py:103: DeprecationWarning: ssl.PROTOCOL_TLS is deprecated
  bad_cert = ssl.SSLContext()


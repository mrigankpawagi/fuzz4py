Return Code: 0
Stdout: <Thread(Thread-1 (multithreaded_function), stopped 127619850831424)>
<Thread(Thread-2 (multithreaded_function), stopped 127619840345664)>
<Thread(Thread-3 (multithreaded_function), stopped 127619829859904)>
<Thread(Thread-4 (multithreaded_function), stopped 127619819374144)>
<Thread(Thread-5 (multithreaded_function), stopped 127619808888384)>
MyClass(a=789, b=2)
OS times: posix.times_result(user=0.57, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604620.74)
Error: badcert.pem not found.  Please create a dummy certificate file.
Error loading bad certificate: [Errno 2] No such file or directory
SSL connection successfully initiated

Stderr: /home/mrigankp/fuzz4py/fuzz4py/inputs/79.py:103: DeprecationWarning: ssl.SSLContext() without protocol argument is deprecated.
  bad_cert = ssl.SSLContext()
/home/mrigankp/fuzz4py/fuzz4py/inputs/79.py:103: DeprecationWarning: ssl.PROTOCOL_TLS is deprecated
  bad_cert = ssl.SSLContext()


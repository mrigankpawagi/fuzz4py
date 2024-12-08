Return Code: 0
Stdout: <Thread(Thread-1 (multithreaded_function), stopped 130047522375232)>
<Thread(Thread-2 (multithreaded_function), stopped 130047511889472)>
<Thread(Thread-3 (multithreaded_function), stopped 130047501403712)>
<Thread(Thread-4 (multithreaded_function), stopped 130047490917952)>
<Thread(Thread-5 (multithreaded_function), stopped 130047480432192)>
MyClass(a=519, b=2)
OS times: posix.times_result(user=0.31, system=0.0, children_user=0.0, children_system=0.0, elapsed=4604620.12)
Error with SSL: [Errno 2] No such file or directory

Stderr: /home/mrigankp/fuzz4py/fuzz4py/inputs/78.py:94: DeprecationWarning: ssl.SSLContext() without protocol argument is deprecated.
  bad_cert = ssl.SSLContext()
/home/mrigankp/fuzz4py/fuzz4py/inputs/78.py:94: DeprecationWarning: ssl.PROTOCOL_TLS is deprecated
  bad_cert = ssl.SSLContext()


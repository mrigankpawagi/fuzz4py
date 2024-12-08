Return Code: 0
Stdout: <Thread(Thread-1 (multithreaded_function), stopped 124991278417472)>
<Thread(Thread-2 (multithreaded_function), stopped 124991196628544)>
<Thread(Thread-3 (multithreaded_function), stopped 124991186142784)>
<Thread(Thread-4 (multithreaded_function), stopped 124991175657024)>
<Thread(Thread-5 (multithreaded_function), stopped 124991165171264)>
MyClass(a=-897, b=2)
OS times: posix.times_result(user=0.2, system=0.0, children_user=0.0, children_system=0.0, elapsed=4610586.25)
Error with SSL: [Errno 2] No such file or directory

Stderr: /home/mrigankp/fuzz4py/fuzz4py/inputs/78.py:94: DeprecationWarning: ssl.SSLContext() without protocol argument is deprecated.
  bad_cert = ssl.SSLContext()
/home/mrigankp/fuzz4py/fuzz4py/inputs/78.py:94: DeprecationWarning: ssl.PROTOCOL_TLS is deprecated
  bad_cert = ssl.SSLContext()


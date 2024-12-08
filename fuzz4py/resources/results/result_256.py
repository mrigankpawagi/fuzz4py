Return Code: 0
Stdout: Thread 135165814769216 result: 49995000
Thread 135165804283456 result: 49995000
Thread 135165793797696 result: 49995000
Thread 135165705717312 result: 49995000
Thread 135165695231552 result: 49995000
Retrieved key: b'value1'

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 56, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 46, in main
    with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
                             ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


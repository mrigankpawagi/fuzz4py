Return Code: 0
Stdout: Thread 134798077068864 result: 49995000
Thread 134798066583104 result: 49995000
Thread 134798056097344 result: 49995000
Thread 134798045611584 result: 49995000
Thread 134798035125824 result: 49995000
Retrieved key: b'value1'

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 56, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/256.py", line 46, in main
    with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
                             ^^^^^^
NameError: name 'socket' is not defined. Did you forget to import 'socket'?


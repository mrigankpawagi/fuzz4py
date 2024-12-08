Return Code: 1
Stdout: 27
27
posix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4612552.22)
Error with os.times(): [Errno 1] Operation not permitted

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/776.py", line 101, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/776.py", line 79, in main
    if protocol in context.get_protocols(): # Prevent crash if protocol is not available
                   ^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'SSLContext' object has no attribute 'get_protocols'. Did you mean: 'set_npn_protocols'?


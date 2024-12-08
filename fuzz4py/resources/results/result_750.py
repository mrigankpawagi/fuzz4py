Return Code: 1
Stdout: -493 c?
Elapsed time: 0.115312447946053
JIT function result: 475993390000000

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/750.py", line 102, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/750.py", line 92, in main
    context.load_verify_locations(cert)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
ValueError: embedded null byte


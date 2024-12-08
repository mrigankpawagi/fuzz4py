Return Code: 1
Stdout: 470 X
Elapsed time: 1.5531157169607468
JIT function result: 542993631000000

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/751.py", line 102, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/751.py", line 92, in main
    context.load_verify_locations(cert)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
ValueError: embedded null byte


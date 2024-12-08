Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/601.py", line 81, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/601.py", line 32, in main
    contexts.extend([ssl.SSLContext(random.choice([ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1_3,ssl.PROTOCOL_TLSv1_2])) for _ in range(3)]) #Fuzz more protocols
                                                                                                                 ^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'ssl' has no attribute 'PROTOCOL_TLSv1_3'. Did you mean: 'PROTOCOL_TLSv1_1'?


Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/601.py", line 81, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/601.py", line 32, in main\n    contexts.extend([ssl.SSLContext(random.choice([ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1_3,ssl.PROTOCOL_TLSv1_2])) for _ in range(3)]) #Fuzz more protocols\n                                                                                                                 ^^^^^^^^^^^^^^^^^^^^\nAttributeError: module \'ssl\' has no attribute \'PROTOCOL_TLSv1_3\'. Did you mean: \'PROTOCOL_TLSv1_1\'?\n'
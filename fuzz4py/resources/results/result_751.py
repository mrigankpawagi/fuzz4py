Return Code: 1
Stdout: b"855 :0\x7f'k\x157N;\x1c\x12\xd2\xa05$P\x7f\xd4\xb44(7\x1aVd\x14\xdb\xa9Tr|.\nElapsed time: 1.6647279750322923\nJIT function result: 324023880000000\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/751.py", line 102, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/751.py", line 92, in main\n    context.load_verify_locations(cert)\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^\nValueError: embedded null byte\n'

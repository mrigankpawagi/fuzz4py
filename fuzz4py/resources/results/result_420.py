Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/420.py", line 101, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/420.py", line 78, in main\n    fuzz_replace_protocol()\n    ~~~~~~~~~~~~~~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/420.py", line 35, in fuzz_replace_protocol\n    b = copy.replace(a, 2)\nTypeError: replace() takes 1 positional argument but 2 were given\n'

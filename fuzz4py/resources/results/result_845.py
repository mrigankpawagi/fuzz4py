Return Code: 1
Stdout: b"Results: ['00', '11', '22', '33', '44']\n"
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 61, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 56, in main\n    p2 = p2.__replace__(x=5)\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 51, in __replace__\n    return type(self)(**kwds)\n           ~~~~~~~~~~^^^^^^^^\nTypeError: main.<locals>.Point.__init__() missing 1 required positional argument: \'y\'\n'

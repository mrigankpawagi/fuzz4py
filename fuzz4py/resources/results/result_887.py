Return Code: 1
Stdout: b'Elapsed time: 2.1642015781253576e-05\nUser CPU time: 0.02\nError in __replace__: x must be an integer\nError during copy.replace: x must be an integer\nError during copy.replace: x must be an integer\n(1, 2)\n(3, 2)\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/887.py", line 140, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/887.py", line 118, in main\n    print(p5)\n          ^^\nUnboundLocalError: cannot access local variable \'p5\' where it is not associated with a value\n'

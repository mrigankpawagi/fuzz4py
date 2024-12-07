Return Code: 1
Stdout: b'Thread Thread-1 (worker): 1\nThread Thread-2 (worker): 2\nThread Thread-3 (worker): 3\nThread Thread-4 (worker): hello\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/208.py", line 83, in <module>\n    main()\n    ~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/208.py", line 44, in main\n    replaced_data = copy.replace(MyData(5), 10)\nTypeError: replace() takes 1 positional argument but 2 were given\n'

Return Code: 1
Stdout: Thread Thread-1 (worker): 1
Thread Thread-2 (worker): 2
Thread Thread-3 (worker): 3
Thread Thread-4 (worker): hello

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/208.py", line 83, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/208.py", line 44, in main
    replaced_data = copy.replace(MyData(5), 10)
TypeError: replace() takes 1 positional argument but 2 were given


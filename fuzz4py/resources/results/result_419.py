Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/419.py", line 95, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/419.py", line 75, in main
    fuzz_replace_protocol()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/419.py", line 35, in fuzz_replace_protocol
    b = copy.replace(a, 2)
TypeError: replace() takes 1 positional argument but 2 were given


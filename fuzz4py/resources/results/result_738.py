Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 54, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 40, in main
    results = complex_operation(data, True)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/738.py", line 20, in complex_operation
    data = data.replace(100, 200) #Test replace protocol
           ^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'replace'


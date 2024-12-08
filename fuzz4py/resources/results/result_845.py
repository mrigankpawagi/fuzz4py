Return Code: 1
Stdout: Results: ['00', '11', '22', '33', '44']

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 61, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 56, in main
    p2 = p2.__replace__(x=5)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/845.py", line 51, in __replace__
    return type(self)(**kwds)
           ~~~~~~~~~~^^^^^^^^
TypeError: main.<locals>.Point.__init__() missing 1 required positional argument: 'y'


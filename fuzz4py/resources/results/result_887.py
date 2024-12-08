Return Code: 1
Stdout: Elapsed time: 2.0574021618813276e-05
User CPU time: 0.02
Error in __replace__: x must be an integer
Error during copy.replace: x must be an integer
Error during copy.replace: x must be an integer
(1, 2)
(3, 2)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/887.py", line 140, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/887.py", line 118, in main
    print(p5)
          ^^
UnboundLocalError: cannot access local variable 'p5' where it is not associated with a value


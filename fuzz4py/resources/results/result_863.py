Return Code: 1
Stdout: Thread 130613552088640 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 130613562574400 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 130613541602880 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 130613531117120 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 130613443036736 failed: cannot access local variable 'global_var' where it is not associated with a value
Final value of global_var: 0

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/863.py", line 51, in <module>
    b = copy.replace(a, 2)
TypeError: replace() takes 1 positional argument but 2 were given


Return Code: 1
Stdout: Thread 137633239926336 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 137633229440576 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 137633197983296 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 137633218954816 failed: cannot access local variable 'global_var' where it is not associated with a value
Thread 137633208469056 failed: cannot access local variable 'global_var' where it is not associated with a value
Final value of global_var: 0

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/863.py", line 51, in <module>
    b = copy.replace(a, 2)
TypeError: replace() takes 1 positional argument but 2 were given


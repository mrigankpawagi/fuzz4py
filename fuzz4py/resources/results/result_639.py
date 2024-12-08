Return Code: 1
Stdout: 
Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/639.py", line 69, in <module>
    test_race_condition()
    ~~~~~~~~~~~~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/639.py", line 32, in test_race_condition
    results.append(threads[i].get_ident())
                   ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Thread' object has no attribute 'get_ident'


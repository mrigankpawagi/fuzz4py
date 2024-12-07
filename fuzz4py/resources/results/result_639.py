Return Code: 1
Stdout: b''
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/639.py", line 69, in <module>\n    test_race_condition()\n    ~~~~~~~~~~~~~~~~~~~^^\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/639.py", line 32, in test_race_condition\n    results.append(threads[i].get_ident())\n                   ^^^^^^^^^^^^^^^^^^^^\nAttributeError: \'Thread\' object has no attribute \'get_ident\'\n'

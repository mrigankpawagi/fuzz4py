Return Code: 0
Stdout: 
Stderr: E
======================================================================
ERROR: test_my_function (__main__.TestFuzzing.test_my_function)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/399.py", line 197, in test_my_function
    self.assertEqual(len(results), 3)
                     ~~~^^^^^^^^^
TypeError: object of type 'NoneType' has no len()

----------------------------------------------------------------------
Ran 1 test in 0.103s

FAILED (errors=1)


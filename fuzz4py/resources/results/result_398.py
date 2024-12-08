Return Code: 0
Stdout: Total execution time: 0.10051880101673305

Stderr: F
======================================================================
FAIL: test_my_function (__main__.TestFuzzing.test_my_function)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/398.py", line 182, in test_my_function
    self.assertEqual(result, input_data[i] * 2)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 2

----------------------------------------------------------------------
Ran 1 test in 0.103s

FAILED (failures=1)


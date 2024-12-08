Return Code: 0
Stdout: Error in MyClass.method(): tuple indices must be integers or slices, not str
Total execution time: 0.10044537100475281
OS times results: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4605769.12)
SSL connection successful

Stderr: FF.....
======================================================================
FAIL: test_my_class (__main__.TestFuzzing.test_my_class)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/396.py", line 180, in test_my_class
    self.assertEqual(MyClass().method(), 1)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 1

======================================================================
FAIL: test_my_function (__main__.TestFuzzing.test_my_function)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/396.py", line 187, in test_my_function
    self.assertEqual(result, input_data[i]*2)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 2

----------------------------------------------------------------------
Ran 7 tests in 0.905s

FAILED (failures=2)


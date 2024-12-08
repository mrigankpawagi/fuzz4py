Return Code: 0
Stdout: Error in MyClass.method(): tuple indices must be integers or slices, not str
OS times results: posix.times_result(user=0.03, system=0.0, children_user=0.0, children_system=0.0, elapsed=4611679.17)
SSL connection successful

Stderr: F.....
======================================================================
FAIL: test_my_class (__main__.TestFuzzing.test_my_class)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/393.py", line 148, in test_my_class
    self.assertEqual(MyClass().method(), 1)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 1

----------------------------------------------------------------------
Ran 6 tests in 0.779s

FAILED (failures=1)


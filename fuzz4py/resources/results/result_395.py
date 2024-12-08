Return Code: 0
Stdout: Error in MyClass.method(): tuple indices must be integers or slices, not str
Exception in thread: 'Thread' object has no attribute 'result'
Exception in thread: 'Thread' object has no attribute 'result'
Exception in thread: 'Thread' object has no attribute 'result'
Total execution time: 0.10045123100280762
OS times results: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4605768.16)
SSL connection successful

Stderr: FF.....
======================================================================
FAIL: test_my_class (__main__.TestFuzzing.test_my_class)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/395.py", line 170, in test_my_class
    self.assertEqual(MyClass().method(), 1)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 1

======================================================================
FAIL: test_my_function (__main__.TestFuzzing.test_my_function)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/395.py", line 175, in test_my_function
    self.assertEqual(len(results), len(input_data))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0 != 3

----------------------------------------------------------------------
Ran 7 tests in 0.897s

FAILED (failures=2)


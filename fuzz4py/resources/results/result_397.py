Return Code: 0
Stdout: b'Error in MyClass.method(): tuple indices must be integers or slices, not str\nTotal execution time: 0.10031004599295557\nOS times results: posix.times_result(user=0.02, system=0.0, children_user=0.0, children_system=0.0, elapsed=4562421.37)\nSSL connection successful\n'
Stderr: b'FF.....\n======================================================================\nFAIL: test_my_class (__main__.TestFuzzing.test_my_class)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/397.py", line 179, in test_my_class\n    self.assertEqual(MyClass().method(), 1)\n    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: None != 1\n\n======================================================================\nFAIL: test_my_function (__main__.TestFuzzing.test_my_function)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/397.py", line 186, in test_my_function\n    self.assertEqual(result, input_data[i]*2)\n    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: None != 2\n\n----------------------------------------------------------------------\nRan 7 tests in 0.886s\n\nFAILED (failures=2)\n'

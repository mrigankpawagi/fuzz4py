Return Code: 0
Stdout: b'Total execution time: 0.10010975797194988\n'
Stderr: b'F\n======================================================================\nFAIL: test_my_function (__main__.TestFuzzing.test_my_function)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/398.py", line 182, in test_my_function\n    self.assertEqual(result, input_data[i] * 2)\n    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: None != 2\n\n----------------------------------------------------------------------\nRan 1 test in 0.101s\n\nFAILED (failures=1)\n'
Return Code: 1
Stdout: b'Thread 135645693478464 processed: 1, result: 6.0\nThread 135645682992704 processed: 1, result: 6.0\nThread 135645601203776 processed: 1, result: 6.0\nThread 135645590718016 processed: 1, result: 6.0\nThread 135645580232256 processed: 1, result: 6.0\nThread 135645693478464 processed: 2, result: 10.0\nThread 135645682992704 processed: 2, result: 12.0\nThread 135645601203776 processed: 2, result: 12.0\nThread 135645590718016 processed: 2, result: 12.0\nThread 135645580232256 processed: 2, result: 12.0\nThread 135645693478464 processed: 3, result: 18.0\nThread 135645682992704 processed: 3, result: 18.0\nThread 135645601203776 processed: 3, result: 18.0\nThread 135645590718016 processed: 3, result: 18.0\nThread 135645580232256 processed: 3, result: 18.0\nThread 135645693478464 processed: 4, result: 24.0\nThread 135645682992704 processed: 4, result: 24.0\nThread 135645601203776 processed: 4, result: 24.0\nThread 135645590718016 processed: 4, result: 24.0\nThread 135645580232256 processed: 4, result: 24.0\nThread 135645693478464 processed: 5, result: 30.0\nThread 135645682992704 processed: 5, result: 30.0\nThread 135645601203776 processed: 5, result: 30.0\nThread 135645590718016 processed: 5, result: 30.0\nThread 135645580232256 processed: 5, result: 30.0\ndocstring\n'
Stderr: b'Traceback (most recent call last):\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 87, in <module>\n    result_annotation = complex_annotation(data_for_annotation)\n  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 69, in complex_annotation\n    if item is not None and isinstance(item, tuple) and item[0] > 0:\n                                                        ^^^^^^^^^^^\nTypeError: \'>\' not supported between instances of \'NoneType\' and \'int\'\n'
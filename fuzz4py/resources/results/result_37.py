Return Code: 0
Stdout: b"threading with GIL\nthreading without GIL\nObject after replacement: 42\nposix.times_result(user=0.01, system=0.0, children_user=0.0, children_system=0.0, elapsed=4561194.84)\nTime taken for os.times(): 2.4750479497015476e-06\nSSL context created.\n{1: 1.0, 2: 2.0, 3: 3.0, 10: 10.0}\nThread 133924602775104 processed: 1, result: 6.0\nThread 133924592289344 processed: 1, result: 0.0\nThread 133924581803584 processed: 1, result: 6.0\nThread 133924571317824 processed: 1, result: 5.0\nThread 133924560832064 processed: 1, result: 5.0\nThread 133924550346304 processed: 1, result: 1.0\nThread 133924539860544 processed: 1, result: 6.0\nThread 133924460168768 processed: 1, result: 6.0\nThread 133924602775104 processed: 2, result: 12.0\nThread 133924592289344 processed: 2, result: 0.0\nThread 133924581803584 processed: 2, result: 12.0\nThread 133924571317824 processed: 2, result: 12.0\nThread 133924560832064 processed: 2, result: 12.0\nThread 133924550346304 processed: 2, result: 12.0\nThread 133924539860544 processed: 2, result: 12.0\nThread 133924460168768 processed: 2, result: 12.0\nError in my_function: Forced error, arg1: 3, arg2: test15\nThread 133924602775104 processed: 3, result: nan\nThread 133924592289344 processed: 3, result: 18.0\nThread 133924581803584 processed: 3, result: 18.0\nThread 133924571317824 processed: 3, result: 0.0\nThread 133924560832064 processed: 3, result: 18.0\nThread 133924550346304 processed: 3, result: 3.0\nError in my_function: Forced error, arg1: 3, arg2: test27\nThread 133924539860544 processed: 3, result: nan\nThread 133924460168768 processed: 3, result: 18.0\nThread 133924602775104 processed: 4, result: 24.0\nThread 133924592289344 processed: 4, result: 0.0\nThread 133924581803584 processed: 4, result: 0.0\nThread 133924571317824 processed: 4, result: 0.0\nThread 133924560832064 processed: 4, result: 24.0\nThread 133924550346304 processed: 4, result: 24.0\nThread 133924539860544 processed: 4, result: 24.0\nThread 133924460168768 processed: 4, result: 24.0\nThread 133924602775104 processed: 5, result: 0.0\nError in my_function: Forced error, arg1: 5, arg2: test100\nThread 133924592289344 processed: 5, result: nan\nThread 133924581803584 processed: 5, result: 30.0\nThread 133924571317824 processed: 5, result: 30.0\nThread 133924560832064 processed: 5, result: 0.0\nThread 133924550346304 processed: 5, result: 30.0\nThread 133924539860544 processed: 5, result: 25.0\nThread 133924460168768 processed: 5, result: 30.0\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: test49\nThread 133924602775104 processed: a, result: nan\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: 123\nThread 133924592289344 processed: a, result: nan\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: test56\nThread 133924581803584 processed: a, result: nan\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: None\nThread 133924571317824 processed: a, result: nan\nError in my_function: Forced error, arg1: a, arg2: test87\nThread 133924560832064 processed: a, result: nan\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: None\nThread 133924550346304 processed: a, result: nan\nError in my_function: could not convert string to float: 'a', arg1: a, arg2: test87\nThread 133924539860544 processed: a, result: nan\nError in my_function: Forced error, arg1: a, arg2: test94\nThread 133924460168768 processed: a, result: nan\nThread 133924602775104 processed: 0, result: 0.0\nThread 133924592289344 processed: 0, result: 0.0\nThread 133924581803584 processed: 0, result: 0.0\nThread 133924571317824 processed: 0, result: 0.0\nThread 133924560832064 processed: 0, result: 0.0\nThread 133924550346304 processed: 0, result: 0.0\nError in my_function: Forced error, arg1: 0, arg2: 123\nThread 133924539860544 processed: 0, result: nan\nThread 133924460168768 processed: 0, result: 0.0\nThread 133924602775104 processed: -1, result: -6.0\nThread 133924592289344 processed: -1, result: -6.0\nThread 133924581803584 processed: -1, result: -6.0\nThread 133924571317824 processed: -1, result: -1.0\nError in my_function: Forced error, arg1: -1, arg2: None\nThread 133924560832064 processed: -1, result: nan\nThread 133924550346304 processed: -1, result: -6.0\nThread 133924539860544 processed: -1, result: -6.0\nThread 133924460168768 processed: -1, result: -6.0\ndocstring\nAnd a second line\n"
Stderr: b''

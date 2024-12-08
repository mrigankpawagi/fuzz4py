Return Code: 0
Stdout: Running with data: [1, 2, 3]
Thread Thread-2 (thread_function): [2, 4, 6]
Thread Thread-3 (thread_function): [2, 4, 6]
Thread Thread-4 (thread_function): [2, 4, 6]
Thread Thread-1 (thread_function): [2, 4, 6]
All threads finished for current data set

Running with data: [1, 2, 'a']
Thread Thread-8 (thread_function): [2, 4, 'aa']
Thread Thread-7 (thread_function): [2, 4, 'aa']
Thread Thread-6 (thread_function): [2, 4, 'aa']
Thread Thread-5 (thread_function): [2, 4, 'aa']
All threads finished for current data set

Running with data: [1, 2, 3, 10000000000]
Thread Thread-10 (thread_function): [2, 4, 6, 20000000000]
Thread Thread-11 (thread_function): [2, 4, 6, 20000000000]
Thread Thread-9 (thread_function): [2, 4, 6, 20000000000]
All threads finished for current data set

Running with data: []
Thread Thread-14 (thread_function): Data processing failed.
Thread Thread-13 (thread_function): Data processing failed.
Thread Thread-12 (thread_function): Data processing failed.
All threads finished for current data set

Running with data: [None]
Error in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None
Thread Thread-16 (thread_function): [None]
Error in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None
Thread Thread-15 (thread_function): [None]
Error in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None
Thread Thread-17 (thread_function): [None]
All threads finished for current data set

Running with data: [True, False]
Thread Thread-18 (thread_function): [2, 0]
Thread Thread-20 (thread_function): [2, 0]
Thread Thread-21 (thread_function): [2, 0]
Thread Thread-19 (thread_function): [2, 0]
All threads finished for current data set


Stderr: 

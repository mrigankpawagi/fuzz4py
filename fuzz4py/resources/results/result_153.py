Return Code: 0
Stdout: b"Running with data: [1, 2, 3]\nThread Thread-2 (thread_function): [2, 4, 6]\nThread Thread-1 (thread_function): [2, 4, 6]\nThread Thread-3 (thread_function): [2, 4, 6]\nThread Thread-4 (thread_function): [2, 4, 6]\nAll threads finished for current data set\n\nRunning with data: [1, 2, 'a']\nThread Thread-5 (thread_function): [2, 4, 'aa']\nThread Thread-7 (thread_function): [2, 4, 'aa']\nThread Thread-6 (thread_function): [2, 4, 'aa']\nAll threads finished for current data set\n\nRunning with data: [1, 2, 3, 10000000000]\nThread Thread-9 (thread_function): [2, 4, 6, 20000000000]\nThread Thread-8 (thread_function): [2, 4, 6, 20000000000]\nThread Thread-10 (thread_function): [2, 4, 6, 20000000000]\nAll threads finished for current data set\n\nRunning with data: []\nThread Thread-12 (thread_function): Data processing failed.\nThread Thread-11 (thread_function): Data processing failed.\nThread Thread-15 (thread_function): Data processing failed.\nThread Thread-13 (thread_function): Data processing failed.\nThread Thread-14 (thread_function): Data processing failed.\nAll threads finished for current data set\n\nRunning with data: [None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None\nThread Thread-20 (thread_function): [None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None\nThread Thread-16 (thread_function): [None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None\nThread Thread-19 (thread_function): [None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None\nThread Thread-17 (thread_function): [None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None], i: None\nThread Thread-18 (thread_function): [None]\nAll threads finished for current data set\n\nRunning with data: [True, False]\nThread Thread-23 (thread_function): [2, 0]\nThread Thread-21 (thread_function): [2, 0]\nThread Thread-22 (thread_function): [2, 0]\nThread Thread-25 (thread_function): [2, 0]\nThread Thread-24 (thread_function): [2, 0]\nAll threads finished for current data set\n\nRunning with data: [1.5, 2.7, 3.14]\nThread Thread-26 (thread_function): [3.0, 5.4, 6.28]\nThread Thread-27 (thread_function): [3.0, 5.4, 6.28]\nAll threads finished for current data set\n\nRunning with data: [-1, -2, -3]\nThread Thread-28 (thread_function): [-2, -4, -6]\nThread Thread-29 (thread_function): [-2, -4, -6]\nAll threads finished for current data set\n\nRunning with data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nThread Thread-30 (thread_function): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nThread Thread-33 (thread_function): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nThread Thread-34 (thread_function): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nThread Thread-31 (thread_function): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nThread Thread-32 (thread_function): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nAll threads finished for current data set\n\nRunning with data: [-100, 87, -81, -93, -3, 68, 26, 58, 38, -14, 8, 48, 76, -79, 34, -14, 96, -68, 44, -77]\nThread Thread-37 (thread_function): [-200, 174, -162, -186, -6, 136, 52, 116, 76, -28, 16, 96, 152, -158, 68, -28, 192, -136, 88, -154]\nThread Thread-35 (thread_function): [-200, 174, -162, -186, -6, 136, 52, 116, 76, -28, 16, 96, 152, -158, 68, -28, 192, -136, 88, -154]\nThread Thread-36 (thread_function): [-200, 174, -162, -186, -6, 136, 52, 116, 76, -28, 16, 96, 152, -158, 68, -28, 192, -136, 88, -154]\nAll threads finished for current data set\n\nRunning with data: [0.5342616267076922, 0.9150663903319949, 0.24951535191632768, 0.46914403101310453, 0.011259288150916369, 0.8008706810770981, 0.26850209187526086, 0.6541107372719279, 0.7270142478774076, 0.1533590941361409]\nThread Thread-40 (thread_function): [1.0685232534153843, 1.8301327806639898, 0.49903070383265535, 0.9382880620262091, 0.022518576301832738, 1.6017413621541963, 0.5370041837505217, 1.3082214745438558, 1.4540284957548153, 0.3067181882722818]\nThread Thread-38 (thread_function): [1.0685232534153843, 1.8301327806639898, 0.49903070383265535, 0.9382880620262091, 0.022518576301832738, 1.6017413621541963, 0.5370041837505217, 1.3082214745438558, 1.4540284957548153, 0.3067181882722818]\nThread Thread-39 (thread_function): [1.0685232534153843, 1.8301327806639898, 0.49903070383265535, 0.9382880620262091, 0.022518576301832738, 1.6017413621541963, 0.5370041837505217, 1.3082214745438558, 1.4540284957548153, 0.3067181882722818]\nAll threads finished for current data set\n\nRunning with data: [None, 1, 2, None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nThread Thread-41 (thread_function): [None, 2, 4, None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nThread Thread-42 (thread_function): [None, 2, 4, None]\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nError in complex_function: unsupported operand type(s) for *: 'NoneType' and 'int', data: [None, 1, 2, None], i: None\nThread Thread-43 (thread_function): [None, 2, 4, None]\nAll threads finished for current data set\n\nRunning with data: []\nThread Thread-44 (thread_function): Data processing failed.\nThread Thread-45 (thread_function): Data processing failed.\nAll threads finished for current data set\n\nRunning with data: [1, 2, 3, 10000000000, 1.1]\nThread Thread-46 (thread_function): [2, 4, 6, 20000000000, 2.2]\nThread Thread-47 (thread_function): [2, 4, 6, 20000000000, 2.2]\nAll threads finished for current data set\n\nRunning with data: [b'abc', 1, 2]\nThread Thread-48 (thread_function): [b'abcabc', 2, 4]\nThread Thread-49 (thread_function): [b'abcabc', 2, 4]\nThread Thread-50 (thread_function): [b'abcabc', 2, 4]\nAll threads finished for current data set\n\n"
Stderr: b''

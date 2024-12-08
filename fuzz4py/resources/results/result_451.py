Return Code: 1
Stdout: Worker 7 raised exception: Intentional TypeError
Worker 0 raised exception: Intentional Error
Worker 5 raised exception: Intentional Error
Worker 3 raised exception: Simulated exception
Final Counter: 45
4999950000
Original: 5, Copied: 10, Copied y: changed
Error in dbm.sqlite3 test: table mytable has no column named another_data
Elapsed time: 1.0768 seconds
['a', 'b']

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/451.py", line 151, in <module>
    processed_data = my_complex_function(data)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/451.py", line 130, in my_complex_function
    return [x * 2 for x in data]
            ~~^~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


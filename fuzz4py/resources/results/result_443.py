Return Code: 1
Stdout: Worker 7 raised exception: Simulated exception
Worker 0 raised exception: Simulated exception
Final Counter: 45
4249615241
Original: 5, Copied: 10, Copied y: changed
Error in dbm.sqlite3 test: table mytable has no column named another_data
Elapsed time: 1.2257 seconds
['a', 'b']

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/443.py", line 150, in <module>
    processed_data = my_complex_function(data)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/443.py", line 128, in my_complex_function
    return [x * 2 for x in data]
            ~~^~~
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


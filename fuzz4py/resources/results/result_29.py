Return Code: 1
Stdout: Thread 127070128571968 processed: 1, result: 6.0
Thread 127070118086208 processed: 1, result: 6.0
Thread 127070107600448 processed: 1, result: 6.0
Thread 127070027908672 processed: 1, result: 6.0
Thread 127070017422912 processed: 1, result: 6.0
Thread 127070128571968 processed: 2, result: 12.0
Thread 127070118086208 processed: 2, result: 12.0
Thread 127070107600448 processed: 2, result: 10.0
Thread 127070027908672 processed: 2, result: 12.0
Thread 127070017422912 processed: 2, result: 12.0
Thread 127070128571968 processed: 3, result: 18.0
Thread 127070118086208 processed: 3, result: 18.0
Thread 127070107600448 processed: 3, result: 18.0
Thread 127070027908672 processed: 3, result: 18.0
Thread 127070017422912 processed: 3, result: 18.0
Thread 127070128571968 processed: 4, result: 24.0
Thread 127070118086208 processed: 4, result: 24.0
Thread 127070107600448 processed: 4, result: 24.0
Thread 127070027908672 processed: 4, result: 24.0
Thread 127070017422912 processed: 4, result: 24.0
Thread 127070128571968 processed: 5, result: 30.0
Thread 127070118086208 processed: 5, result: 30.0
Thread 127070107600448 processed: 5, result: 30.0
Thread 127070027908672 processed: 5, result: 30.0
Thread 127070017422912 processed: 5, result: 30.0
docstring

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 87, in <module>
    result_annotation = complex_annotation(data_for_annotation)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 69, in complex_annotation
    if item is not None and isinstance(item, tuple) and item[0] > 0:
                                                        ^^^^^^^^^^^
TypeError: '>' not supported between instances of 'NoneType' and 'int'


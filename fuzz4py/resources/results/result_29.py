Return Code: 1
Stdout: Thread 135331632383552 processed: 1, result: 6.0
Thread 135331621897792 processed: 1, result: 6.0
Thread 135331611412032 processed: 1, result: 6.0
Thread 135331531720256 processed: 1, result: 6.0
Thread 135331521234496 processed: 1, result: 6.0
Thread 135331632383552 processed: 2, result: 10.0
Thread 135331621897792 processed: 2, result: 12.0
Thread 135331611412032 processed: 2, result: 10.0
Thread 135331531720256 processed: 2, result: 12.0
Thread 135331521234496 processed: 2, result: 12.0
Thread 135331632383552 processed: 3, result: 18.0
Thread 135331621897792 processed: 3, result: 18.0
Thread 135331611412032 processed: 3, result: 18.0
Thread 135331531720256 processed: 3, result: 18.0
Thread 135331521234496 processed: 3, result: 18.0
Thread 135331632383552 processed: 4, result: 24.0
Thread 135331621897792 processed: 4, result: 24.0
Thread 135331611412032 processed: 4, result: 24.0
Thread 135331531720256 processed: 4, result: 24.0
Thread 135331521234496 processed: 4, result: 24.0
Thread 135331632383552 processed: 5, result: 25.0
Thread 135331621897792 processed: 5, result: 30.0
Thread 135331611412032 processed: 5, result: 30.0
Thread 135331531720256 processed: 5, result: 30.0
Thread 135331521234496 processed: 5, result: 30.0
docstring

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 87, in <module>
    result_annotation = complex_annotation(data_for_annotation)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/29.py", line 69, in complex_annotation
    if item is not None and isinstance(item, tuple) and item[0] > 0:
                                                        ^^^^^^^^^^^
TypeError: '>' not supported between instances of 'NoneType' and 'int'


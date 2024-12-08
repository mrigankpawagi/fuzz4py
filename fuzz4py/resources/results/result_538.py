Return Code: 1
Stdout: SSL connection established (or should have been)

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/538.py", line 114, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/538.py", line 87, in main
    Point = namedtuple("Point", [("x", int), ("y", int)])
  File "/home/mrigankp/fuzz4py/cpython/Lib/collections/__init__.py", line 403, in namedtuple
    raise ValueError('Type names and field names must be valid '
                     f'identifiers: {name!r}')
ValueError: Type names and field names must be valid identifiers: "('x', <class 'int'>)"


Return Code: 1
Stdout: Result for input [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: 45, time taken: 0.015671253204345703

Stderr: Exception in thread Thread-1 (<lambda>):
Exception in thread Thread-2 (<lambda>):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 25, in my_function
    result += item
TypeError: unsupported operand type(s) for +=: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 51, in <module>
    main()
    ~~~~^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 39, in main
    result = my_function(data)
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 28, in my_function
    except (TypeError, ValueError, dbm.error) as e:
        print(f"An error occurred: {e}")
        return -1
TypeError: catching classes that do not inherit from BaseException is not allowed
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/cpython/Lib/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 19, in <lambda>
    t = threading.Thread(target=lambda: db.set('key', str(random.randint(1,10000))))
                                        ^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/980.py", line 19, in <lambda>
    t = threading.Thread(target=lambda: db.set('key', str(random.randint(1,10000))))
                                        ^^^^^^
AttributeError: '_Database' object has no attribute 'set'. Did you mean: 'get'?
AttributeError: '_Database' object has no attribute 'set'. Did you mean: 'get'?


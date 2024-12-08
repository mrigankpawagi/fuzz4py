Return Code: 1
Stdout: Error in test_free_threading: Incorrect result for arg1

Stderr: Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/55.py", line 97, in <module>
    test_free_threading(0, "abc")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/55.py", line 47, in test_free_threading
    t2 = threading.Thread(target=worker, args=(int(arg2),))
                                               ~~~^^^^^^
ValueError: invalid literal for int() with base 10: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/mrigankp/fuzz4py/fuzz4py/inputs/55.py", line 143, in <module>
    except (dbm.error, ssl.SSLError, OSError, ValueError, TypeError, Exception) as e:
      print(f"An error occurred: {type(e).__name__} - {e}")
TypeError: catching classes that do not inherit from BaseException is not allowed


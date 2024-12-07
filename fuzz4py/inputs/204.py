
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import sys
import socket

# Fuzzing for free-threading and GIL
def thread_func(lock, data, fuzz_val):
    with lock:
        try:
            data.append(time.time() + fuzz_val)
        except (TypeError, ValueError) as e:
            print(f"Thread error: Invalid data type or value: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890, b"bytes", [], (), {"key": "value"}, True, False, complex(1,2), object(), [1, 2, "a"], (1, 2, "b"), {"key": 123}, None,  # Add more
               b'\x00\x01\x02\x03',  # Byte string with null characters
               1234567890123456789012345678901234567890.0, # float
               [1, 2, thread_func], # with function
               {"key": 123, "key2": lambda: None}, # with a lambda
               lambda: 1,  # A lambda function
               (x for x in range(10)), # generator expression
               {'a':set(), 'b':frozenset()}, # frozenset and set test
               bytearray(b"test"),
               {},
               [],
               (),
               [],
               {"1":1},
               [1, 2, {}, {"a":set()}], # nested dictionaries and sets
               ]
    try:
        for _ in range(20):  # Fixed number of iterations
            fuzz_val = fuzz_vals[_ % len(fuzz_vals)]
            t = threading.Thread(target=thread_func, args=(lock, data, fuzz_val))
            t.start()
            t.join()
        print(f"Data after threading: {data}")
    except Exception as e:
        print(f"Error during free threading fuzz: {e}")


# Fuzzing for os module timer functions
try:
    t = os.times()
    print(f"OS times: {t}")
    try:
        try:
            fuzz_val = int(sys.argv[1]) if len(sys.argv) > 1 else 0
        except (ValueError, TypeError) as e:
            print(f"Invalid fuzz value. Must be an integer: {e}")
            sys.exit(1)

        try:
            print(os.cpu_time(fuzz_val))
            print(os.times())
            print(os.getpid())
            print(os.getcwd())
            print(os.path.abspath('.'))
            print(os.listdir('.')) # Added to handle possible exceptions.
        except (IndexError, ValueError, TypeError, OSError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    except Exception as e:
        print(f"Error with os.times(): {e}")



# Fuzzing for replace protocol
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        try:
            if x is not None:
                self.x = int(x)
            if y is not None:
                self.y = int(y)
            return self
        except (ValueError, TypeError) as e:
            print(f"Error in __replace__: {e}")
            return None

    def __str__(self):
        return f"({self.x}, {self.y})"


# Function for complex typing and dbm.sqlite3 (more robustness)
def complex_function(data: typing.List[int], replacement: str = "default") -> str:
    try:
        db = dbm.open('mydatabase', 'n')  
        db['key1'] = str(data)
        db.close()
        return "Operation completed."
    except (dbm.error, OSError, TypeError, ValueError) as e:
        return f"Error: {e}"

if __name__ == "__main__":
    free_threading_fuzz()
    p = Point(1, 2)
    result = complex_function([1, 2, 3])
    print(result)

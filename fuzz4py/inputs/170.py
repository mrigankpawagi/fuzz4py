
import threading
import time
import copy
import os
import ssl
import typing

# Fuzzing for free-threading and GIL
def thread_func(lock, data):
    with lock:
        try:
            data.append(time.time())
        except Exception as e:
            print(f"Thread error: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    threads = []
    for i in range(5):
        t = threading.Thread(target=thread_func, args=(lock, data))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Data after threading: {data}")

# Fuzzing for os module timer functions
try:
    t = os.times()
    print(f"OS times: {t}")
    print(os.cpu_time())
except Exception as e:
    print(f"Error with os.times(): {e}")


# Fuzzing for replace protocol
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        return self

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

try:
    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=3)
    print(f"Original Point: {p1}, Modified Point: {p2}")
except Exception as e:
    print(f"Error with copy.replace(): {e}")


# Example of complex typing (not a comprehensive test)
def complex_function(input_data: typing.Union[list[int], tuple[str, int]]) -> str:
    if isinstance(input_data, list):
        return str(sum(input_data))
    elif isinstance(input_data, tuple):
        return input_data[0] + str(input_data[1])
    else:
        return "Invalid input"


# Test cases for the complex type annotation
try:
    result1 = complex_function([1, 2, 3])
    result2 = complex_function(("hello", 10))
    print(f"Result 1: {result1}, Result 2: {result2}")
except Exception as e:
  print(f"Error in complex_function: {e}")



free_threading_fuzz()

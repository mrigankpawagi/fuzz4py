
import threading
import time
import copy
import os
import ssl
import typing
import sys

# Fuzzing for free-threading and GIL
def thread_func(lock, data, fuzz_val):
    with lock:
        try:
            data.append(time.time() + fuzz_val)
        except Exception as e:
            print(f"Thread error: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    threads = []
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890]
    for i in range(10):
        fuzz_val = fuzz_vals[i % len(fuzz_vals)]
        t = threading.Thread(target=thread_func, args=(lock, data, fuzz_val))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Data after threading: {data}")


# Fuzzing for os module timer functions
try:
    t = os.times()
    print(f"OS times: {t}")
    try:
        fuzz_val = int(sys.argv[1]) if len(sys.argv) > 1 else 0
        fuzz_val = fuzz_val * -1
        print(os.cpu_time(fuzz_val))
    except (IndexError, ValueError) as e:
        print(f"Error getting cpu time: {e}")
except Exception as e:
    print(f"Error with os.times(): {e}")


# Fuzzing for replace protocol
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        if x is not None:
            try:
                self.x = int(x)
            except ValueError:
                print("Invalid x value")
                return None
        if y is not None:
            try:
                self.y = int(y)
            except ValueError:
                print("Invalid y value")
                return None
        return self

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


try:
    p1 = Point(1, 2)
    p2 = copy.replace(p1, x="abc")
    p3 = copy.replace(p1, x=3.14)
    p4 = copy.replace(p1, x=None)
    p5 = copy.replace(p1, x="abc", y="def")
    p6 = copy.replace(p1)
    print(f"Original Point: {p1}, Modified Point (non-numeric): {p2}, Modified Point (float): {p3}, Modified Point (None): {p4}, Modified Point (multiple): {p5}, Modified Point (no params): {p6}")
except Exception as e:
    print(f"Error with copy.replace(): {e}")


# Example of complex typing (with fuzzing)
def complex_function(input_data):
    if isinstance(input_data, list):
        try:
            return str(sum(input_data))
        except TypeError:
            return "Error: Invalid list type"
    elif isinstance(input_data, tuple):
        try:
            return input_data[0] + str(input_data[1])
        except IndexError:
            return "Error: Invalid tuple index"
    else:
        return "Invalid input"


try:
    result1 = complex_function([1, 2, 3])
    result2 = complex_function(("hello", 10))
    result3 = complex_function([1, 2, "a"])
    result4 = complex_function((1, 2))
    result5 = complex_function([])
    result6 = complex_function(())
    print(f"Result 1: {result1}, Result 2: {result2}, Result 3: {result3}, Result 4: {result4}, Result 5: {result5}, Result 6: {result6}")
except Exception as e:
  print(f"Error in complex_function: {e}")


free_threading_fuzz()

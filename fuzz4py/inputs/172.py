
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
            data.append(time.time() + fuzz_val)  #introduce a fuzzing variable
        except Exception as e:
            print(f"Thread error: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    threads = []
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890]  # Add more fuzzing values
    for i in range(10):  # Increase number of threads
        fuzz_val = fuzz_vals[i % len(fuzz_vals)]  # Cycle through fuzz values
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
        val = int(sys.argv[1]) if len(sys.argv) > 1 else 0  # Fuzz with command line arg
        val = val * -1  #fuzzing negative value
        print(os.cpu_time(val))
    except (IndexError, ValueError) as e:
        print(f"Error getting cpu time: {e}")


except Exception as e:
    print(f"Error with os.times(): {e}")


# Fuzzing for replace protocol (adding a potential for exceptions)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        if x is not None:
            try:
                self.x = int(x)  #vulnerability to type error
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
    p2 = copy.replace(p1, x="abc")  # Fuzzing with non-numeric input
    p3 = copy.replace(p1, x=3.14)   # Fuzzing with a float
    p4 = copy.replace(p1, x=None)  # Fuzzing with None
    p5 = copy.replace(p1, x="abc", y="def")   # Fuzz with multiple values
    p6 = copy.replace(p1)   # Fuzz with no parameters
    print(f"Original Point: {p1}, Modified Point (non-numeric): {p2}, Modified Point (float): {p3}, Modified Point (None): {p4}, Modified Point (multiple): {p5}, Modified Point (no params): {p6}")
except Exception as e:
    print(f"Error with copy.replace(): {e}")


# Example of complex typing (with fuzzing)
def complex_function(input_data: typing.Union[list[int], tuple[str, int]]) -> str:
    if isinstance(input_data, list):
        try:
            return str(sum(input_data))
        except TypeError:
            return "Error: Invalid list type"  # Handle potential TypeError
    elif isinstance(input_data, tuple):
        try:
            return input_data[0] + str(input_data[1])
        except IndexError:
            return "Error: Invalid tuple index"  # Handle potential IndexError
    else:
        return "Invalid input"


# Test cases for the complex type annotation
try:
    result1 = complex_function([1, 2, 3])
    result2 = complex_function(("hello", 10))
    result3 = complex_function([1, 2, "a"])  # Fuzzing with non-numeric list element
    result4 = complex_function((1, 2))  # Fuzzing with a tuple containing only ints
    result5 = complex_function([])  # Fuzzing with empty list
    result6 = complex_function(())  # Fuzzing with empty tuple
    print(f"Result 1: {result1}, Result 2: {result2}, Result 3: {result3}, Result 4: {result4}, Result 5: {result5}, Result 6: {result6}")
except Exception as e:
  print(f"Error in complex_function: {e}")



free_threading_fuzz()

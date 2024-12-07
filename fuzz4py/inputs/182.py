
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
        except (TypeError, ValueError) as e:
            print(f"Thread error: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    threads = []
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890, b"bytes", [], (), {"key": "value"}, True, False, complex(1,2)]
    for i in range(15):
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
        try:
            fuzz_val = int(sys.argv[1]) if len(sys.argv) > 1 else 0
            fuzz_val = fuzz_val * -1
            print(os.cpu_time(fuzz_val))
            print(os.times())
            print(os.getpid())
            print(os.getcwd())
            print(os.path.abspath('.'))
            print(os.listdir('.'))

            os.stat('nonexistent_file.txt')  # Attempt to stat without try-except
        except FileNotFoundError as e:
            print(f"Error: {e}")  # Handle FileNotFoundError explicitly
        except (IndexError, ValueError, TypeError) as e:
            print(f"Error getting cpu time: {e}")
        except OSError as e: #Catch broader OSError
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")  #Catch a generic exception
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
          except (ValueError, TypeError) as e:
              print(f"Invalid x value: {e}")
              return None
        if y is not None:
          try:
            self.y = int(y)
          except (ValueError, TypeError) as e:
              print(f"Invalid y value: {e}")
              return None
        return self

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

try:
    p1 = Point(1, 2)
    p2 = copy.copy(p1)
    print(f"Original point: {p1}")
    print(f"Copied point: {p2}")
    p3 = p1.__replace__(x=3)
    print(f"Modified point: {p3}")
except Exception as e:
    print(f"Error with copy.replace(): {e}")

# Example of complex typing (with fuzzing)
def complex_function(input_data):
    if isinstance(input_data, list):
        try:
            return str(sum(input_data))
        except (TypeError, ValueError):
            return "Error: Invalid list type"
    elif isinstance(input_data, tuple):
        try:
            return str(input_data[0]) + str(input_data[1])
        except (IndexError, TypeError):
            return "Error: Invalid tuple index"
    else:
        return "Invalid input"

# Example usage of complex_function
print(complex_function([1,2,3]))
print(complex_function((4,5)))
print(complex_function("not a list or tuple"))


if __name__ == "__main__":
    try:
        free_threading_fuzz()
    except Exception as e:
        print(f"An error occurred: {e}")
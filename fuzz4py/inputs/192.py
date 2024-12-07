
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
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890, b"bytes", [], (), {"key": "value"}, True, False, complex(1,2), object(), [1, 2, "a"], (1, 2, "b"), {"key": 123}, None]  #Added more types
    for i in range(20):  # Increased loop iterations
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
        fuzz_val = 0
        if len(sys.argv) > 1:
          try:
            fuzz_val = int(sys.argv[1])
          except (ValueError, TypeError):
            print("Invalid fuzz value.  Must be an integer.")
            exit(1)
            
        try:
            print(os.cpu_time(fuzz_val))
            print(os.times())
            print(os.getpid())
            print(os.getcwd())
            print(os.path.abspath('.'))
            print(os.listdir('.'))
            
            #Added more fuzzing for os.stat
            try:
                os.stat('nonexistent_file.txt')
            except FileNotFoundError as e:
                print(f"Error: {e}")
            try:
                os.stat(b"nonexistent_file.txt")
            except FileNotFoundError as e:
                print(f"Error: {e}")
            try:
                os.stat("nonexistent_file.txt".encode('utf-8'))
            except FileNotFoundError as e:
                print(f"Error: {e}")            
            try:
                os.listdir(b'/tmp')
            except FileNotFoundError as e:
              print(f"Error: {e}")

        except (IndexError, ValueError, TypeError, OSError) as e:
            print(f"Error: {e}")  # More specific exception handling
        except Exception as e:
            print(f"Unexpected error: {e}")  # Catch-all for unexpected errors
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
                self.x = int(x)  #Added check, but not required for some error cases
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

    # fuzzing __replace__
    p4 = Point(1,2)
    p5 = p4.__replace__(x="abc")
    print(f"Modified point p5: {p5}")
    p6 = p4.__replace__(x=None, y="a")
    print(f"Modified point p6: {p6}")
    
except Exception as e:
    print(f"Error with copy.replace(): {e}")


# Example of complex typing (with fuzzing)
def complex_function(input_data):
    if isinstance(input_data, list):
        try:
            return str(sum(input_data))
        except (TypeError, ValueError) as e:
            return f"Error: Invalid list type ({e})"
    elif isinstance(input_data, tuple):
        try:
            return str(input_data[0]) + str(input_data[1])
        except (IndexError, TypeError) as e:
            return f"Error: Invalid tuple index ({e})"
    else:
        return "Invalid input"

# Example usage of complex_function
print(complex_function([1,2,3]))
print(complex_function((4,5)))
print(complex_function("not a list or tuple"))
print(complex_function([1, 2, "a"]))
print(complex_function((1, 2, "b")))  # test index error

if __name__ == "__main__":
    try:
        free_threading_fuzz()
    except Exception as e:
        print(f"An error occurred: {e}")

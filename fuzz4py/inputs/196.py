
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
            print(f"Thread error: {e}")
    return

def free_threading_fuzz():
    data = []
    lock = threading.Lock()
    threads = []
    fuzz_vals = [0, 10, -5, 1000.5, -100, 0j, "abc", None, 1234567890123456789012345678901234567890, b"bytes", [], (), {"key": "value"}, True, False, complex(1,2), object(), [1, 2, "a"], (1, 2, "b"), {"key": 123}, None]
    for _ in range(20):
        fuzz_val = fuzz_vals[_ % len(fuzz_vals)]
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
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    except Exception as e:
        print(f"Error with os.times(): {e}")


# Fuzzing for replace protocol (same as before)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        if x is not None:
            try:
                self.x = int(x)
            except (ValueError, TypeError):
                print("Invalid x value")
                return None
        if y is not None:
            try:
                self.y = int(y)
            except (ValueError, TypeError):
                print("Invalid y value")
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

    p4 = Point(1,2)
    p5 = p4.__replace__(x="abc")
    print(f"Modified point p5: {p5}")
    p6 = p4.__replace__(x=None, y="a")
    print(f"Modified point p6: {p6}")
except Exception as e:
    print(f"Error with copy.replace(): {e}")



# Function for complex typing and dbm.sqlite3
def complex_function(data: typing.List[int], replacement: str = "default"):
    """
    A function demonstrating various Python 3.13 features.
    """
    try:
        # Using dbm.sqlite3
        db = dbm.open('mydatabase', 'c')
        db['key1'] = str(data)
        db.close()

        # Free-threading and GIL (same as before)
        threads = []
        for i in range(5):
            thread = threading.Thread(target=work, args=(i, data,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

        # Example of copy.replace() (same as before)
        new_data = copy.replace(data, 100)
        return new_data
    except Exception as e:
        return f"Error: {e}"

def work(thread_id, data):
    time.sleep(0.1)  # Simulate work
    print(f"Thread {thread_id} accessing data {data}")


# Example usage of complex_function (and SSL) and main function
def create_ssl_context():
  # Fuzzing ssl.create_default_context()
  context = ssl.create_default_context()
  try:
      with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
          # Simulate a connection
          s.connect(('example.com', 443))
          return True
  except ssl.SSLError as e:
      return f"SSL Error: {e}"

def main():
    try:
        data = [1, 2, 3, 4, 5]
        result = complex_function(data)
        # ... (rest of the main function)
        print(f"Result: {result}")
        print(create_ssl_context())


    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()



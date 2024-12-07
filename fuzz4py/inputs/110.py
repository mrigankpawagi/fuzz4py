
import threading
import time
import copy
import ssl
import os
import dbm
import typing
import random
import socket


def jit_target_function(arg1, arg2):
    """
    A function likely to be JIT compiled.  Modified to include error handling.
    """
    try:
        result = 0
        for i in range(random.randint(100000, 1000000)):  # Vary loop iterations
            result += arg1 + arg2
            if result > 1000000000: #Avoid potential overflow issues
              raise OverflowError("Result too large.")
        return result
    except Exception as e:
        print(f"Error in jit_target_function: {e}")
        return None


def test_freethreading(arg):
    #Illustrative - use real C extensions for true testing.
    #Simulate a potentially race-prone function using a shared resource.
    shared_resource = 0
    lock = threading.Lock()
    
    def worker(arg):
        nonlocal shared_resource
        with lock:
            try:
                shared_resource += arg
                result = jit_target_function(shared_resource, arg)
                if result is not None:
                    return result
                else:
                    return None
            except Exception as e:
                print(f"Error in worker thread: {e}")
                return None

    threads = []
    for i in range(random.randint(2, 20)): # Vary number of threads
        t = threading.Thread(target=worker, args=(arg,))
        threads.append(t)
        try:
          t.start()
        except Exception as e:
          print(f"Error starting thread: {e}")


    results = []
    for t in threads:
        t.join()
        try:
            result = t.result() if hasattr(t, "result") else None  # Handle cases where result isn't available
            results.append(result)
        except Exception as e:
            print(f"Error joining thread: {e}")
            
    return shared_resource, results  # Return both shared resource and results from each thread.



def my_function():
    """
    This function
    has a docstring
    with various whitespace
    """
    pass

def annotated_function(arg: typing.Union[str, int, typing.Callable[[str], int]]) -> int:
    try:
        if callable(arg):
            return arg(str(random.randint(-100000, 100000)))  # Wider range, more diverse inputs
        else:
            return arg + 5  # Handle non-callable input
    except Exception as e:
        print(f"Error in annotated_function: {e}")
        return None


# Fuzzing copy.replace() (more comprehensive)
class ReplaceableClass:
    def __init__(self, value):
        self.value = value

    def __replace__(self, value=None):
        if value is not None:
            try:
              return ReplaceableClass(float(value)) #Test floats too, different type
            except Exception as e:
              print(f"Error in __replace__: {e}")
              return None
        else:
            return self

# Fuzzing os timer functions (more extensive) - Includes error handling for potential issues.
try:
    start_time = os.times()[0]
    time.sleep(random.uniform(0, 10)) # Wider range for sleep time
    end_time = os.times()[0]
    print(f"Elapsed time: {end_time - start_time}")
except Exception as e:
    print(f"Error with os.times(): {e}")


# Fuzzing dbm.sqlite3 (more extensive) - Includes error handling for invalid keys and types
try:
  db = dbm.open('mydatabase', 'c')
  for i in range(10):
      key = str(random.random())  # Random float keys
      value = str(random.random())
      db[key] = value
      try:
          print(db[key])
      except Exception as e:
          print(f"Error accessing key {key}: {e}")
  db.close()
except Exception as e:
  print(f"Error with dbm.sqlite3: {e}")


#Fuzzing ssl.create_default_context() (simulated):
try:
  context = ssl.create_default_context()
  print("SSL context created successfully")
except Exception as e:
  print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    import socket
    data = [1, 2, 3, 4, 5]
    try:
        shared_resource, results = test_freethreading(10)
        print(f"Shared Resource: {shared_resource}, Results: {results}")
        annotated_function("hello")
        annotated_function(lambda x: len(x))
        annotated_function(42)
        annotated_function(None)
        annotated_function(ReplaceableClass(42))
        test_copy_replace(data) # Call the function to test
        test_dbm_sqlite3()
        test_ssl_connection()
    except Exception as e:
        print(f"A critical error occurred: {e}")


def test_copy_replace(obj: typing.Any):
    """Tests copy.replace() with custom objects."""
    try:
        new_obj = copy.replace(obj)
    except Exception as e:
        print(f"Error during copy.replace(): {e}")


def test_dbm_sqlite3():
    """Tests the dbm.sqlite3 module."""
    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1'
        db.close()
        db = dbm.open('test.db', 'r')
        value = db['key1']
        db.close()
        os.remove('test.db')
    except Exception as e:
        print(f"Error during dbm.sqlite3 test: {e}")


def test_ssl_connection():
    """Tests ssl connection."""
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname="example.com") as s:
            s.connect(("example.com", 443))
    except ssl.SSLError as e:
        print(f"SSL connection error: {e}")

def modify_data(data: list, lock: threading.Lock) -> None:
    """Modifies a list of integers concurrently."""
    with lock:
        for i in range(len(data)):
            data[i] += 1
            data[i] *= 2
            time.sleep(0.01)
            if data[i] > 1000:
                raise ValueError("Data exceeds limit")


def test_threading_race(data: list) -> None:
    """Tests for race conditions in multi-threaded scenarios."""
    lock = threading.Lock()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=modify_data, args=(data, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


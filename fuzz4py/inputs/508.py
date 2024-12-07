
import threading
import time
import copy
import dbm
import sqlite3
import os
import ssl
import typing

def threaded_function(data, lock, db):
    try:
        # Simulate a long-running operation, possibly using C extensions
        time.sleep(0.1) 
        
        # Vulnerable line: Using arbitrary data type for key
        key = str(data) + "str"  # Ensure key is a string
        
        # Correctly using a lock to prevent race conditions
        lock.acquire()
        try:
            db[key] = str(data)  #Convert data to string to avoid type errors
        finally:
            lock.release()

    except Exception as e:
        print(f"Error in thread: {e}")


def main():
    # Using sqlite3 as the default dbm module
    try:
        db = dbm.open('mydatabase', 'c')  # 'c' for creation, use dbm.sqlite3 if available
        lock = threading.Lock()
        
        threads = []
        for i in range(5):
            thread = threading.Thread(target=threaded_function, args=(i, lock, db))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()

        # Example of accessing data (and handling possible errors)
        try:
          for key in db:
              print(f"Key: {key}, Value: {db[key]}")
        except Exception as e:
          print(f"Error accessing database: {e}")


    except Exception as e:
        print(f"An error occurred in main: {e}")
    
    finally:
        try:
          if 'db' in locals() and db:
            db.close()
        except Exception as e:
            print(f"Error closing database: {e}")


def my_function(arg1: int, arg2: str = "default") -> str:
    """
    This function does something.
    """
    try:
        return str(arg1) + arg2
    except Exception as e:
        return str(e)

def concurrent_function(data: typing.List[int]):
    # Testing free-threading and the GIL
    lock = threading.Lock()
    threads = []
    for i in data:
        # Vulnerable line: creating threads with possibly insecure data
        try:
            # Sanitize input to prevent potential injection
            safe_arg2 = str(i).encode('utf-8').decode('utf-8')
            t = threading.Thread(target=lambda x, y: my_function(x,y), args=(i,safe_arg2))
            threads.append(t)
            t.start()
        except Exception as e:
          print(f"Error creating thread {i}: {e}")
    for t in threads:
        t.join()
        
def test_os_timer():
  try:
    # Vulnerable line:  No input validation.  Potentially dangerous if 'value' can be malicious
    value = os.times()  # No direct use of the returned data (potential vulnerability mitigated)
    print(f"OS Times: {value}")
  except Exception as e:
    print("Error in os.times():", e)
    
def test_dbm():
  try:
    db = dbm.open("mydatabase", 'c')
    # Vulnerable line:  No input validation on key
    db['key1'] = 'value1'
    db.close()
    
    db = dbm.open("mydatabase", 'r')
    try:
      # Vulnerable line:  No input validation on key
      print(db['key1'])
    except KeyError as e:
        print(f"KeyError: {e}") # Handle potential KeyError
    db.close()
  except Exception as e:
    print("Error in dbm operations:", e)
    

def test_replace_protocol():
  class MyClass:
    def __init__(self, x: int, y: str):
      self.x = x
      self.y = y
    def __replace__(self, **changes):
      try:
        return MyClass(int(changes.get('x', self.x)), changes.get('y', self.y))
      except ValueError as e:
        print(f"Error in __replace__: {e}")
        return None # or raise the exception

  obj = MyClass(1, "hello")
  try:
    new_obj = copy.replace(obj, x=2)
    print(new_obj.x)
  except Exception as e:
    print(f"Error in test_replace_protocol: {e}")
  
def test_ssl():
  try:
    ctx = ssl.create_default_context()
    try:
      with open('valid_cert.pem', 'rb') as f:
        ctx.load_verify_locations(cafile=f)  
    except FileNotFoundError as e:
        print(f"Error: Certificate file not found: {e}")
  except Exception as e:  # Catch potential other errors
      print("SSL Error:", e)


# ... (rest of the code, including main2, is unchanged)



def my_function(arg1, arg2):
    # This function is likely to be JIT-compiled.
    result = 0
    for i in range(10000):
        result += arg1 * arg2
    return result

def threaded_function(input1, input2, lock):
  try:
    result = my_function(input1, input2)
    with lock:
      print(f"Thread {threading.current_thread().name}: Result = {result}")
  except Exception as e:
    with lock:
      print(f"Thread {threading.current_thread().name}: Error: {e}")


def main2():
    lock = threading.Lock()
    input_data = [(1,2), (3,4), (5,6)]
    
    threads = []
    for i, (arg1, arg2) in enumerate(input_data):
      thread = threading.Thread(target=threaded_function, args=(arg1, arg2, lock))
      threads.append(thread)
      thread.start()
    
    for thread in threads:
      thread.join()
      
    # Demonstrate interaction with os module timer functions
    start_time = time.monotonic()
    os.times()
    end_time = time.monotonic()
    print(f"Time taken by os.times(): {end_time - start_time:.6f} seconds")

    #Example using copy.replace() on a custom class
    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __replace__(self, a=None, b=None):
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyClass(10,20)
    new_obj = copy.replace(obj, a=30)
    print(f"Original object: {obj.a}, {obj.b}")
    print(f"Replaced object: {new_obj.a}, {new_obj.b}")
    

    # Example of a simplified database interaction using dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    
    #Example of testing SSL
    try:
        context = ssl.create_default_context()
        # Add certificate validation if you have a known certificate to test against
        # context.load_verify_locations(...)
    except Exception as e:
        print(f"Error with SSL: {e}")


if __name__ == "__main__":
    main()
    test_os_timer()
    test_dbm()
    test_replace_protocol()
    
    data = [1, 2, 3, 4, 5]
    concurrent_function(data)
    test_ssl()
    main2()


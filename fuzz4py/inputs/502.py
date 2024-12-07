
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

        # Correctly using a lock to prevent race conditions
        lock.acquire()
        try:
            db[str(data)] = data
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
        t = threading.Thread(target=lambda x: my_function(x) , args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
def test_os_timer():
  try:
    os.times()
  except Exception as e:
    print("Error in os.times():", e)
    
def test_dbm():
  try:
    db = dbm.open("mydatabase", 'c')
    db['key1'] = 'value1'
    db.close()
    db = dbm.open("mydatabase", 'r')
    print(db['key1'])
    db.close()
  except Exception as e:
    print("Error in dbm operations:", e)
    
def test_replace_protocol():
  class MyClass:
    def __init__(self, x: int, y: str):
      self.x = x
      self.y = y
    def __replace__(self, **changes):
      return MyClass(changes.get('x', self.x), changes.get('y', self.y))
      
  obj = MyClass(1, "hello")
  new_obj = copy.replace(obj, x=2)
  print(new_obj.x)
  
def test_ssl():
  try:
    ctx = ssl.create_default_context()
    # Replace with a valid certificate
    with open('valid_cert.pem', 'rb') as f:
        ctx.load_verify_locations(cafile=f)  
    # Further SSL operations (e.g., connection establishment) could be added here...
  except ssl.SSLError as e:
      print("SSL Error:", e)


if __name__ == "__main__":
    main()
    test_os_timer()
    test_dbm()
    test_replace_protocol()

    # Example usage of concurrent_function:
    data = [1, 2, 3, 4, 5]  
    concurrent_function(data) 
    test_ssl()


import threading
import copy
import os
import ssl
import dbm
import time
import typing
import socket

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    A function demonstrating the use of complex type annotations and threading.
    """
    results = []
    threads = []
    
    for i in data:
        thread = threading.Thread(target=process_element, args=(i,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
    # Introducing potential race condition vulnerability
    try:
        db = dbm.sqlite3.open('test.db', 'c')
        all_keys = list(db.keys()) # Convert to list for consistency
        return all_keys
    except Exception as e:
      print(f"Error retrieving data: {e}")
    finally:
        if 'db' in locals() and isinstance(db, dbm.sqlite3.Db):
            db.close()

def process_element(element: int):
  """
    Simulates a thread-safe operation.

    (Note: this is a placeholder; a real operation might involve accessing shared resources).
    """
  try:
    time.sleep(0.01 + element/100) # Introduce varying sleep times
    if not (0 <= element <= 1000):  # More concise range check
        raise ValueError("Input must be in range [0, 1000]")
    result = element * 2
    
    # Simulate accessing shared resources (potentially problematic in free-threading)
    with dbm.sqlite3.open('test.db', 'c') as db:
        db[str(element)] = str(result)
    return [result]
  except ValueError as e:
    print(f"Error processing {element}: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return [] # Return empty list for consistent structure


def test_replacement():
    class MyObject:
        def __init__(self, value):
            self.value = value
            
        def __replace__(self, other):
            if hasattr(other, 'value'):  # Check for necessary attribute
              self.value = other.value
            return self # crucial for correct behavior

        def __getitem__(self, key): 
            if key == "value": return self.value
            return None

        def __setitem__(self, key, val):
            if key == "value": self.value = val
            else:
              raise KeyError("Invalid key")

    obj1 = MyObject(10)
    try:
        obj2 = copy.replace(obj1, value=20)  # use replace
    except Exception as e:
        print(f"Error during copy.replace: {e}")
        return
    assert obj1.value == 10
    try:
      assert obj2.value == 20 # Accessing through __getitem__
    except Exception as e:
        print(f"Error accessing object: {e}")

def main():
    data = [1, 2, -3, 4, 5, 1001, -100, 0, 1000]  # More diverse input, including error cases.
    results = complex_function(data)
    print(results)

    try:
        ctx = ssl.create_default_context()
        conn = ctx.wrap_socket(socket.socket(), server_hostname="localhost") # Use a valid host here
        conn.close()
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    
    test_replacement()
    
    try:
      for i in range(1, 10):
          time_result = os.times()
          print(f"Time result {i}: {time_result}")
          time.sleep(0.1) # Introduce delays for os.times fuzzing.
    except Exception as e:
      print(f"Error during os.times(): {e}")


if __name__ == "__main__":
    main()


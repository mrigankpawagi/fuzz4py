
import threading
import copy
import os
import ssl
import dbm
import time
import typing
import socket
import random

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
        db_filename = f"test_{random.randint(1, 100)}.db"  # Fuzz database names
        db = dbm.sqlite3.open(db_filename, 'c')
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
    sleep_time = 0.01 + element/100 if 0 <= element <= 1000 else 0  # Handle out-of-range inputs gracefully
    time.sleep(sleep_time)
    if not (0 <= element <= 1000):
        raise ValueError(f"Input {element} must be in range [0, 1000]")
    result = element * 2
    
    # Simulate accessing shared resources (potentially problematic in free-threading)
    # Added error handling and randomized filename to fuzz dbm operations
    db_filename = f"test_{random.randint(1, 100)}.db"
    try:
      with dbm.sqlite3.open(db_filename, 'c') as db:
        db[str(element)] = str(result)
    except Exception as e:
      print(f"Error interacting with db {db_filename}: {e}")
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
            try:  # Added try-except to catch potential errors during replacement
              self.value = other['value'] if isinstance(other, dict) else other.value if hasattr(other, 'value') else self.value # handle different input types
            except (AttributeError, KeyError) as e:
              print(f"Error during replacement: {e}")
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
      assert obj2.value == 20 
    except Exception as e:
        print(f"Error accessing object: {e}")

def main():
    data = [1, 2, -3, 4, 5, 1001, -100, 0, 1000, 1002]  # More diverse input, including error cases and an out-of-range value.
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
          time.sleep(random.uniform(0.1, 0.5)) # Varying sleep times for fuzzing.
    except Exception as e:
      print(f"Error during os.times(): {e}")


if __name__ == "__main__":
    main()

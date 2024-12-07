
import threading
import copy
import os
import ssl
import dbm
import time
import typing

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
    
    return results

def process_element(element: int):
  """
    Simulates a thread-safe operation.

    (Note: this is a placeholder; a real operation might involve accessing shared resources).
    """
  try:
    time.sleep(0.01)
    if element < 0:
        raise ValueError("Input must be non-negative")
    results = [element * 2]
    
    # Simulate accessing shared resources (potentially problematic in free-threading)
    with dbm.sqlite3.open('test.db', 'c') as db:
        db[str(element)] = str(element * 2)
    
    return results
  except ValueError as e:
    print(f"Error processing {element}: {e}")

def test_replacement():
    class MyObject:
        def __init__(self, value):
            self.value = value
            
        def __replace__(self, other):
            self.value = other
        
    obj1 = MyObject(10)
    obj2 = copy.replace(obj1)
    obj2.value = 20
    assert obj1.value == 10

def main():
    data = [1, 2, -3, 4, 5] # includes negative to test error handling
    results = complex_function(data)
    print(results)

    try:
      ctx = ssl.create_default_context()
      # Attempt a connection (placeholder, you'd use a real connection here)
      conn = ctx.wrap_socket(socket.socket(), server_hostname="localhost") # Use a valid host here
      conn.close()
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    
    test_replacement()
    
    try:
      for i in range(1, 10):
          time_result = os.times()
          print(f"Time result {i}: {time_result}")
    except Exception as e:
      print(f"Error during os.times(): {e}")


import socket
if __name__ == "__main__":
    main()


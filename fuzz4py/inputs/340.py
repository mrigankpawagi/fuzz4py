
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket
import random

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    A function with complex logic to demonstrate potential race conditions.
    """
    results = []
    for i in range(len(data)):
        try:
            results.append(data[i] * 2)
            time.sleep(random.uniform(0.005, 0.015)) # Introduce variability
        except Exception as e:
          print(f"Error in complex_function: {e}, data: {data}")
          return None  # Handle potential errors
    return results



def threaded_func(data: typing.List[int]):
  results = complex_function(copy.deepcopy(data))
  if results is not None:
    print(f"Thread {threading.get_ident()} result: {results}")
  else:
    print(f"Thread {threading.get_ident()} failed.")


def main():
  data_to_process = [1, 2, 3, 4, 5]
  threads = []

  for i in range(len(data_to_process)):
    # Add a potential error condition
    data_to_process_copy = copy.deepcopy(data_to_process)
    if random.random() < 0.2:
      data_to_process_copy.append(None) # Injects None
    thread = threading.Thread(target=threaded_func, args=(data_to_process_copy,))
    threads.append(thread)
    thread.start()


  for thread in threads:
    thread.join()


  try:
    # Example using dbm.sqlite3 - Introduce malformed data
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'  
    db['key2'] = b'\0\x00\x01\x02\x03' #Testing binary data
    # Additional fuzzing: malformed key
    try:
        db['key3'] = b'\x00' * 1024 # very long key
        print("Very long key written")
    except Exception as e:
        print(f"Error writing long key: {e}")
    #Additional fuzzing: malformed value
    try:
        db['key4'] = b'\x00' * 1024 # very long value
        print("Very long value written")
    except Exception as e:
        print(f"Error writing long value: {e}")

    db.close()
    print("Database operation successful.")
  except Exception as e:
    print(f"Error during database operation: {e}")

  context = ssl.create_default_context()


  # Simulate a connection with a potentially problematic certificate
  #  Introduce invalid hostname to test SSL connection handling
  try:
      with context.wrap_socket(socket.socket(), server_hostname='invalid-hostname.com') as s:
          s.connect(('example.com', 443))
          print('Connected successfully.')
  except Exception as e:
      print(f'SSL connection failed: {e}')
  
  try:
    # Fuzz os.times with arguments
    t = os.times()
    print(f"OS Times: {t}")
    # Attempting to pass invalid arguments to os.times()
    try:
        result = os.times(123) #Invalid argument
        print(f"Result of os.times(123): {result}")
    except Exception as e:
        print(f"Error in os.times(123): {e}")
    #Fuzzing with different flags (if applicable)
    try:
      t2 = os.times(0)  # Pass 0 as a flag to test edge cases
      print(f"OS Times (flag 0): {t2}")
    except Exception as e:
      print(f"Error in os.times(0): {e}")


  except Exception as e:
    print(f"Error in os.times: {e}")


if __name__ == "__main__":
    main()

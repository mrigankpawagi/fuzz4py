
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    A function with complex logic to demonstrate potential race conditions.
    """
    results = []
    for i in range(len(data)):
        results.append(data[i] * 2)
        time.sleep(0.01)  # Simulate work
    return results



def threaded_func(data: typing.List[int]):
  results = complex_function(copy.deepcopy(data))
  print(f"Thread {threading.get_ident()} result: {results}")



def main():
  data_to_process = [1, 2, 3, 4, 5]
  threads = []

  for i in range(len(data_to_process)):
    thread = threading.Thread(target=threaded_func, args=(copy.deepcopy(data_to_process),))
    threads.append(thread)
    thread.start()


  for thread in threads:
    thread.join()


  try:
    # Example using dbm.sqlite3
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'
    db.close()
    print("Database operation successful.")
  except Exception as e:
    print(f"Error during database operation: {e}")

  context = ssl.create_default_context()


  # Simulate a connection with a potentially problematic certificate
  try:
      with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
          s.connect(('example.com', 443))
          print('Connected successfully.')
  except Exception as e:
      print(f'SSL connection failed: {e}')
  
  
  try:
    print(os.times())
  except Exception as e:
    print(f"Error in os.times: {e}")




if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import dbm
import typing

def my_function(data: typing.List[int]) -> typing.List[int]:
    """
    A function that modifies a list.

    Args:
        data: A list of integers.

    Returns:
        A modified list of integers.
    """
    try:
        # Simulate a potentially JIT-compiled hot loop
        for i in range(10000):
            if i % 2 == 0:
                data.append(i * 2)
            else:
                data.insert(i, i * 3)
        return data
    except Exception as e:
        return [str(e)]

def threaded_function(data):
  modified_data = my_function(data)
  # simulating some other operation with possible side effects
  db = dbm.sqlite3.open('mydatabase', 'c')
  db['key'] = str(modified_data)
  db.close()
  time.sleep(0.1)


def main():

  # Using the new copy.replace() method to potentially modify a mutable object
  original_data = [1, 2, 3]
  new_data = copy.copy(original_data)
  # Illustrative, but not guaranteed to be JIT compiled
  new_data = copy.replace(new_data, 0)

  # Demonstrates different thread use
  threads = []
  for _ in range(5):
      thread = threading.Thread(target=threaded_function, args=(new_data,))
      threads.append(thread)
      thread.start()

  for thread in threads:
      thread.join()

  # Illustrative: testing different inputs
  ssl_context = ssl.create_default_context()
  try:
    with ssl_context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
        s.connect(('example.com', 443))  # Replace with a valid host
        # Send some data
        s.sendall(b'some data')
        # Receive data
        data = s.recv(1024)
        print(f"Received data: {data}")
  except ssl.SSLError as e:
    print(f"SSL Error: {e}")


if __name__ == "__main__":
    main()

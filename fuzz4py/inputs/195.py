
import threading
import time
import copy
import os
import ssl
import dbm
import typing


def complex_function(data: typing.List[int], replacement: str = "default"):
    """
    A function demonstrating various Python 3.13 features.
    """
    try:
        # Using dbm.sqlite3
        db = dbm.open('mydatabase', 'c')
        db['key1'] = str(data)
        db.close()

        # Free-threading and GIL
        threads = []
        for i in range(5):
            thread = threading.Thread(target=work, args=(i, data,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()


        # Example of copy.replace()
        new_data = copy.replace(data, 100)
        return new_data
    except Exception as e:
        return f"Error: {e}"

def work(thread_id, data):
    time.sleep(0.1)  # Simulate work
    print(f"Thread {thread_id} accessing data {data}")

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
        # Fuzzing docstring whitespace (intentionally incorrect indentation)
        """This is a docstring with  incorrect indentation. """
        
        data = [1, 2, 3, 4, 5]
        result = complex_function(data)

        # testing os module timer function
        start_time = time.perf_counter()
        time.sleep(1) # Simulate work
        end_time = time.perf_counter()

        print(f"Elapsed time: {end_time - start_time:.4f} seconds")

        print(f"Result: {result}")
        print(create_ssl_context())


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import socket  #Import socket for ssl example
    main()

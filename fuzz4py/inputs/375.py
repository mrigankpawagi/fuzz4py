
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket
import random

def worker(data: typing.List[int], lock):
    with lock:
        for i in data:
            time.sleep(i / 1000.0)
            # Simulate a potential race condition (only affects threads)
            data[data.index(i)] = data[data.index(i)] + 1
            
            # Introduce a potential error - add a random sleep
            time.sleep(0.001 * (i % 3))  
            
            
            # Introduce a potential error by mutating the list in a different way
            if i % 2 == 0:
              try:
                data.pop(i)
              except IndexError:
                pass
            try:
                data.append(i + random.randint(-5,5))  # Fuzzing - adding random values
            except IndexError:
                pass
            except TypeError as e:
              print(f"Error in worker: {e}") # Handle potential type errors.
              

def main():
    data = list(range(100))
    lock = threading.Lock()
    threads = []

    for i in range(20): # Increased thread count
      threads.append(threading.Thread(target=worker, args=(copy.deepcopy(data), lock))) #Deep copy to avoid modifying the original in multiple threads

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    #Check if all values are updated
    try:
      for i in range(len(data)):
        if data[i] != i + 1:
          print(f"Error: Data element {i} should be {i+1}, but it is {data[i]}")
    except IndexError:
      print("Error: Index out of bounds")
    
    
    #Testing ssl, this might fail due to lack of a proper certificate
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
          s.connect(('example.com', 443))
          print("SSL connection established successfully.")
          
          # Attempt to send and receive data over the connection (fuzzing)
          s.sendall(b"Fuzzing test")
          response = s.recv(1024)
          print(f"Received: {response.decode()}")
    except ssl.SSLError as e:
        print(f"SSL connection failed: {e}")
      
      #Fuzzing with malformed data
      try:
        db = dbm.open('test.db', 'c')
        db['key'] = b'\x00' * 1024  #Fuzzing - large binary data
        db.close()
      except dbm.error as e:
          print(f"Error opening/accessing database: {e}")


if __name__ == "__main__":
    main()

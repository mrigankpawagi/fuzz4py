
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def worker(data: typing.List[int], lock):
    with lock:
        for i in data:
            time.sleep(i / 1000.0)
            # Simulate a potential race condition (only affects threads)
            data[data.index(i)] = data[data.index(i)] + 1


def main():
    data = list(range(100))
    lock = threading.Lock()
    threads = []

    for i in range(20): # Changed from 10 to 20 to increase thread count
      threads.append(threading.Thread(target=worker, args=(copy.deepcopy(data), lock))) #Deep copy to avoid modifying the original in multiple threads
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    #Check if all values are updated
    for i in range(len(data)):
      if data[i] != i + 1:
        print(f"Error: Data element {i} should be {i+1}, but it is {data[i]}")
    
    
    #Testing ssl, this might fail due to lack of a proper certificate
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
          s.connect(('example.com', 443))
          print("SSL connection established successfully.")
    except ssl.SSLError as e:
        print(f"SSL connection failed: {e}")
  


if __name__ == "__main__":
    main()

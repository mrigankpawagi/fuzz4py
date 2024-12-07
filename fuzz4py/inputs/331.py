
import threading
import copy
import dbm
import os
import ssl
import typing
import time

def worker(data, lock):
    try:
        # Simulate work, potentially using a C extension
        intermediate_result = data * 2
        # Simulate database interaction
        with dbm.open('mydatabase', 'c') as db:
            db[str(intermediate_result)] = str(time.time())
            
    except Exception as e:
        lock.acquire()
        print(f"Error in worker: {e}")
        lock.release()
    finally:
      lock.release()


def main():
    data = 10
    lock = threading.Lock()
    threads = []
    
    for i in range(5):
        t = threading.Thread(target=worker, args=(data, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    try:
      with dbm.open('mydatabase','r') as db:
        for key in db:
          print(f"Key: {key}, Value: {db[key]}")
    except Exception as e:
      print(f"Error accessing database: {e}")
    finally:
      try:
        os.remove('mydatabase')
      except:
        pass

if __name__ == "__main__":
    main()


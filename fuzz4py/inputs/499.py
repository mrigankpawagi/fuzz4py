
import threading
import time
import copy
import ssl
import dbm

def threaded_function(data, lock, db):
    try:
        # Simulate a long-running operation, possibly using C extensions
        time.sleep(0.1) 

        # Potential for race condition if not properly synchronized
        # Example with potential issue (fixed in real-world usage)
        # db[str(data)] = data  
        # use lock to prevent race conditions
        lock.acquire()
        try:
            db[str(data)] = data
        finally:
            lock.release()


        
    except Exception as e:
        print(f"Error in thread: {e}")



def main():
    #Using sqlite3 as default dbm module
    db = dbm.open('mydatabase', 'c') # 'c' for creation
    lock = threading.Lock()
    
    
    try:
        threads = []
        for i in range(5):
            thread = threading.Thread(target=threaded_function, args=(i, lock, db))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()

        # Example of accessing data (and handling possible errors)
        for key in db:
          print(f"Key: {key}, Value: {db[key]}")

    except Exception as e:
      print(f"An error occurred in main: {e}")
    
    finally:
       db.close()


if __name__ == "__main__":
    main()




import threading
import time
import copy
import dbm
import sqlite3

def threaded_function(data, lock, db):
    try:
        # Simulate a long-running operation, possibly using C extensions
        time.sleep(0.1) 

        # Correctly using a lock to prevent race conditions
        lock.acquire()
        try:
            db[str(data)] = data
        finally:
            lock.release()

    except Exception as e:
        print(f"Error in thread: {e}")


def main():
    # Using sqlite3 as the default dbm module
    try:
        db = dbm.open('mydatabase', 'c')  # 'c' for creation, use dbm.sqlite3 if available
        lock = threading.Lock()
        
        threads = []
        for i in range(5):
            thread = threading.Thread(target=threaded_function, args=(i, lock, db))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()

        # Example of accessing data (and handling possible errors)
        try:
          for key in db:
              print(f"Key: {key}, Value: {db[key]}")
        except Exception as e:
          print(f"Error accessing database: {e}")


    except Exception as e:
        print(f"An error occurred in main: {e}")
    
    finally:
        try:
          if 'db' in locals() and db:
            db.close()
        except Exception as e:
            print(f"Error closing database: {e}")


if __name__ == "__main__":
    main()


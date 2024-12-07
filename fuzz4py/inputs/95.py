
import threading
import copy
import dbm
import os
import ssl
import typing
import time


def worker(data, lock, dbm_file):
    try:
        # Simulate some operation on the data, potentially modifying it.
        new_data = copy.deepcopy(data)
        new_data["thread_id"] = threading.get_ident()

        # Access the database.
        with dbm.open(dbm_file, 'c') as db:
            db[str(threading.get_ident())] = str(new_data)
            
        with lock:
           # This is a potential race condition depending on the order of operations. 
           # The result is that a key may not be present in the database at all.
           try:
               result = db[str(threading.get_ident())]
           except KeyError as e:
                print(f"Key not found - potential race condition for thread {threading.get_ident()}.  Error: {e}")
                
    except Exception as e:
        print(f"Error in worker thread: {e}")


def main():
    # Setup for threading
    lock = threading.Lock()
    dbm_file = 'mydatabase.dbm'

    # Test data
    data = {"key1": "value1", "key2": "value2"}

    # Create threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data, lock, dbm_file))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads finished.")
    # Clean up the dbm file when finished - better for testing
    os.remove(dbm_file)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Main process error: {e}")

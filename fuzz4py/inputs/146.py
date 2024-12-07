
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def worker(data, lock, db):
    # Simulate some work, potentially slow or CPU-intensive.
    time.sleep(0.1)
    
    # Access shared resource with lock.  Critically important for fuzzing.
    with lock:
        # Simulate database writing
        key = str(data)
        db[key] = data
        # Potentially problematic:  Error handling crucial for fuzzing
        try:
            result = int(db[key])
        except (KeyError, ValueError):
            result = -1

    return result

def main():
    # Using sqlite3 as the default dbm
    db = dbm.open('mydatabase', 'c')

    # Crucial for thread safety
    lock = threading.Lock()
    threads = []
    
    # Create some complex data to fuzz with
    data_list = [
        {'a': 1, 'b': [2, 3, 4], 'c': None},
        'foo',
        b'bar',
        123,
        -123.45,
        {'a' : 1.1, 'b' : lambda x: x**2},
        [1, 2, 3, 4],
        copy.deepcopy([1, 2, 3, 4])  # Fuzzing copy.deepcopy
    ]
   
    for data in data_list:
        thread = threading.Thread(target=worker, args=(data, lock, db))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # Simulate reading data from the database for a complex case
    try:
        for key in db.keys():
            value = db[key]
            print(f"Key: {key}, Value: {value}")
    except Exception as e:
        print(f"Error reading database: {e}")

    db.close()
    
    # Demonstrate using ssl.create_default_context()
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    main()

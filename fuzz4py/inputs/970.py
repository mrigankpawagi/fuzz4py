
import threading
import copy
import dbm
import os
import ssl
import typing

def worker(data: typing.List[int], lock: threading.Lock, db: dbm.sqlite3):
    """
    A worker thread that modifies shared data and the database.
    """
    for i in data:
        lock.acquire()
        try:
            # Simulate a database update (potentially race condition)
            db[str(i)] = str(i * 2) 
            # Simulate some work...
            os.times()
        finally:
            lock.release()
    # Example of a complex annotation
    assert isinstance(data, typing.List[int])
    return 1
    

def main():
    # Test data
    data = list(range(10))
    # Initialize shared resources
    lock = threading.Lock()
    # Example of a dynamically created database
    db = dbm.sqlite3.open('mydatabase', 'c')
    
    threads = []
    for i in range(5):
        thread_data = copy.deepcopy(data)  # Important for each thread to get a copy
        # Test using different types of threads (e.g., threading.Thread, etc.)
        thread = threading.Thread(target=worker, args=(thread_data, lock, db))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    # Cleanup
    db.close()

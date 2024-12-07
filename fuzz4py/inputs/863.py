
import threading
import time
import copy
import os
import ssl
import typing

def worker(arg, lock):
    try:
        # Simulate a time-consuming operation, potentially JIT-compiled
        time.sleep(0.1)
        lock.acquire()
        try:
          # Access global variable using locals() - can lead to unexpected errors with optimizations
          print(f"Thread {threading.get_ident()} accessed global {global_var}")
          # Simulate an operation that interacts with a resource
          global_var += 1
        finally:
            lock.release()
    except Exception as e:
        print(f"Thread {threading.get_ident()} failed: {e}")


if __name__ == "__main__":
    global_var = 0
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f"Final value of global_var: {global_var}")
    
    # Example of copy.replace() -  potential race condition if not handled correctly
    class Replaceable:
        def __init__(self, value):
            self.value = value
        def __replace__(self, value):
            if not isinstance(value, int):
                raise TypeError("Value must be an integer.")
            self.value = value
            return self

    a = Replaceable(1)
    b = copy.replace(a, 2)
    
    print(f"Original value of a: {a.value}")
    print(f"Replaced value of b: {b.value}")


    # Example with dbm.sqlite3 (using an in-memory database - would be more robust in a real case)
    # import dbm.sqlite3 
    # db = dbm.sqlite3.open(':memory:', 'c')
    # db['key'] = 'value'
    # print(db['key'])



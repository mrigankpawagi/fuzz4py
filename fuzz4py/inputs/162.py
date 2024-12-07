
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(data, lock):
    try:
        # Simulate a potentially JIT-compiled operation
        result = sum(data) * 2
        
        # Accessing locals() in a multithreaded context
        local_data = locals() 
        local_data['inner_data'] = result
        
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: {result}")
        lock.release()
        
    except Exception as e:
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: Error: {e}")
        lock.release()


def main():
    # Example data, could be dynamically generated or from a file
    data = list(range(1000))
    
    # Test with and without GIL
    
    lock = threading.Lock()

    threads = []
    for i in range(5):
      thread = threading.Thread(target=worker, args=(data, lock))
      threads.append(thread)
      thread.start()

    for thread in threads:
      thread.join()


    # Fuzzing Docstrings with varying indentation
    docstring = """This is a test docstring
        with varying indentation levels
      ."""

    # Fuzzing complex type annotations
    annotation_data: typing.List[typing.Tuple[int, str]] = [(1, "a"), (2, "b")]

    # Testing dbm.sqlite3 (replace with a proper dbm.sqlite3 test)
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        db.close()

        db = dbm.open('test.db', 'r')
        print(db['key'])
        db.close()
        os.remove('test.db') # Clean up
    except Exception as e:
      print(f"dbm error: {e}")

    # Fuzzing os module timer functions (Linux specific)
    try:
        time_result = os.times()
        print(f"os.times() result: {time_result}")

    except Exception as e:
        print(f"os timer error: {e}")

    # Fuzzing ssl.create_default_context() (test with different certificates)
    try:
        context = ssl.create_default_context()
        # ... use the context to create a secure connection ...
        print("SSL context created successfully.")

    except Exception as e:
        print(f"SSL error: {e}")


if __name__ == "__main__":
    main()



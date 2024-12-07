
import threading
import time
import copy
import os
import ssl
import dbm
import typing


def my_thread_function(data, lock):
    try:
        # Simulate work that might take time.
        time.sleep(0.1)
        # Access shared resource.  Race condition vulnerability!
        lock.acquire()
        try:
            data.append(1)  # Race condition potential
        finally:
            lock.release()
    except Exception as e:
        print(f"Error in thread: {e}")

def main():
    data = []
    lock = threading.Lock()

    # Create threads
    threads = [threading.Thread(target=my_thread_function, args=(data, lock)) for _ in range(5)]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data list: {data}")

    # Example using copy.replace() - testing the replace protocol
    try:
        class MyReplaceableClass:
            def __init__(self, value):
                self.value = value

            def __replace__(self, value=None):
                return MyReplaceableClass(value or self.value)
                
        obj1 = MyReplaceableClass(10)
        obj2 = copy.replace(obj1, value=20)  # Using the replacement method
        print(f"Modified object: {obj2.value}") 
    except Exception as e:
        print(f"Error during replace: {e}")

    # Example testing ssl default context
    try:
        context = ssl.create_default_context()
        print("SSL default context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    main()



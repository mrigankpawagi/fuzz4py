
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random


def my_thread_function(data, lock):
    try:
        # Simulate work that might take time. Introduce random delay.
        time.sleep(random.uniform(0.05, 0.15))  
        # Access shared resource.  Race condition vulnerability!
        lock.acquire()
        try:
            # Introduce a potential error by appending a random value
            data.append(random.randint(-100, 100))  
        finally:
            lock.release()
    except Exception as e:
        print(f"Error in thread: {e}")


def complex_function(arg1: typing.List[int], arg2: typing.Dict[str, float]) -> int:
    """
    A function that demonstrates potential concurrency issues.
    """
    result = 0
    for i in arg1:
        result += i
        time.sleep(random.uniform(0.0005, 0.0015))  # Varying sleep times
    for key, value in arg2.items():
        try:
            result *= value
        except TypeError as e:
            print(f"TypeError in complex_function: {e}")
            return -1  # Indicate error
    return result

def main():
    # Test with and without the GIL
    data1 = [1, 2, 3, 4, 5]
    data2 = {'a': 2.5, 'b': 3.0, 'c': 1.5}


    # Free-threading test case, potentially prone to race conditions
    result_thread = []
    for _ in range(5):  # Create 5 threads
        thread = threading.Thread(target=complex_function, args=([random.randint(1, 100) for _ in range(5)], {'a': random.uniform(1, 5), 'b': random.uniform(1, 5), 'c': random.uniform(1, 5)}))
        thread.start()
        result_thread.append(thread)

    for thread in result_thread:
        thread.join()


    # Test with a custom class implementing __replace__
    class MyCustomClass(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __replace__(self, a=None, b=None):
            return MyCustomClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyCustomClass(10, 20)
    new_obj = copy.replace(obj, a=30, b=40)  # Modify both attributes
    print(f"Modified object: {new_obj.a}, {new_obj.b}")

    # Test dbm.sqlite3 (more robust testing)
    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1'  # Append a second key-value pair
        db['key2'] = str(random.randint(10000, 99999)) # Non-string
        value1 = db['key1']
        value2 = db['key2']
        db.close()
        print("dbm.sqlite3 test completed successfully.")
    except Exception as e:
        print(f"dbm error: {e}")


    # Test ssl (more robust testing)
    try:
      context = ssl.create_default_context()
      context.check_hostname = False
      context.verify_mode = ssl.CERT_NONE
      print("SSL context created successfully.")
    except Exception as e:
        print(f"SSL Error: {e}")


    # ... (rest of the main function is the same)

if __name__ == "__main__":
    main()

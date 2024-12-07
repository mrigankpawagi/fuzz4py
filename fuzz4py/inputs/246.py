
import threading
import time
import copy
import os
import ssl
import dbm
import typing


def complex_function(arg1: typing.List[int], arg2: typing.Dict[str, float]) -> int:
    """
    A function that demonstrates potential concurrency issues.
    """
    result = 0
    for i in arg1:
        result += i
        time.sleep(0.001)
    for key, value in arg2.items():
        result *= value
    return result


def main():
    # Test with and without the GIL
    data1 = [1, 2, 3, 4, 5]
    data2 = {'a': 2.5, 'b': 3.0, 'c': 1.5}
    
    
    # Free-threading test case, potentially prone to race conditions
    result_thread = []
    for _ in range(5): # Create 5 threads
        thread = threading.Thread(target=complex_function, args=([1,2,3,4,5],{'a':2.5,'b':3.0,'c':1.5}))
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
    new_obj = copy.replace(obj, a=30)
    
    # Test dbm.sqlite3
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        value = db['key']
        db.close()
    except Exception as e:
        print(f"dbm error: {e}")

    # Test ssl
    try:
      context = ssl.create_default_context()
      context.check_hostname = False #Bypass verification for fuzzing
      context.verify_mode = ssl.CERT_NONE
    except Exception as e:
        print(f"SSL Error: {e}")


    print("Test completed.")

    # Example using copy.replace() - testing the replace protocol (from the second program)
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

    # Example testing ssl default context (from the second program)
    try:
        context = ssl.create_default_context()
        print("SSL default context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

    data = []
    lock = threading.Lock()

    # Create threads
    threads = [threading.Thread(target=my_thread_function, args=(data, lock)) for _ in range(5)]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data list: {data}")



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


if __name__ == "__main__":
    main()

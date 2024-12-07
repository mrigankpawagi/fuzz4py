
import threading
import copy
import dbm
import os
import ssl
import typing
import time
import random

def threaded_function(data: int, use_gil: bool = True) -> int:
    """A threaded function for testing free-threading and the GIL."""
    result = 0
    for i in range(random.randint(100000, 1000000)):  # Random loop iterations
        result += i
    return result


def main():
    """Main function to demonstrate various Python features and potential issues."""
    # Free-threading and JIT compilation test
    threads = []
    for i in range(random.randint(1, 10)):  # Random number of threads
        thread = threading.Thread(target=threaded_function, args=(i,), kwargs={'use_gil': True})
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


    # copy.replace() test
    class ReplaceableClass:
        def __init__(self, value):
            self.value = value
        def __replace__(self, value=None, other_attr=None):  # Added a new attribute
            if value is not None:
                return ReplaceableClass(value)
            return self

    obj = ReplaceableClass(10)
    new_obj = copy.replace(obj, value=20, other_attr="some_value")  # Added new attribute
    print(f"Original object: {obj.value}, new object: {new_obj.value}")

    # dbm.sqlite3 test
    try:
        db_file = f'mydatabase_{random.randint(1,100)}.db'  # Random filename
        db = dbm.open(db_file, 'c')  
        db['key1'] = str(random.randint(1, 1000))  # Non-string value
        db.close()

        db = dbm.open(db_file, 'r')
        try:
            value = db['key1']
            print(f"Retrieved value: {value}")
        except KeyError as e:
          print(f"Error with dbm: {e}")  # Handle KeyError
        db.close()

        os.remove(db_file)  # Clean up


    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")

    # os module timer functions
    try:
        start_time = time.perf_counter()
        result = os.times()
        end_time = time.perf_counter()
        print(f"os.times() result: {result}, execution time: {end_time - start_time}")
        
    except Exception as e:
        print(f"Error with os module timer: {e}")

    # ssl test
    try:
        context = ssl.create_default_context()
        # This would be replaced by a real connection test in a full fuzzer
        print("SSL context created successfully.")

    except Exception as e:
        print(f"SSL error: {e}")

if __name__ == "__main__":
    main()


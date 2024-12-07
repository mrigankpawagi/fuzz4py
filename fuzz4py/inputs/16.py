
import copy
import typing
import threading
import time
import os
import ssl
import dbm
import random

def complex_function(data: typing.List[int], replace_value: int = 0) -> typing.List[int]:
    """
    A function demonstrating the use of copy.deepcopy() and potentially complex
    behavior.  This version avoids a potential race condition.
    """
    
    # Create a local copy to modify
    local_copy = copy.deepcopy(data)
    
    try:
        # Modify the local copy outside of a thread
        local_copy[0] = replace_value
        # Introduce potential error - negative index
        local_copy[-100] = 1
    except IndexError:
        print("Index Error caught, likely due to input data issues.")
    
    # Simulate other operations, but we return immediately.
    return local_copy


def main_complex():
  # Example usage:
  input_data = [1, 2, 3]
  result = complex_function(input_data)
  print(f"Original data: {input_data}")
  print(f"Modified data: {result}")


def slow_function(arg1: int, arg2: str) -> int:
    """
    This function simulates a computationally expensive task.
    """
    time.sleep(random.random())  # Introduce randomness
    try:
        return arg1 * len(arg2)
    except TypeError:
        print("TypeError caught in slow_function.")
        return 0


def test_threading():
    """
    This test case demonstrates multithreading and the GIL.
    """
    
    results = []
    threads = []

    for i in range(5):
        thread = threading.Thread(target=slow_function, args=(i, str(i)))
        thread.start()
        threads.append(thread)
        # Introduce a random delay
        time.sleep(random.random())


    for thread in threads:
        thread.join()
        
    for thread in threads:
        try:
            result = thread.result() if hasattr(thread, 'result') else None
            if result is not None:
              results.append(result)
            else:
              print("Thread result not available.")
        except AttributeError:  # handle potential issues in result attribute
            print("Thread result is not available or not set.")
        except Exception as e:
            print(f"Error in thread: {e}")
    print("Results:", results)


def test_replace(obj: typing.Any) -> typing.Any:
    """
    This test case demonstrates the copy.replace() method for custom objects.
    """
    try:
        replaced_obj = copy.replace(obj)
        return replaced_obj
    except TypeError as e:
        print(f"Error in replace: {e}")
        return None


def main_fuzzing():
    # Fuzzing with various data types
    test_threading()
    # Fuzzing copy.replace with various objects
    custom_obj = {'a':1, 'b': 2}
    test_replace(custom_obj)
    
    try:
        # Fuzzing dbm.sqlite3 - more complex example with potential errors.
        db = dbm.open('test.db', 'c')  # using 'c' (create)
        db['key'] = 'value'
        db['key2'] = 123 # Integer
        db['key3'] = None # None type
        db['key4'] = {'a':1} # Dictionary
        
        # Add more fuzzing data - more diverse types
        db['key5'] = b'binary data'  # binary data
        db['key6'] = 3.14159  # float
        db['key7'] = True  # boolean
        db['key8'] = complex(1,2) # complex number
        db['key9'] = [1,2,3] # list
        db['key10'] = (1,2) # tuple
        db['key11'] = {1,2} # set
        db.close()
    except Exception as e:
        print(f"Error in dbm.sqlite3: {e}")
    
    try:
        # Test the ssl module, with invalid context types
        context = ssl.create_default_context()
        invalid_context = 123
        try:
            ssl.create_default_context(invalid_context)
        except Exception as e:
            print(f"Error in ssl: {e}")
        print("SSL context created successfully (or at least one valid type).")
    except Exception as e:
        print(f"Error in ssl: {e}")


if __name__ == "__main__":
    main_complex()
    main_fuzzing()


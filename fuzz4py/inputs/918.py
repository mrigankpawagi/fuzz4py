
import threading
import time
import copy
import os
import ssl
import typing
import random
import dbm
import sys

def complex_function(data: typing.List[int], replace_val: int = 0) -> typing.List[int]:
    """
    A function with complex logic that demonstrates threading.
    Also uses copy.replace() and typing annotations.
    """
    if not isinstance(data, list):
        raise TypeError("Input data must be a list.")
    
    local_data = data[:]  # Create a copy to avoid modifying the original data in the thread
    
    # Introduce potential error by iterating outside list bounds
    try:
        for i in range(len(local_data) + random.randint(-5, 5)):
            if isinstance(local_data[i], int):
                local_data[i] = local_data[i] + 1
    except IndexError as e:
        print(f"IndexError during processing: {e}")
        return None  # Indicate failure

    time.sleep(1)

    if hasattr(local_data[0], "__replace__"):
        try:
            local_data_copy = copy.replace(local_data[0], newval=replace_val)  # Potential failure
            local_data[0] = local_data_copy
        except Exception as e:
            print(f"Error during copy.replace: {e}")
            return None

    return local_data


def thread_test():
  
  test_data = [1,2,3,4,5]
  
  results = []

  for i in range(3):
    thread_result = threading.Thread(target=complex_function, args=(test_data.copy(), i)) # Crucial: copy the list
    thread_result.start()
    results.append(thread_result)

  for thread in results:
    thread.join()

  for i in range(3):
    # Correctly accessing the result of each thread
    result = complex_function(test_data.copy(), i)
    if result is not None:  # Check for potential errors from the thread
        print(f"result {i+1}:", result)
    else:
        print(f"result {i+1}: Error")

  return results


def complex_function2(data: typing.List[int]) -> int:
    """
    A complex function demonstrating various Python features.
    """
    result = 0
    try:
        for item in data:
            result += item * 2
        return result
    except TypeError:
        return -1

def multithreaded_function(data):
    """
    A multi-threaded function that uses the GIL.
    """

    threads = []
    for item in data:
        t = threading.Thread(target=complex_function2, args=(item,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def fuzz_replace_protocol(data):
    class Replaceable:
        def __init__(self, value):
            self.value = value
        def __replace__(self, new_value):
            self.value = new_value
            return self

    try:
      replaced_data = copy.replace(data, Replaceable(0))
      print("fuzz_replace_protocol result:", replaced_data)
    except Exception as e:
      print(f"fuzz_replace_protocol error: {e}")


def fuzz_dbm_sqlite(filename):
    db = dbm.open(filename, 'c')
    try:
        db['key'] = 'value'
        value = db['key']
        print(f"dbm.sqlite3 result: {value}")
    except Exception as e:
        print(f"Error accessing database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
  try:
    data = [1,2,3,4,5]
    multithreaded_function(data)  # Exercise multithreading with GIL
    fuzz_replace_protocol(data)  # Test replace protocol

    # Fuzzing dbm.sqlite3 (with error handling)
    fuzz_dbm_sqlite("test_db")

    # Example with possible JIT compilation (hot loop)
    results = []
    for _ in range(10000):
        results.append(complex_function2([1, 2, 3]))
    print(sum(results))
    
    # Fuzzing ssl.create_default_context (with error handling)
    context = ssl.create_default_context()
    try:
      with context.wrap_socket(sys.stdout.buffer, server_hostname='example.com') as ssock:
        ssock.write(b'hello')
    except Exception as e:
      print(f"SSL error: {e}")
      
    thread_test()
    
  except Exception as e:
    print(f"General Error: {e}")

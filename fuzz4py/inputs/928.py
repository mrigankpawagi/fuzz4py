
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys

def race_condition_example(data: list[int]) -> list[int]:
    """
    Demonstrates a potential race condition (if not thread safe)
    """
    lock = threading.Lock()
    result = []
    threads = []
    for i in data:
        thread = threading.Thread(target=process_data, args=(i, lock, result))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return result

def process_data(value: int, lock: threading.Lock, result: list[int]):
  """Helper function for race_condition_example."""
  lock.acquire()
  try:
    #Introduce potential error - divide by zero
    if value != 0:
        result.append(value * 2)
    else:
        result.append(-1)
  finally:
    lock.release()

def complex_annotation_example(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
  """
  An example showcasing complex type annotations
  """
  results = []
  for item in data:
    if isinstance(item, int):
      results.append(item * 2)
    elif isinstance(item, str):
        try:
            results.append(int(item) * 3)
        except ValueError:
            results.append(0)  # More robust handling of non-integer strings
    else:
        results.append(-1)  # Handle unexpected types more consistently
  return results
  
def fuzz_replace_protocol(data: list):
  """Example using copy.replace() with potential issue"""
  try:
    return copy.deepcopy(data) # using deepcopy as the replace protocol was not fully explained.
  except Exception as e:
      return f"Error: {e}"


# Fuzzing dbm.sqlite3 - more comprehensive fuzzing
def fuzz_dbm_sqlite3():
    try:
        db = dbm.open('test.db', 'c')
        key = str(random.randint(1, 100))
        value = str(random.randint(1, 1000))
        db[key] = value
        db.close()
        db2 = dbm.open('test.db', 'r')
        result = db2.get(key)  # handle missing keys gracefully
        db2.close()
        os.remove('test.db')  # Cleanup
        return result
    except Exception as e:
        return f"Error: {e}"

# Fuzzing OS timer
def fuzz_os_timer():
  try:
    return os.times()
  except Exception as e:
    return f"Error: {e}"

# Fuzzing ssl
def fuzz_ssl_connection():
  try:
    context = ssl.create_default_context()
    # fuzzed hostname
    hostname = str(random.randint(1, 1000))
    return context.check_hostname(hostname, 'test.crt')  # Using a sample cert
  except Exception as e:
    return f"Error: {e}"

def threaded_function(arg):
    try:
        #Simulate a database operation (using dbm.sqlite3)
        db = dbm.open('mydatabase', 'c')
        db[str(arg)] = str(arg * 2)
        db.close()
    except Exception as e:
        print(f"Error in threaded function: {e}")

def complex_annotation_func(arg: typing.List[typing.Union[int, str]]) -> typing.Dict[str, int]:
    result = {}
    for item in arg:
        if isinstance(item, int):
            result[str(item)] = item * 2
        elif isinstance(item, str):
            result[item] = len(item)
        else:
            print("Unexpected type in complex_annotation_func")
    return result

def main():
    # Fuzzing replace protocol (PEP 618)
    class MyReplaceable:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **kwargs):
            if 'value' in kwargs:
                self.value = kwargs['value']
            return copy.copy(self)


    my_obj = MyReplaceable(10)
    replaced_obj = my_obj.__replace__(value=20)
    print(f"Original object: {my_obj.value}, Replaced object: {replaced_obj.value}")



    # Fuzzing threading and GIL (PEP 703) and JIT (PEP 744)
    threads = []
    for i in range(5):
        x = i
        thread = threading.Thread(target=threaded_function, args=(x,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # Fuzzing complex type annotations
    complex_list = [1, "hello", 3, "world", 10, "python", "123abc", 55]
    result_dict = complex_annotation_func(complex_list)
    print(result_dict)


    # Fuzzing os module timer functions
    try:
        start_time = time.perf_counter()
        os.times()
        end_time = time.perf_counter()
        print(f"Time taken by os.times(): {end_time - start_time}")
    except Exception as e:
        print(f"Error in os.times(): {e}")



    # Fuzzing docstring whitespace stripping
    def my_docstring_function(x):
        """
        This is a docstring
        with some whitespace.


        """
        return x*x
    print(my_docstring_function.__doc__)

    # Example usage - previous code
    data = [1, 2, 3, 4, 5, 0]
    complex_data = [1, "2", 3, "4a", 5, "abc", 1.23,  [1, 2], None, True]
    result = race_condition_example(data)
    print(f"Race Condition Example: {result}")
    print(f"Complex Annotation Example: {complex_annotation_example(complex_data)}")
    print(f"Fuzzing replace Protocol: {fuzz_replace_protocol([1,2,3])}")
    print(f"Fuzzing dbm: {fuzz_dbm_sqlite3()}")
    print(f"Fuzzing OS timer: {fuzz_os_timer()}")
    print(f"Fuzzing SSL: {fuzz_ssl_connection()}")


if __name__ == "__main__":
    main()

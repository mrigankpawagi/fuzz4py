
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
        #Fuzzing with different data types and special characters
        key = chr(random.randint(0, 255))
        value = chr(random.randint(0, 255))
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
    #fuzzed hostname and certificate
    hostname = str(random.randint(1, 1000))
    
    #Attempting to use different certificates. Replace with a certificate you have
    try:
        with open('test.crt', 'r') as f:
            cert = f.read()
        return context.check_hostname(hostname, cert)
    except FileNotFoundError:
        return f"Error: test.crt not found."

  except Exception as e:
    return f"Error: {e}"

def threaded_function(arg):
    try:
        #Simulate a database operation (using dbm.sqlite3)
        db = dbm.open('mydatabase', 'c')
        #Fuzzing arg input.
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
    # ... (rest of the code is the same)
    complex_list = [1, "hello", 3, "world", 10, "python", "123abc", 55, None, True, False, [], {}, ""]
    result_dict = complex_annotation_func(complex_list)
    print(result_dict)
    # ... (rest of the code is the same)

if __name__ == "__main__":
    main()

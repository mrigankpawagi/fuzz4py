
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

# Example usage - add more comprehensive test cases here
data = [1, 2, 3, 4, 5, 0]  #include a zero
complex_data = [1, "2", 3, "4a", 5, "abc", 1.23,  [1, 2], None, True] #Added more diverse types
result = race_condition_example(data)
print(f"Race Condition Example: {result}")
print(f"Complex Annotation Example: {complex_annotation_example(complex_data)}")
print(f"Fuzzing replace Protocol: {fuzz_replace_protocol([1,2,3])}")
print(f"Fuzzing dbm: {fuzz_dbm_sqlite3()}")
print(f"Fuzzing OS timer: {fuzz_os_timer()}")
print(f"Fuzzing SSL: {fuzz_ssl_connection()}")


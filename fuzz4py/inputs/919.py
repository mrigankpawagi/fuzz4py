
import threading
import time
import copy
import dbm
import os
import ssl
import typing

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
    result.append(value * 2)
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
    else:
      try:
        results.append(int(item) * 3)  # Potential for ValueError
      except ValueError as e:
          print(f"Error converting {item} to int: {e}")
  return results
  
def fuzz_replace_protocol(data: list):
  """Example using copy.replace() with potential issue"""
  try:
      return copy.replace(data, value=42) #fuzzing new protocol
  except Exception as e:
      return f"Error: {e}"


# Fuzzing dbm.sqlite3
def fuzz_dbm_sqlite3():
    try:
        db = dbm.open('test.db', 'c')  # 'c' for create
        db['key1'] = 'value1'
        db['key2'] = 'value2'  #different data type
        db.close()
        db2 = dbm.open('test.db', 'r')
        result = db2['key1']
        return result
    except Exception as e:
        return f"Error: {e}"


# Fuzzing OS timer
def fuzz_os_timer():
    try:
        return os.times()  # fuzzing timing information
    except Exception as e:
        return f"Error: {e}"
    
# Fuzzing ssl
def fuzz_ssl_connection():
  try:
    context = ssl.create_default_context()
    # Replace with your fuzzed certificate
    return context.check_hostname('www.example.com', 'test.crt')  
  except Exception as e:
    return f"Error: {e}"



# Example usage (you would add more sophisticated fuzzing here)
#  Replace with fuzzed data
data = [1, 2, 3, 4, 5]
complex_data = [1, "2", 3, "4a", 5]
result = race_condition_example(data)
print(f"Race Condition Example: {result}")
print(f"Complex Annotation Example: {complex_annotation_example(complex_data)}")
print(f"Fuzzing replace Protocol: {fuzz_replace_protocol([1,2,3])}")
print(f"Fuzzing dbm: {fuzz_dbm_sqlite3()}")
print(f"Fuzzing OS timer: {fuzz_os_timer()}")
print(f"Fuzzing SSL: {fuzz_ssl_connection()}")

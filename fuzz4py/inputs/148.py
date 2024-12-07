
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def jit_sensitive_function(data):
    """
    A function likely to be JIT compiled.
    """
    result = 0
    for i in range(len(data)):
        result += data[i]
    return result

def test_free_threading(data):
  """
  Tests the free-threading feature.
  """
  
  threads = []
  for i in range(len(data)):
    def worker(x):
      return jit_sensitive_function(x)

    t = threading.Thread(target=worker, args=(data,))
    threads.append(t)
    t.start()

  results = []
  for t in threads:
    t.join()
    # Simulate some error prone operation that can be impacted by race condition
    results.append(len(results)*2)

  return results

def test_complex_annotation(data: typing.List[typing.Union[int, str]]):
  """
  Tests complex type annotations.
  """
  result = []
  for item in data:
    if isinstance(item, int):
      result.append(str(item))
    elif isinstance(item, str):
      try:
        result.append(int(item))
      except ValueError:
        result.append(len(item))
  return result

def test_replace_protocol(data):
  """
  Tests the copy.replace() feature.
  """
  
  try:
    new_data = copy.deepcopy(data) #Use deepcopy for safety
    if hasattr(new_data, 'replace'):
        new_data.replace(0, 100)  
        return len(new_data)
    else:
        return -2  # Special return for types without replace.
  except Exception as e:
    return -1
  

def worker(data, lock, db):
    # Simulate some work, potentially slow or CPU-intensive.
    time.sleep(0.1)
    
    # Access shared resource with lock.  Critically important for fuzzing.
    with lock:
        # Simulate database writing
        key = str(data)
        db[key] = data
        # Potentially problematic:  Error handling crucial for fuzzing
        try:
            result = int(db[key])
        except (KeyError, ValueError):
            result = -1

    return result

def main():
  """
  Main function for testing.
  """
  data1 = list(range(10))
  results1 = test_free_threading(data1)
  print("Free threading results:", results1)

  data2 = [1, 2, "3", 4, "abc"]
  results2 = test_complex_annotation(data2)
  print("Complex annotation results:", results2)
  
  data3 = copy.deepcopy([1, 2, 3])
  results3 = test_replace_protocol(data3)
  print("Replace protocol results:", results3)

  try: 
    db_file = "mydatabase.db"
    db = dbm.open(db_file, 'c')  # Open for create
    db['key1'] = 'value1'
    db.close()
  except Exception as e:
      print(f"Error with dbm.sqlite3 (initialization): {e}")
  
  # Database operations in a separate section for clarity
  try:
      db = dbm.open('mydatabase', 'c')
      lock = threading.Lock()
      threads = []
      data_list = [
          {'a': 1, 'b': [2, 3, 4], 'c': None},
          'foo',
          b'bar',
          123,
          -123.45,
          {'a' : 1.1, 'b' : lambda x: x**2},
          [1, 2, 3, 4],
          copy.deepcopy([1, 2, 3, 4])  # Fuzzing copy.deepcopy
      ]
      for data in data_list:
          thread = threading.Thread(target=worker, args=(data, lock, db))
          threads.append(thread)
          thread.start()

      for thread in threads:
          thread.join()
      
      for key in db.keys():
          value = db[key]
          print(f"Key: {key}, Value: {value}")
      db.close()
  except Exception as e:
      print(f"Error with dbm.sqlite3 (operations): {e}")

  try:
    context = ssl.create_default_context()
    print("SSL context created successfully.")
  except Exception as e:
    print(f"Error with SSL context: {e}")


if __name__ == "__main__":
  main()

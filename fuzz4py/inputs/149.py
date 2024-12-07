
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
    for i in data:
        try:
            result += i
        except TypeError:
            pass  # Handle non-numeric data gracefully
    return result

def test_free_threading(data):
  """
  Tests the free-threading feature.
  """
  threads = []
  results = []
  lock = threading.Lock()  # Added lock
  for item in data:
    def worker(x, res_list, lck):
      with lck:
        res_list.append(jit_sensitive_function(x))
    t = threading.Thread(target=worker, args=(item, results, lock))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
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
    else:
      result.append(None)  # Handle unexpected types
  return result

def test_replace_protocol(data):
  """
  Tests the copy.replace() feature.
  """
  try:
    new_data = copy.deepcopy(data)
    if hasattr(new_data, 'replace'):
        new_data.replace(0, 100)  
        return len(new_data)
    else:
        return -2  # Special return for types without replace.
  except Exception as e:
    return -1
  
def worker(data, lock, db):
    """Worker thread function for database operations."""
    time.sleep(0.1)
    with lock:
      try:
        key = str(data)
        db[key] = data
        result = int(db[key])
      except (KeyError, ValueError, TypeError) as e:
        result = -2  # Handle potential errors more comprehensively.
    return result


def main():
  data1 = list(range(10))
  results1 = test_free_threading(data1)
  print("Free threading results:", results1)

  data2 = [1, 2, "3", 4, "abc", 5.5, None] # Added a few more test cases
  results2 = test_complex_annotation(data2)
  print("Complex annotation results:", results2)
  
  data3 = [1, 2, 3]
  results3 = test_replace_protocol(data3)
  print("Replace protocol results:", results3)

  try: 
    db_file = "mydatabase.db"
    db = dbm.open(db_file, 'c')  # Open for create
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
        copy.deepcopy([1, 2, 3, 4])
    ]
    for data in data_list:
      thread = threading.Thread(target=worker, args=(data, lock, db))
      threads.append(thread)
      thread.start()

    for thread in threads:
      thread.join()
      
    for key in db:
      try:
        value = db[key]
        print(f"Key: {key}, Value: {value}")
      except Exception as e:
        print(f"Error retrieving key {key}: {e}")
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

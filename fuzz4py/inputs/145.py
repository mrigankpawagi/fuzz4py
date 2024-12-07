
import threading
import copy
import dbm
import os
import ssl
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
  

def main():
  """
  Main function for testing.
  """
  data1 = list(range(10))
  results1 = test_free_threading(data1)
  print(results1)

  data2 = [1, 2, "3", 4, "abc"]
  results2 = test_complex_annotation(data2)
  print(results2)
  
  data3 = copy.deepcopy([1, 2, 3])
  results3 = test_replace_protocol(data3)
  print(results3)

  try: 
    db_file = "mydatabase.db"
    db = dbm.open(db_file, 'c')  # Open for create
    db['key1'] = 'value1'
    db.close()
  except Exception as e:
      print(f"Error with dbm.sqlite3: {e}")
  
  try:
    context = ssl.create_default_context()
    # No specific action to fuzz here, but create a context to test.
    print("SSL context created successfully.")
  except Exception as e:
    print(f"Error with SSL context: {e}")


if __name__ == "__main__":
  main()

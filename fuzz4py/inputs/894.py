
import threading
import copy
import dbm
import os
import ssl
import typing
import time
import random

# Fuzzing with free-threading (PEP 703)
def worker(lock, data, delay):
    with lock:
        time.sleep(delay)
        data.append(random.randint(1, 100))

def free_threading_test():
    data = []
    lock = threading.Lock()
    threads = []
    delays = [random.random() for _ in range(10)] # Introduce varying delays
    for i, delay in enumerate(delays):
        thread = threading.Thread(target=worker, args=(lock, data, delay))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return data

# Fuzzing JIT compiler (PEP 744) -  simple hot loop
def jit_loop(n, multiplier):
    result = 0
    for i in range(n):
        result += i * multiplier
    return result


# Fuzzing docstring whitespace stripping (Language)
def my_function(param1, extra_whitespace):
    """This function does something.
        With some extra whitespace.
    """
    return param1 + 1 + extra_whitespace


# Fuzzing annotation scopes (Language)
def annotated_function(data: typing.List[int] | typing.Dict[str, float] | str) -> str:
  if isinstance(data, list):
    return str(sum(data))
  elif isinstance(data, dict):
    return str(sum(data.values()))
  elif isinstance(data, str):
    return data
  else:
    return "Invalid input"


# Fuzzing copy.replace (Standard Library) - Custom class
class MyData:
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

  def __replace__(self, value1=None, value2=None):
      try:
          value1 = int(value1) if value1 is not None else self.value1
          value2 = int(value2) if value2 is not None else self.value2
          return MyData(value1, value2)
      except ValueError:
          return None  # Handle non-numeric input


  def __str__(self):
      return f"MyData(value1={self.value1}, value2={self.value2})"



# Fuzzing dbm.sqlite3 (Standard Library) - wider range of inputs
try:
  db = dbm.open('mydatabase', 'c')
  db['key1'] = 'value1'
  db['key2'] = 'value2'
  db['key3'] = b'\x00\x01\x02' # bytes input
  db.close()
except Exception as e:
  print(f"Error with dbm.sqlite3: {e}")


# Fuzzing os module timer functions (Standard Library)
try:
  start_time = time.perf_counter()
  time.sleep(random.uniform(-1, 10))  # Introduce negative/large sleep time
  end_time = time.perf_counter()
  print(f"Elapsed time: {end_time - start_time}")
except Exception as e:
  print(f"Error with os timer functions: {e}")


# Fuzzing ssl with varying certificate handling (Standard Library)
try:
    ssl_context = ssl.create_default_context()
    # ... (simulate ssl connection) - Placeholder
    # Replace with fuzzed SSL connection attempts
    print("SSL connection attempted (fuzzed)")
except Exception as e:
    print(f"SSL error: {e}")



# Basic execution - uncomment to run individual parts
# print(free_threading_test())
# print(jit_loop(1000, random.randint(1, 10)))
# print(my_function(5, random.random()))
# print(annotated_function([1, 2, 3]))
# print(annotated_function({'a': 1.5, 'b': 2.5}))
# print(annotated_function("test")) # Testing string input
# my_data = MyData(10, 20)
# new_data = copy.replace(my_data, value1=30, value2="incorrect")  # test invalid input
# print(my_data)
# print(new_data) if new_data else print("Replacement failed")



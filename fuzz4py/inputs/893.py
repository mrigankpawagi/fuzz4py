
import threading
import copy
import dbm
import os
import ssl
import typing
import time
import random

# Fuzzing with free-threading (PEP 703)
def worker(lock, data):
    with lock:
        data.append(random.randint(1, 100))

def free_threading_test():
    data = []
    lock = threading.Lock()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker, args=(lock, data))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return data

# Fuzzing JIT compiler (PEP 744) -  simple hot loop
def jit_loop(n):
    result = 0
    for i in range(n):
        result += i * 2
    return result


# Fuzzing docstring whitespace stripping (Language)
def my_function(param1):
    """This function does something.
        With some extra whitespace.
    """
    return param1 + 1


# Fuzzing annotation scopes (Language)
def annotated_function(data: typing.List[int] | typing.Dict[str, float]) -> str:
  if isinstance(data, list):
    return str(sum(data))
  elif isinstance(data, dict):
    return str(sum(data.values()))
  else:
    return "Invalid input"

# Fuzzing copy.replace (Standard Library) - Custom class
class MyData:
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

  def __replace__(self, value1=None, value2=None):
      return MyData(value1 if value1 is not None else self.value1, value2 if value2 is not None else self.value2)

  def __str__(self):
      return f"MyData(value1={self.value1}, value2={self.value2})"


# Fuzzing dbm.sqlite3 (Standard Library)
try:
  db = dbm.open('mydatabase', 'c')
  db['key1'] = 'value1'
  db['key2'] = 'value2'
  db.close()
except Exception as e:
  print(f"Error with dbm.sqlite3: {e}")


# Fuzzing os module timer functions (Standard Library)
try:
  start_time = time.perf_counter()
  time.sleep(random.random())  # Introduce random sleep time
  end_time = time.perf_counter()
  print(f"Elapsed time: {end_time - start_time}")
except Exception as e:
  print(f"Error with os timer functions: {e}")


# Fuzzing ssl with a dummy certificate (Standard Library) - simplified for brevity
try:
    ssl_context = ssl.create_default_context()
    # ... (simulate ssl connection)
    print("SSL connection attempted")
except Exception as e:
    print(f"SSL error: {e}")


# Basic execution - uncomment to run individual parts
# print(free_threading_test())
# print(jit_loop(1000))
# print(my_function(5))
# print(annotated_function([1, 2, 3]))
# print(annotated_function({'a': 1.5, 'b': 2.5}))
# my_data = MyData(10, 20)
# new_data = copy.replace(my_data, value1=30)
# print(my_data)
# print(new_data)


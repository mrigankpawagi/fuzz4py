
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
    delays = [random.random() for _ in range(10)]
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
          return None


  def __str__(self):
      return f"MyData(value1={self.value1}, value2={self.value2})"


# Fuzzing dbm.sqlite3 (Standard Library)
def dbm_test():
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db['key2'] = 'value2'
        db['key3'] = b'\x00\x01\x02'
        db.close()
        print("dbm test successful")
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


# Fuzzing os module timer functions (Standard Library)
def os_timer_test():
    try:
        start_time = time.perf_counter()
        time.sleep(random.uniform(-1, 10))
        end_time = time.perf_counter()
        print(f"Elapsed time: {end_time - start_time}")
    except Exception as e:
        print(f"Error with os timer functions: {e}")


# Fuzzing ssl (Standard Library)
def ssl_test():
    try:
        ssl_context = ssl.create_default_context()
        print("SSL connection attempted (fuzzed)")  # Placeholder
    except Exception as e:
        print(f"SSL error: {e}")



def process_element(element, context):
  try:
    key = str(element)
    context[key] = str(element * 2)
    time.sleep(0.1)
  except Exception as e:
      print(f"Error processing element: {e}")

def multithreaded_function(data, context):
  threads = []
  for i in data:
    t = threading.Thread(target=process_element, args=(i, context))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  return 0



def jit_test_function(data):
    total = 0
    for i in data:
        total += i
    return total


def main():
  dbm_test()
  os_timer_test()
  ssl_test()

  try:
      context = dbm.sqlite3.open('test_db', 'c')
      data = [1, 2, 3, 4]
      result = multithreaded_function(data, context)
      print(f"Result of multithreaded function: {result}")

      data = list(range(10000))  
      result = jit_test_function(data)
      print(f"Result of jit_test_function: {result}")

      context.close()
  except Exception as e:
    print(f"Error during database or JIT operations: {e}")

  try:
    orig_obj = {"a": 1, "b": 2}
    new_obj = copy.replace(orig_obj, a=3)
    print(f"Original: {orig_obj}, New: {new_obj}")
  except Exception as e:
    print(f"Error in copy.replace: {e}")



  def test_func():
    """This is a test function.
    """
    pass
  print(test_func.__doc__)

if __name__ == "__main__":
    main()


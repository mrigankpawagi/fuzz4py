
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import functools
import random

# Fuzzing free-threading (PEP 703)
def worker(lock, data, delay):
    with lock:
        # Simulate a potentially race-prone operation
        data.append(random.randint(1, 10))  # Add random data
        time.sleep(delay)
        return len(data)



def free_threading_test():
    data = []
    lock = threading.Lock()
    threads = []
    delays = [random.uniform(0.001, 0.05) for _ in range(5)]  # Fuzz delays
    for i, delay in enumerate(delays):
        thread = threading.Thread(target=worker, args=(lock, data, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return len(data)


# Fuzzing JIT compiler (PEP 744) - Hot loop
def jit_test(n):
    sum_val = 0
    for i in range(n):
        sum_val += i * i
        # Add a random pause
        time.sleep(random.random() * 0.001)  # Fuzz with small delays
    return sum_val


# Fuzzing docstring whitespace stripping (Language)
def my_function(arg1, arg2):
  """
  This is a docstring.

  Args:
    arg1: The first argument.
    arg2: The second argument.
  """
  return arg1 + arg2


# Fuzzing complex type annotations (Language)
def annotated_function(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
  result = []
  for item in data:
    if isinstance(item, int):
      result.append(item)
    elif isinstance(item, str):
      try:
        result.append(int(item))
      except ValueError:
        pass
      
  return result


# Added fuzzing for different data types for annotated function
def annotated_function_fuzzer():
    data_types = [
        [1, 2, 3, "4", 5],  # Mixed types
        [1, 2, "a", "b", "c"],  # Non-convertable strings
        [1, "1", 2, "2", 3, "3", 4,"4"], #More varied data
        [1,2,3,"4.5"], # Floats
        [1,2,3, "1a"], # Malformed strings
        [],
        [""],
        [None]  # None value
    ]
    for data in data_types:
        try:
          result = annotated_function(data)
          print(f"Annotated function result for data {data}: {result}")
        except Exception as e:
          print(f"Error with input {data}: {e}")
    
    

if __name__ == "__main__":
  # Run tests
  try:
      result = free_threading_test()
      print(f"Free threading test result: {result}")
      print(f"JIT test result (with 1000): {jit_test(1000)}")
      print(f"Function result with arguments 5, 10: {my_function(5,10)}")

      annotated_function_fuzzer()


  except Exception as e:
      print(f"An error occurred: {e}")

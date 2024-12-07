
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import functools

# Fuzzing free-threading (PEP 703)
def worker(lock, data):
    with lock:
        # Simulate a potentially race-prone operation
        data.append(1)
        time.sleep(0.01)
        return len(data)



def free_threading_test():
    data = []
    lock = threading.Lock()
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=worker, args=(lock, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return len(data)

# Fuzzing JIT compiler (PEP 744) - Hot loop
def jit_test(n):
    sum_val = 0
    for i in range(n):
        sum_val += i*i
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




if __name__ == "__main__":
  # Run tests
  try:
      result = free_threading_test()
      print(f"Free threading test result: {result}")
      print(f"JIT test result (with 1000): {jit_test(1000)}")
      print(f"Function result with arguments 5, 10: {my_function(5,10)}")


      # Sample usage with complex types. Replace with your desired data
      annotated_data = [1, 2, "3", 4, "5", "abc"]  # Example data
      annotated_result = annotated_function(annotated_data)
      print(f"Annotated function result: {annotated_result}")


  except Exception as e:
      print(f"An error occurred: {e}")


import threading
import time
import copy
import ssl
import os
import typing
import random

def worker(arg):
    try:
        print(f"Thread {threading.current_thread().name} starting with arg: {arg}")
        result = arg * 2  # Simulate some work
        
        # Introduce potential race condition
        global counter
        counter += 1  
        
        print(f"Thread {threading.current_thread().name} result: {result}")
        return result
    except Exception as e:
        print(f"Thread {threading.current_thread().name} error: {e}")
        return None


def main():
  global counter
  counter = 0

  # Fuzzing `copy.replace()`
  class MyClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def __replace__(self, a: int = None, b: str = None) -> "MyClass":
        if a is not None:
          self.a = a
        if b is not None:
          self.b = b
        return self
  
  # Fuzz with potentially invalid input
  obj = MyClass(10, "hello")
  
  a_val = random.randint(-100, 100)  
  b_val = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10)) # random string

  try:
    new_obj = copy.replace(obj, a=a_val, b=b_val)
  except Exception as e:
    print(f"Error replacing object: {e}")

  print(f"Original object: {obj.a}, {obj.b}")
  try:
    print(f"Replaced object: {new_obj.a}, {new_obj.b}")
  except Exception as e:
    print("Error accessing replaced object")

  # Fuzzing threading with PEP 703 (introducing potential race condition)
  threads = []
  for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

  # Wait for all threads to complete (crucial for race condition testing)
  for thread in threads:
    thread.join()

  print(f"Global counter after all threads: {counter}")

  # Example of complex annotation scope (fuzzing with invalid input)
  def complex_function(arg: typing.List[typing.Tuple[int, str]]) -> typing.Dict[str, int]:
      results = {}
      for tup in arg:
          try:
              x, y = tup
              if isinstance(x, int) and isinstance(y, str): # Validation added
                results[y] = x * 2
              else:
                print(f"Invalid input type for tuple: {tup}") # More specific feedback
          except Exception as e:
              print(f"Error processing tuple: {e}")
              return {} #Return empty dict if error occurs.
      return results
  
  #Fuzz with invalid data
  invalid_input = [(1, "a"), (2, "b"), (3, None), (4, 5), (5, "abcde" * 100), (6,123)] # More diverse invalid inputs.
  result = complex_function(invalid_input)
  print(f"Complex function result: {result}")



  # Example using ssl.create_default_context() (simplified, with error handling)
  try:
    context = ssl.create_default_context()
    print(f"SSL context created successfully.")
  except Exception as e:
    print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
  main()

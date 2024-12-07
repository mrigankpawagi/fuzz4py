
import threading
import time
import copy
import ssl
import os
import typing

def worker(arg):
    try:
        print(f"Thread {threading.current_thread().name} starting with arg: {arg}")
        result = arg * 2  # Simulate some work
        print(f"Thread {threading.current_thread().name} result: {result}")
        return result
    except Exception as e:
        print(f"Thread {threading.current_thread().name} error: {e}")
        return None

def main():
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

  obj = MyClass(10, "hello")
  new_obj = copy.replace(obj, a=20, b="world")
  print(f"Original object: {obj.a}, {obj.b}")
  print(f"Replaced object: {new_obj.a}, {new_obj.b}")


  # Fuzzing threading with PEP 703
  threads = []
  for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)


  # Example of complex annotation scope
  def complex_function(arg: typing.List[typing.Tuple[int, str]]) -> typing.Dict[str, int]:
      results = {}
      for tup in arg:
          try:
              x, y = tup
              results[y] = x * 2
          except Exception as e:
              print(f"Error processing tuple: {e}")
      return results
  
  result = complex_function([(1, "a"), (2, "b")])
  print(f"Complex function result: {result}")

  # Example using ssl.create_default_context() (simplified)
  try:
    context = ssl.create_default_context()
    print(f"SSL context created successfully.")
  except Exception as e:
    print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
  main()

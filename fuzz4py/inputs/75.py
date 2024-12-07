
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def jit_test_function(data: list[int]) -> int:
    """
    A function likely to be JIT-compiled, demonstrating a hot loop.
    """
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total

def race_condition_test():
    shared_data = {"value": 0}

    def incrementer():
        for _ in range(10000):
            with threading.Lock(): # Add a lock
              shared_data["value"] += 1
              time.sleep(random.random() * 0.001)


    threads = [threading.Thread(target=incrementer) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Final value: {shared_data['value']}")



def replace_test():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __replace__(self, **kwargs):
          return copy.replace(self, **kwargs)
            
    point = Point(1, 2)
    new_point = copy.replace(point, x=3)
    print(point.x)  #Output 1
    print(new_point.x) #Output 3

def docstring_fuzz():
    """
    A docstring with varying indentation.  This test fuzzes
    the behavior of tools that parse docstrings.
        Also demonstrating annotation scope with a lambda.

        x : int = lambda : 4

    """
    pass



def main():
  data = [random.randint(1, 100) for _ in range(1000)]
  try:
      jit_test_function(data)
      race_condition_test()
      replace_test()
      docstring_fuzz()

  except Exception as e:
      print(f"An error occurred: {e}")
  

if __name__ == "__main__":
    main()


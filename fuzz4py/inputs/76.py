
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
              # introduce a potential race with a  `shared_data` change
              if random.random() < 0.1:
                  shared_data["another_key"] = "some value"


    threads = [threading.Thread(target=incrementer) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Final value: {shared_data.get('value', 0)}")  #handle potential missing key


def replace_test():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __replace__(self, **kwargs):
            result = copy.copy(self)
            for key, value in kwargs.items():
                setattr(result, key, value)
            return result
            
    point = Point(1, 2)
    new_point = copy.replace(point, x=3, y=5)
  
    try:
      new_point2 = copy.replace(point, z = 10)  # Test with non-existent attribute
    except Exception as e:
      print(f"Error in replace: {e}")


    print(point.x)  #Output 1
    print(new_point.x) #Output 3
    print(new_point.y)


def docstring_fuzz():
    """
    A docstring with varying indentation.  This test fuzzes
    the behavior of tools that parse docstrings.
        Also demonstrating annotation scope with a lambda.
    
        x : int = lambda : 4  # valid but might cause issue
        # y : float =  lambda :  3
    """
    try:
        x: int = lambda: 4
        print (x())
    except Exception as e:
        print(f"Error in docstring lambda: {e}")
    pass  # removed the potentially problematic lambda inside annotation



def main():
  data = [random.randint(1, 100) for _ in range(1000)]
  try:
      jit_test_function(data)
      race_condition_test()
      replace_test()
      docstring_fuzz()
      
      # add a potential error
      nonexistent_function() # This will raise an exception

  except Exception as e:
      print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()



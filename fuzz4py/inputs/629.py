
import threading
import copy
import os
import ssl
import sqlite3
import typing

def my_function(data: typing.List[int]) -> typing.List[int]:
    """
    Processes a list of integers.
    """
    results = []
    for num in data:
        if num > 5:
            results.append(num * 2)
        else:
            results.append(num)
    return results


def threaded_function(data: typing.List[int]):
    """
    Example of multi-threading with race condition vulnerability
    """
    #Illustrating a potential race condition
    global shared_result 

    shared_result = []
    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=process_data, args=(data[i],))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    return shared_result

def process_data(num):
  global shared_result
  result = my_function([num])
  shared_result.append(result[0]) # potential race condition

def main():

    # Fuzzing with complex types
    try:
      data = [1,2,6,7,8,3,10]
      result = threaded_function(data)
      print(result)


      # Fuzzing with invalid input (illustrative)
      data_invalid = [1, 2, "a", 4, 5]
      result_invalid = my_function(data_invalid)
      print(result_invalid) # potential failure


      # Fuzzing os module timer functions
      start_time = os.times()
      # Simulate some work
      for i in range(100000):
        pass
      end_time = os.times()
      print(f"Elapsed time: {end_time[0] - start_time[0]}")


      # Fuzzing copy.replace() (illustrative)
      class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __replace__(self, x=None, y=None):
          if x is not None: self.x = x
          if y is not None: self.y = y
          return self

      point = Point(1,2)
      new_point = copy.copy(point)
      new_point.x = 3


      #Illustrative ssl
      context = ssl.create_default_context()


    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()


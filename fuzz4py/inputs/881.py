
import threading
import copy
import os
import ssl
import time
import random
import dbm
import sys
import typing

def threaded_function(arg: int) -> int:
    """
    A simple threaded function.
    """
    try:
        time.sleep(random.uniform(0.05, 0.15))
        if arg is None:
            return -2
        elif arg is not None:
            return arg * 2
        else:
            return 0
    except Exception as e:
        print(f"Error in threaded_function: {e}")
        return -1


def main():
    """
    Main function for testing threading and the new os timer functions.
    """
    args = [i for i in range(5)]
    results = []
    threads = []
    
    args.append(None)  # Fuzzing with a None value

    for arg in args:
        thread = threading.Thread(target=threaded_function, args=(arg,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    start_time = time.perf_counter()
    try:
        cpu_times = os.times()
        user_time = cpu_times[0] if len(cpu_times) > 0 else -1
        if not isinstance(user_time, (int, float)):
          user_time = -1
    except (AttributeError, IndexError, TypeError) as e:
        print(f"Error accessing os.times(): {e}")
        user_time = -1

    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"User CPU time: {user_time}")


    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, x: int = None, y: int = None):
            return Point(x if x is not None else self.x, y if y is not None else self.y)

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, other):
          if not isinstance(other, Point):
            return False
          return self.x == other.x and self.y == other.y
          

    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=3)

    try:
        p3 = copy.replace(p1, x='a')
        print(p3)
    except Exception as e:
        print(f"Error during copy.replace: {e}")

    try:
      p4 = copy.replace(p1, x = [1,2,3])
      print(p4)
    except Exception as e:
        print(f"Error during copy.replace: {e}")
    

    print(p1)
    print(p2)


    def my_func(a: typing.List[lambda x: int]) -> typing.List[int]:
        try:
            return [func(1) for func in a]
        except (TypeError, Exception) as e:
            print(f"Error in my_func: {e}")
            return []

    try:
      my_list_of_lambdas2 = [lambda x: x + 1, lambda x: x * 2, lambda x: x**2]  # Valid example
      result = my_func(my_list_of_lambdas2)
      print(result)
    except Exception as e:
        print(f"Error during my_func execution: {e}")
    
    try:
      my_list_of_lambdas3 = [1, 2, 3, 4] # incorrect list type
      result = my_func(my_list_of_lambdas3)
      print(result)
    except Exception as e:
        print(f"Error during my_func execution: {e}")

if __name__ == "__main__":
    main()


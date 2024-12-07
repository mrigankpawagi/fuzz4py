
import threading
import copy
import os
import ssl
import time
import random
import dbm
import sys
import typing

def threaded_function(arg: object) -> int:
    """
    A simple threaded function.
    """
    try:
        time.sleep(random.uniform(0.05, 0.15))
        if arg is None:
            return -2
        elif arg is not None:
            if isinstance(arg, int):
                return arg * 2
            elif isinstance(arg, float):
                return int(arg) * 2
            elif isinstance(arg, str):
                return -4
            else:
                return -3
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
    
    args.append(None)
    args.append("hello")
    args.append(10.5)
    args.append(True)
    args.append([1,2])
    args.append({"a":1})

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
        if user_time is None:
          user_time = -1
    except (AttributeError, IndexError, TypeError, ValueError) as e:
        print(f"Error accessing os.times(): {e}")
        user_time = -1

    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"User CPU time: {user_time}")


    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, x: typing.Optional[int] = None, y: typing.Optional[int] = None):
            if x is not None and not isinstance(x, int):
                raise TypeError("x must be an integer")
            if y is not None and not isinstance(y, int):
                raise TypeError("y must be an integer")
            return Point(x if x is not None else self.x, y if y is not None else self.y)
        
        def __str__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, other):
          if not isinstance(other, Point):
            return False
          return self.x == other.x and self.y == other.y

    p1 = Point(1, 2)
    p2 = copy.copy(p1)
    p2.x = 3
    p2 = p1.__replace__(x=3)
    try:
        p5 = p1.__replace__(x="a") 
    except TypeError as e:
        print(f"Error in __replace__: {e}")
    p6 = p1.__replace__(x=None, y=None)

    try:
        p3 = copy.replace(p1, x='a')
    except (TypeError, AttributeError) as e:
        print(f"Error during copy.replace: {e}")

    try:
        p4 = copy.replace(p1, x=[1, 2, 3])
    except (TypeError, AttributeError) as e:
        print(f"Error during copy.replace: {e}")

    print(p1)
    print(p2)
    print(p5)
    print(p6)

    def my_func(a: typing.List[typing.Callable[[int], int]]) -> typing.List[int]:
        if not all(callable(func) for func in a):
            raise TypeError("All elements in the list must be callable")
        return [func(1) for func in a]

    try:
        my_list_of_lambdas2 = [lambda x: x + 1, lambda x: x * 2, lambda x: x**2]
        result = my_func(my_list_of_lambdas2)
        print(result)
    except TypeError as e:
        print(f"Error in my_func: {e}")
    
    try:
        my_list_of_lambdas3 = [1, 2, 3, 4]
        result = my_func(my_list_of_lambdas3)
    except TypeError as e:
        print(f"Error in my_func: {e}")

if __name__ == "__main__":
    main()


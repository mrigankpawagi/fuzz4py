
import threading
import copy
import os
import ssl
import time
import typing
import random

def threaded_function(arg: int) -> int:
    """
    A simple threaded function.
    """
    try:
        time.sleep(random.uniform(0.05, 0.15))  # Introduce random sleep times
        return arg * 2 if arg is not None else 0  #Handle potential None arg
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

    for arg in args:
        thread = threading.Thread(target=threaded_function, args=(arg,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    # Demonstrating os.timer function (more comprehensive test)
    start_time = time.perf_counter()
    try:
        cpu_times = os.times()
        # Accessing specific elements from cpu_times (e.g., user time)
        user_time = cpu_times[0] 
    except Exception as e:
        print(f"Error accessing os.times(): {e}")
        user_time = -1

    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"User CPU time: {user_time}")


    # Demonstrating copy.replace
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, x: int = None, y: int = None):
            return Point(x if x is not None else self.x, y if y is not None else self.y)

        def __str__(self):  # Add a string representation for better output
            return f"({self.x}, {self.y})"


    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=3)
    try:
        p3 = copy.replace(p1, x='a') # testing with a string.
        print(p3)
    except Exception as e:
        print(f"Error during copy.replace: {e}")


    print(p1)
    print(p2)

    # Example demonstrating a complex type annotation with lambda and potential error handling
    def my_func(a: typing.List[lambda x: x+1]) -> typing.List[int]:
        try:
           return [x(1) for x in a]
        except TypeError as e:
           print(f"Error in my_func: {e}")
           return []
    
    try:
        my_list_of_lambdas = [lambda x: x + 1 for i in range(5)] 
        result = my_func(my_list_of_lambdas)
        print(result)
        
        #Fuzzing with incorrect input
        my_list_of_lambdas2 = [1,2,3,4]
        result = my_func(my_list_of_lambdas2)
        print(result)
    except Exception as e:
        print(f"Error during my_func execution: {e}")
    
if __name__ == "__main__":
    main()


import threading
import copy
import os
import ssl
import time
import typing

def threaded_function(arg: int) -> int:
    """
    A simple threaded function.
    """
    time.sleep(0.1)
    return arg * 2

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
    
    # Demonstrating os.timer function (example - replace with more comprehensive test)
    start_time = time.perf_counter()
    os.times()
    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time}")
    
    # Demonstrating copy.replace
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, x: int = None, y: int = None):
            return Point(x if x is not None else self.x, y if y is not None else self.y)

    p1 = Point(1,2)
    p2 = copy.replace(p1, x=3)
    print(p1.x, p1.y)
    print(p2.x, p2.y)

    # Example demonstrating a complex type annotation with lambda
    def my_func(a: typing.List[lambda x: x+1]) -> typing.List[int]: 
        return [x(1) for x in a]


if __name__ == "__main__":
    main()

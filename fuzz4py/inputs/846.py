
import threading
import copy
import time
import os
import ssl
import typing


def my_function(arg1: int, arg2: str = "default") -> str:
    """This function demonstrates a possible race condition.

    Args:
        arg1: An integer argument.
        arg2: A string argument.

    Returns:
        A string concatenation of the arguments.
    """
    return str(arg1) + arg2


def threaded_function(arg1, arg2, shared_data_list):
    # Using a lock to protect shared data. Crucial for thread safety.
    lock = threading.Lock()
    with lock:
        # Accessing and potentially modifying the shared data.
        shared_data_list.append(my_function(arg1, arg2))
    # Simulate some work
    time.sleep(0.01)


def main():
    shared_data = []
    threads = []
    for i in range(5):
        thread = threading.Thread(target=threaded_function, args=(i, str(i), shared_data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Results:", shared_data)


    # Example using copy.replace()
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __replace__(self, x=None, y=None):
          new_point = type(self)(x if x is not None else self.x, y if y is not None else self.y)
          return new_point

    p1 = Point(1, 2)
    p2 = copy.copy(p1)  # Create a shallow copy
    p2 = p2.__replace__(x=5)  # Modify the copied object
    print(f"p1: {p1.x}, {p1.y}")
    print(f"p2: {p2.x}, {p2.y}")

if __name__ == "__main__":
    main()

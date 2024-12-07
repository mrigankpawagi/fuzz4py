
import threading
import copy
import os
import ssl
import time
import typing
import random
import dbm


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

        def __str__(self):
            return f"({self.x}, {self.y})"

    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=3)
    try:
        p3 = copy.replace(p1, x='a')
        print(p3)
    except Exception as e:
        print(f"Error during copy.replace: {e}")

    print(p1)
    print(p2)

    # Example demonstrating a complex type annotation with lambda and potential error handling
    def my_func(a: typing.List[lambda x: x + 1]) -> typing.List[int]:
        try:
            return [x(1) for x in a]
        except TypeError as e:
            print(f"Error in my_func: {e}")
            return []

    try:
        my_list_of_lambdas = [lambda x: x + 1 for i in range(5)]
        result = my_func(my_list_of_lambdas)
        print(result)

        # Fuzzing with incorrect input
        my_list_of_lambdas2 = [1, 2, 3, 4]
        result = my_func(my_list_of_lambdas2)
        print(result)
    except Exception as e:
        print(f"Error during my_func execution: {e}")

    # Adding a demonstration of a simple doctest (for docstring whitespace stripping fuzzing)
    def add(a, b):
        """Adds two numbers."""
        return a + b

    def test_add():
        assert add(2, 3) == 5
        assert add(10, 20) == 30


def jit_sensitive_function(data: list[int]) -> int:
    """
    A function designed to be JIT compiled, potentially.
    """
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total


def multithreaded_function(data: list[int], delay: int) -> list:
    """
    A multithreaded function to stress free-threading.
    """
    results = []
    threads = []
    for item in data:
        t = threading.Thread(target=lambda x: results.append(x * 2), args=(item,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    time.sleep(delay)
    return results


def complex_annotation_example(data: typing.List[typing.Union[int, str]]) -> typing.Dict[str, int]:
    """
    Example using complex type annotations.
    """
    result_dict = {}
    for item in data:
        if isinstance(item, int):
            result_dict[str(item)] = item * 2
        elif isinstance(item, str):
            try:
                result_dict[item] = int(item)
            except ValueError:
                result_dict[item] = -1
    return result_dict


if __name__ == "__main__":
    # Free-threading & JIT
    data = [i for i in range(1000)]
    results = multithreaded_function(data, 1)

    try:
        jit_sensitive_function(data)
    except Exception as e:
        print("Exception during JIT function:", e)

    # Complex Annotation Testing
    annotated_data = [1, 2, 3, "4", "five", 6, 7]
    annotated_results = complex_annotation_example(annotated_data)
    print("Complex annotation results:", annotated_results)

    # dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        db.close()
    except Exception as e:
        print("Error with dbm.sqlite3:", e)

    # Placeholder for SSL testing (replace with your tests)
    try:
      context = ssl.create_default_context()
      # ... (SSL connection test code) ...
    except Exception as e:
      print("SSL error:", e)

    # os module example
    try:
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        print(f"OS timer elapsed: {end_time - start_time}")
    except Exception as e:
        print("Error with OS timer:", e)

    main()



import threading
import time
import copy
import os
import ssl
import typing
import random
import sys


def my_function(arg1: int, arg2: str) -> float:
    """
    This function takes two arguments and returns a float.

    Args:
        arg1: An integer.
        arg2: A string.


    Returns:
        A float.
    """
    try:
        if random.random() < 0.1:
            raise ZeroDivisionError("Forced error")
        if arg2 is None:
            return float(arg1) * 0  # Test with None arg2
        if isinstance(arg2, int):
            return float(arg1) * 1
        return float(arg1) * len(arg2)
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error in my_function: {e}, arg1: {arg1}, arg2: {arg2}")
        return float('nan')


def worker(data: list, lock):
    for item in data:
        lock.acquire()
        try:
            time.sleep(random.random() * 0.1)
            arg2 = "test" + str(random.randint(0, 100))
            if random.random() < 0.2:
                arg2 = None
            if random.random() < 0.1:
                arg2 = 123
            if random.random() < 0.1:
                arg2 = b"bytes"  # Test with bytes
            if random.random() < 0.1:
                arg2 = [] # Test with an empty list
            if random.random() < 0.1:
                arg2 = [1, 2, 3]
            result = my_function(item, arg2)
            print(f"Thread {threading.get_ident()} processed: {item}, result: {result}")
        except Exception as e:
            print(f"Error in thread {threading.get_ident()}: {e}")
            print(f"  arg2: {arg2}")
            print(f"  item: {item}")
        finally:
            lock.release()


def main():
    data = [1, 2, 3, 4, 5, "a", 0, -1, 1.23, None, True] # Adding more diverse types
    lock = threading.Lock()
    threads = []
    for item in data:
        t = threading.Thread(target=worker, args=(data, lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def whitespace_test():
    """This is a test with varying whitespace around
      the docstring.
      This line has extra whitespace.
      """
    print("docstring")
    print("And a second line")


def complex_annotation(data: typing.List[typing.Union[typing.Tuple[int, str], None, str]]) -> typing.Dict[int, float]:
    result = {}
    for item in data:
        if item is not None and isinstance(item, tuple) and isinstance(item[0], int) and item[0] > 0:
            try:
                result[item[0]] = float(item[0])
            except (TypeError, ValueError) as e:
                print(f"Error in complex_annotation: {e}, item: {item}")
                result[item[0]] = float('nan')  # More robust error handling
    return result


def complex_function(data: typing.List[int], verbose: bool = False) -> typing.List[int]:
    """
    A function demonstrating free-threading and JIT compiler potential issues.
    """
    if verbose:
        print("Starting complex_function")
    result = []
    for i in data:
        if i > 10:
            result.append(i * 2)
        elif i < 0:
            result.append(0)
        else:
            result.append(i)
    if verbose:
        print("Finished complex_function")
    return result


def test_free_threading():
    data = [1, 2, 3, 4, 5, 12, 15, 20, -5, 0, sys.maxsize] # Add a very large int
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=complex_function, args=(data,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("threading with GIL")
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=complex_function, args=(data, False)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("threading without GIL")
    return True


def fuzz_replace(obj):
    if hasattr(obj, '__replace__'):
        try:
            replaced_obj = copy.replace(obj, some_attribute=42)
            return replaced_obj
        except Exception as e:
            print(f"Exception during replace: {e}")


if __name__ == "__main__":
    try:
        test_free_threading()
    except Exception as e:
        print(f"An error occurred: {e}")


    class ReplaceableObject:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **changes):
            self.value = changes.get('some_attribute', self.value)
            return self

    obj = ReplaceableObject(10)
    fuzz_replace(obj)
    print(f"Object after replacement: {obj.value}")


    try:
        t = time.perf_counter()
        result = os.times()
        t = time.perf_counter() - t
        print(result)
        print(f"Time taken for os.times(): {t}")
    except Exception as e:
        print(f"Error in os.times(): {e}")

    context = ssl.create_default_context()
    print("SSL context created.")

    data_for_annotation = [(1, "a"), (2, "bb"), (3, "ccc"), (None, "extra"), (1, "invalid"), "a string", (1, 123), (0, "error"), (1, 123), (10, None), (1, "a" * 1000)] #Adding a very large string
    result_annotation = complex_annotation(data_for_annotation)
    print(result_annotation)

    main()
    whitespace_test()

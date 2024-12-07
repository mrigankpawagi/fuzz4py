
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
            return 0.0  # Test with None arg2
        if isinstance(arg2, int):
            return float(arg1) * 1
        if not isinstance(arg2, str):
            try:
                arg2 = str(arg2)
            except Exception as e:
                print(f"Error converting arg2 to string: {e}. Returning NaN.")
                return float('nan')
            print("Warning: arg2 is not a string. Converting to string.")
        # Introduce potential error by multiplying by a large number
        try:
            return float(arg1) * len(arg2) * 10000000000
        except OverflowError as e:
            print(f"Overflow error: {e}. Returning NaN.")
            return float('nan')
    except (TypeError, ValueError, ZeroDivisionError, OverflowError) as e:
        print(f"Error in my_function: {e}, arg1: {arg1}, arg2: {arg2}")
        return float('nan')


def worker(data: list, lock):
    for item in data:
        lock.acquire()
        try:
            time.sleep(random.random() * 0.1)
            arg2 = "test" + str(random.randint(0, 100))
            possible_types = [None, 123, b"bytes", [], [1, 2, 3], {1: "a"}, (1, 2), object(), 123.456, float('inf'), float('-inf'), float('nan')]
            for t in possible_types:
                if random.random() < 0.1:
                    arg2 = t
            try:
                result = my_function(item, arg2)
                print(f"Thread {threading.get_ident()} processed: {item}, result: {result}")
            except Exception as e:
                print(f"Error in thread {threading.get_ident()}: {e}, Arg2: {arg2}, Item: {item}")
        except Exception as e:
            print(f"Error in thread {threading.get_ident()}: {e}")
            print(f"  arg2: {arg2}")
            print(f"  item: {item}")
        finally:
            lock.release()


def main():
    data = [1, 2, 3, 4, 5, "a", 0, -1, 1.23, None, True, 100000, -100000, "test", b"bytes", [1,2]]  # Added more diverse data
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
                result[item[0]] = float('nan')
        elif isinstance(item, str):
            try:
                result[0] = float(item)
            except ValueError:
                print(f"Unable to convert {item} to float. Skipping.")
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
    data = [1, 2, 3, 4, 5, 12, 15, 20, -5, 0, sys.maxsize, -sys.maxsize, 10000, -10000, 100000, -100000]
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=complex_function, args=(data, False)))  # Added False for argument
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("threading with GIL")


def fuzz_replace(obj):
    if hasattr(obj, '__replace__'):
        try:
            replaced_obj = copy.replace(obj, some_attribute=42)
            return replaced_obj
        except Exception as e:
            print(f"Exception during replace: {e}")


if __name__ == "__main__":
    test_free_threading()

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

    data_for_annotation = [(1, "a"), (2, "bb"), (3, "ccc"), (None, "extra"), (1, "invalid"), "a string", (1, 123), (0, "error"), (1, 123), (10, None), (1, "a" * 1000), (1, "invalid type"), (-1, "negative"), (0, "zero")]
    result_annotation = complex_annotation(data_for_annotation)
    print(result_annotation)

    main()
    whitespace_test()


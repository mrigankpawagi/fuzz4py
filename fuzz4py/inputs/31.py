
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
        # Introduce potential errors:
        if random.random() < 0.1:
            raise ZeroDivisionError("Forced error")
        return float(arg1) * len(arg2)
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error in my_function: {e}, arg1: {arg1}, arg2: {arg2}")
        return float('nan')


# Free-threading example, introducing potential race condition
def worker(data: list, lock):
    for item in data:
        lock.acquire()
        try:
            # Introduce a random delay to induce potential race conditions
            time.sleep(random.random() * 0.1)  
            #Fuzzing with potentially invalid arg2
            arg2 = 'test' + str(random.randint(0, 100))
            if random.random() < 0.2:
                arg2 = None  #fuzz with None
            result = my_function(item, arg2)
            print(f"Thread {threading.get_ident()} processed: {item}, result: {result}")
        except Exception as e:
            print(f"Error in thread {threading.get_ident()}: {e}")
            print(f"  arg2: {repr(arg2)}")
            print(f"  item: {repr(item)}")
        finally:
            lock.release()


def main():
    data = [1, 2, 3, 4, 5]
    lock = threading.Lock()

    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=worker, args=(data, lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


# Docstring whitespace testing, fuzzing with different indentation
def whitespace_test():
    """This is a test with varying whitespace around
      the docstring.  
      This line has extra whitespace.
      """
    print("docstring")

#Fuzzing by changing input type to a string
def complex_annotation(data: typing.List[typing.Union[typing.Tuple[int, str], None, str]]) -> typing.Dict[int, float]:
    result = {}
    for item in data:
        if item is not None and isinstance(item, tuple) and isinstance(item[0], int) and item[0] > 0:  # Added type check
            try:
                result[item[0]] = float(item[0])
            except (TypeError, ValueError) as e:
                print(f"Error in complex_annotation: {e}, item: {item}")
    return result

if __name__ == "__main__":
    # Testing free-threading
    main()

    # Testing Docstring whitespace
    whitespace_test()

    # Testing complex annotation, fuzzing with different input types
    data_for_annotation = [(1, "a"), (2, "bb"), (3, "ccc"), (None, "extra"), (1, "invalid"), "a string"]  # Added a test case with invalid string, and a string
    result_annotation = complex_annotation(data_for_annotation)
    print(result_annotation)

    # Illustrative example of a potentially problematic class for the replace protocol
    class MyClass:
        def __init__(self, value: int) -> None:
            self.value = value

        def __replace__(self, **kwargs) -> "MyClass":
            if 'value' in kwargs:
                try:
                    new_value = int(kwargs['value'])  # Validation
                    return MyClass(new_value)
                except ValueError as e:
                    print(f"Error in __replace__: {e}")
                    return self
            return self

    original_object = MyClass(10)
    # Fuzzing with various types
    for value in [20, "invalid", None, 10.5, [1, 2]]:
        try:
            replaced_object = copy.replace(original_object, value=value)
            print(f"Original: {original_object.value}, Replaced: {replaced_object.value}")
        except Exception as e:
            print(f"Error during replace with {value}: {e}")

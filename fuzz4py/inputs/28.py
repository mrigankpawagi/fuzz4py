
import threading
import time
import copy
import os
import ssl
import typing


def my_function(arg1: int, arg2: str) -> float:
    """
    This function takes two arguments and returns a float.

    Args:
        arg1: An integer.
        arg2: A string.


    Returns:
        A float.
    """
    return float(arg1) * len(arg2)

# Free-threading example
def worker(data: list, lock):
    for item in data:
        lock.acquire()
        try:
            result = my_function(item, 'test')
            print(f"Thread {threading.get_ident()} processed: {item}, result: {result}")
        except Exception as e:
            print(f"Error in thread {threading.get_ident()}: {e}")
        finally:
            lock.release()

def main():
    data = [1, 2, 3, 4, 5]
    lock = threading.Lock()

    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=worker, args=(data,lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Docstring whitespace testing
def whitespace_test():
    """This is a test with varying whitespace around
      the docstring"""
    print("docstring")

# Complex type annotation example
def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.Dict[int, float]:
    result = {}
    for item in data:
        if item[0] > 0:
            result[item[0]] = float(item[0])
    return result



if __name__ == "__main__":
    # Testing free-threading
    main()

    #Testing Docstring whitespace
    whitespace_test()


    #Testing complex annotation
    data_for_annotation = [(1, "a"), (2, "bb"), (3, "ccc")]
    result_annotation = complex_annotation(data_for_annotation)
    print(result_annotation)


    #Illustrative example of a potentially problematic class for the replace protocol
    class MyClass:
        def __init__(self, value: int) -> None:
            self.value = value

        def __replace__(self, **kwargs) -> "MyClass":
            if 'value' in kwargs:
                return MyClass(kwargs['value'])
            return self

    original_object = MyClass(10)
    replaced_object = copy.replace(original_object, value=20)
    print(f"Original: {original_object.value}, Replaced: {replaced_object.value}")





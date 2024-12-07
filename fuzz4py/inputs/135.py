
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random


def jit_test_function(input_list):
    """
    A function likely to be JIT-compiled.
    """
    result = 0
    for item in input_list:
        try:
            result += item * 2 if isinstance(item, (int, float)) else 0  # Explicit type check
        except TypeError:
            result = 0  # Handle errors gracefully
        except Exception as e:  # Add a general exception handler
            print(f"Unexpected error: {e}")
            result = -1  # Indicate error
    return result


def multithreaded_test(data):
    """
    Multi-threaded function testing free-threading.
    """
    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=jit_test_function, args=(data[i],))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return [t.is_alive() for t in threads]


def main():
    # Test with various inputs, including None and empty lists
    test_data_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test_data_2 = [[1, 2, 'a'], [4, 5, 6], [7, 8, 9]]
    test_data_3 = [[1, 2, 3], [4, 5, None], [7, 8, 9]]
    test_data_4 = [ [], [1], [1, 2, 3]]  # Add empty list
    test_data_5 = [[random.random() for _ in range(3)] for _ in range(3)]

    # Test with free-threading.  Adding error handling.
    try:
        multithreaded_test_result_1 = multithreaded_test(test_data_1)
        multithreaded_test_result_2 = multithreaded_test(test_data_2)
        multithreaded_test_result_3 = multithreaded_test(test_data_3)
        multithreaded_test_result_4 = multithreaded_test(test_data_4)  # Test with empty list
        multithreaded_test_result_5 = multithreaded_test(test_data_5)
    except Exception as e:
        print(f"Error in multithreaded test: {e}")


    # Example using copy.replace() (requires a class with __replace__ method)
    class MyData(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, a=None, b=None):
           if a is not None:
              self.a = a
           if b is not None:
              self.b = b
           return self

    data_copy_example = MyData(1, 2)
    try:
        replaced_data = copy.replace(data_copy_example, a=3)
        print(f"Replaced data: {replaced_data.a}, {replaced_data.b}")
    except Exception as e:
        print(f"Error in copy.replace(): {e}")

    # Test dbm.sqlite3 (more robust)
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db['key2'] = b'\x00\x01\x02'  # Test with binary data
        db.close()
        db = dbm.open('mydatabase', 'r')
        print(f"Database value: {db['key1']}, {db['key2']}")  # Read back the data
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Test ssl module (more comprehensive)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    main()

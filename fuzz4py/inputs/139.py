
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys


def jit_test_function(input_list):
    """
    A function likely to be JIT-compiled.
    """
    result = 0
    for item in input_list:
        try:
            if isinstance(item, (int, float)):
                result += item * 2
            elif isinstance(item, list):
                result += sum(item)
            elif isinstance(item, str):
               result += len(item)
            elif item is None:
                result = -2
            else:
                try:
                    result += int(item)
                except ValueError:
                    result = -3
        except (TypeError, ValueError) as e:
            print(f"Error type: {type(e)}, Error message: {e}")
            result = -1  # Indicate error
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
        try:
          t = threading.Thread(target=jit_test_function, args=(data[i],))
          threads.append(t)
          t.daemon = True  # Important: Make threads daemon
          t.start()
        except Exception as e:
            print(f"Error creating thread: {e}")
            return None
    for t in threads:
        try:
            t.join()
        except Exception as e:
            print(f"Error joining thread: {e}")
            return None
    return [t.is_alive() for t in threads]


def main():
    # Test with various inputs, including None and empty lists
    test_data_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test_data_2 = [[1, 2, 'a'], [4, 5, 6], [7, 8, 9]]
    test_data_3 = [[1, 2, 3], [4, 5, None], [7, 8, 9]]
    test_data_4 = [ [], [1], [1, 2, 3]]  # Add empty list
    test_data_5 = [[random.random() for _ in range(3)] for _ in range(3)]
    test_data_6 = [[1, 2, "abc"], [4, 5, [1,2]], [7, 8, 9.3]] # List and string
    test_data_7 = [[1, 2, "abc"], [4, 5, "xyz"], [7, 8, 9.3], [10, 11, "pqr"]]  # Different data
    test_data_8 = [[1, 2, 3], [4, 5, 6], [7, 8, object()]] #object input
    test_data_9 = [[1, 2, "abc"], [4, 5,  "xyz"], [7, 8, [1,2,3]]]  #Complex data

    # Add more varied inputs!
    test_data_10 = [ [1, 2, "abc"], [4, 5,  "xyz"], [7, 8, 9.3]]  # More data
    test_data_11 = [ [1, 2, 3], [4, 5,  "xyz"], [7, 8, b'abc']]  # byte input
    test_data_12 = [[1,2,3],[4,5,6],[7,8,9],[10,11, "abc"]] #Different data again
    test_data_13 = [["abc", 123, 4.5], [567, 'def', None], [8.9, "ghi", [1,2]]] #Mix of datatypes
    test_data_14 = [[1,2,3],[],[4,5,6]] #empty list again
    test_data = [test_data_1, test_data_2, test_data_3, test_data_4, test_data_5,test_data_6, test_data_7, test_data_8, test_data_9, test_data_10, test_data_11, test_data_12,test_data_13, test_data_14]

    results = []
    for data in test_data:
        try:
            results.append(multithreaded_test(data))
        except Exception as e:
            print(f"Error in multithreaded test for data: {data}, Error: {e}")


    for result in results:
        if result is not None:
          print(f"Multithreaded Result: {result}")

if __name__ == "__main__":
    main()

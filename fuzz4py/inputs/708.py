
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random

def jit_test_function(input_list: typing.List[int]) -> int:
    """
    A function that performs calculations on a list, likely to be JIT-compiled.
    """
    total = 0
    for num in input_list:
        try:
            total += num * num
        except TypeError:
            return -1  # Indicate error with a return value
    return total

def free_threading_example(data: list) -> list:
    """
    Illustrates multi-threading with a potentially race condition-prone operation.
    """
    results = []
    lock = threading.Lock()

    def worker(data_part):
        nonlocal results
        total = 0
        for num in data_part:
            if num is not None:  # Crucial addition to prevent TypeError
                try:
                    total += num
                except TypeError:
                    print(f"Error in worker thread: Type Error encountered.")
                    return None  # Handle potential type errors

        with lock:
            results.append(total)
        return total

    threads = []
    for i in range(0, len(data), 2):
        data_part = data[i:i + 2]
        if data_part:
          thread = threading.Thread(target=worker, args=(data_part,))
          threads.append(thread)
          thread.start()

    for thread in threads:
        thread.join()
    return results

# Fuzzing mutated code
try:
    # Free-threading and JIT example - fuzzing with varying input types
    input_data = [i for i in range(100)]
    input_data_fuzzed = input_data + [random.random()] * 5  # Add random float
    input_data_fuzzed = input_data_fuzzed + [None, "abc", 1.234]  # Add None and a string and a float

    start_time = time.time()
    jit_result = jit_test_function(input_data)
    end_time = time.time()
    print(f"JIT result: {jit_result}, Time taken: {end_time - start_time}")

    try:
      jit_result_fuzzed = jit_test_function(input_data_fuzzed)
      print(f"Fuzzed JIT result: {jit_result_fuzzed}")
    except Exception as e:
        print(f"JIT Fuzzing error: {e}")

    # Free threading example with varied input data
    result = free_threading_example(input_data)
    print(f"Free threading results: {result}")

    result_fuzzed = free_threading_example(input_data_fuzzed)
    print(f"Fuzzed free threading results: {result_fuzzed}")

    # dbm example (sqlite3) - fuzzing with malformed data
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db['key2'] = b'\x00\x01\x02'  # adding a malformed byte string
        db.close()
    except Exception as e:
        print(f"dbm error: {e}")

    # copy.replace() example (using a custom class) - fuzzing with invalid arguments
    class CustomClass:
        def __init__(self, val):
            self.val = val
        def __replace__(self, **kargs):
            try:
                new_val = kargs['val']
                return CustomClass(new_val)
            except KeyError:
                return self

    original_obj = CustomClass(10)
    new_obj = copy.replace(original_obj, val=20)
    try:
        new_obj_fuzzed = copy.replace(original_obj, val="invalid")
        print(f"copy.replace() example: Original {original_obj.val}, New {new_obj.val}, Fuzzed {new_obj_fuzzed.val}")
    except Exception as e:
        print(f"copy.replace() fuzz error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

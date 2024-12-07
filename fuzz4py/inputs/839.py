
import threading
import copy
import os
import ssl
import typing
import dbm
import time

def jit_test_function(input_list):
    """
    A function that might be JIT-compiled.
    """
    total = 0
    for x in input_list:
        total += x
    return total

def race_condition_test(data):
    """
    A function demonstrating potential race conditions.
    """
    lock = threading.Lock()
    shared_data = 0

    def worker(val):
        nonlocal shared_data
        with lock:
            shared_data += val
            time.sleep(0.01)  # Introduce slight delay for race conditions

    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=worker, args=(data[i],))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return shared_data

def complex_annotation_test(data: typing.List[typing.Union[int, str]]):
    """
    Function to test complex type annotations
    """
    if isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, int):
                result.append(item * 2)
            elif isinstance(item, str):
                result.append(item.upper())
        return result
    else:
        return "Invalid input type"


# Fuzzing example for ssl
try:
    context = ssl.create_default_context()
    context.check_hostname = False  # Disable hostname verification for fuzzing purposes
    # (Replace with your specific SSL connection code)
    # ... connection setup ...
except ssl.SSLError as e:
    print(f"SSL Error: {e}")

# Fuzzing example for dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c') #'c' for create
    db['key1'] = 'value1'
    db.close()
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")


# Fuzzing example for copy.replace
class ReplaceableClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __replace__(self, a=None, b=None):
        return ReplaceableClass(a if a is not None else self.a, b if b is not None else self.b)


# ReplaceableClass demonstrates the new copy mechanism

# Example with potential race conditions
try:
   data_race = list(range(100))
   result_race = race_condition_test(data_race)
   print(f"Race condition result: {result_race}")
except Exception as e:
   print(f"Race condition error: {e}")

# Example with complex annotations
try:
    complex_data = [1, 2, "hello", 4, "world"]
    result_annotation = complex_annotation_test(complex_data)
    print(f"Annotation result: {result_annotation}")
except Exception as e:
    print(f"Annotation error: {e}")


# Example using jit_test_function
try:
    input_list = list(range(10000))
    output = jit_test_function(input_list)
    print(f"JIT result: {output}")
except Exception as e:
    print(f"JIT error: {e}")


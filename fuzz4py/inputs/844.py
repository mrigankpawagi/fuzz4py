
import threading
import copy
import os
import ssl
import typing
import dbm
import time
import random

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
            time.sleep(random.uniform(0, 0.05))  # Varying delays

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
            try:
                if isinstance(item, int):
                    result.append(item * 2)
                elif isinstance(item, str):
                    result.append(item.upper())
                else:
                    try:
                        result.append(str(item))  #Handle unexpected types
                    except Exception as e:
                        result.append(f"Error processing {item} (Type conversion): {e}")
            except Exception as e:
                result.append(f"Error processing {item}: {e}")
        return result
    else:
        return "Invalid input type"


# Fuzzing example for ssl
try:
    context = ssl.create_default_context()
    context.check_hostname = False  # Disable hostname verification for fuzzing
    #Fuzzing with invalid certificates
    bad_cert = b'invalid certificate'
    try:
        context.load_verify_locations(cadata=bad_cert)  # Try loading an invalid cert, different type
        # ... connection setup ... (placeholder for a connection method)
        print("Invalid certificate loaded successfully")  # Indicate success, unexpected
    except ssl.SSLError as e:
        print(f"SSL Error (invalid cert): {e}")


    # Fuzzing with very large certificate data
    large_cert = os.urandom(1024 * 1024 * 10)  # Larger size - 10MB
    try:
        context.load_verify_locations(cadata=large_cert)
        # ... connection setup ... (placeholder for a connection method)
        print("Large certificate loaded successfully")  # Indicate success, unexpected
    except ssl.SSLError as e:
        print(f"SSL Error (large cert): {e}")
    
    #Fuzzing with None
    try:
        context.load_verify_locations(cadata=None)
        print("None certificate loaded successfully")
    except ssl.SSLError as e:
        print(f"SSL Error (None): {e}")
except ssl.SSLError as e:
    print(f"SSL Error: {e}")


# Fuzzing example for dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'
    db['key2'] = b'\x00\x01\x02'  # Add a binary key to test
    db['key3'] =  [1,2,3]   #test with list as value
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
    def __repr__(self):
        return f"ReplaceableClass(a={self.a}, b={self.b})"

try:
    rc = ReplaceableClass(1, 2)
    rc2 = copy.copy(rc).__replace__(a=3, b=4)
    print(rc)
    print(rc2)
    rc3 = copy.copy(rc).__replace__() #Test with no arguments
    print(rc3)


except Exception as e:
    print(f"Copy replace error: {e}")



# Example with potential race conditions
try:
    data_race = [random.randint(1, 100) for _ in range(100)]
    result_race = race_condition_test(data_race)
    print(f"Race condition result: {result_race}")
except Exception as e:
    print(f"Race condition error: {e}")

# Example with complex annotations - fuzzing different data types
try:
    complex_data = [1, 2, "hello", 4, "world", None, [], {}, True, 1.5, "test", "another string", 1000000000, "verylongstring", 1234567890,object(), "invalid string", 12345.6789, [], [1, 2, "test",], [1,2, {"a": 1}]]
    result_annotation = complex_annotation_test(complex_data)
    print(f"Annotation result: {result_annotation}")
except Exception as e:
    print(f"Annotation error: {e}")



# Example using jit_test_function
try:
    input_list = [random.randint(-100, 100) for _ in range(10000)]
    output = jit_test_function(input_list)
    print(f"JIT result: {output}")
except Exception as e:
    print(f"JIT error: {e}")


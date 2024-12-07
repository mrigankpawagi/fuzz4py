
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import functools
import random

def worker(data):
    for _ in range(10000):
        data += random.randint(-5, 5)  # Introduce randomness
    return data

def multithreaded_example(data_list):
    threads = []
    results = []
    for data in data_list:
        thread = threading.Thread(target=worker, args=(data,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    for i in range(len(data_list)):
        try:
            results.append(threading.get_ident())
        except RuntimeError as e:
            print(f"Error getting thread ID: {e}")
            results.append("Error")
    return results


def complex_annotation_example(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    results = []
    for item in data:
        if isinstance(item, int):
            results.append(item * 2)
        elif isinstance(item, str):
            try:
                results.append(int(item) * 3)
            except ValueError:
                results.append(-1)  # Handle error, don't return empty list
    return results

# Simulate using dbm.sqlite3 (fuzzing with more data types)
try:
    db = dbm.sqlite3.open('test.db', 'c')
    db['key'] = 'value'
    db['key2'] = 123
    db['key3'] = 3.14
    db['key4'] = True
    db['key5'] = b"binary data"
    db['key6'] = None
    db['key7'] = {'nested': 'dict'}
    db['key8'] = [1, 2, 3]
    db.close()
except Exception as e:
  print(f"Error interacting with dbm.sqlite3: {e}")



# Fuzzing `os` module timer functions (fuzzing with different flags)
try:
    start_time = time.perf_counter()
    os.times(random.randint(1,10))  # random time
    end_time = time.perf_counter()
    print(f"OS time elapsed: {end_time - start_time:.4f}")
except Exception as e:
    print(f"Error in timer fuzzing: {e}")

# Fuzzing `ssl.create_default_context()` (more comprehensive)
try:
    context = ssl.create_default_context()
    # Trying to load invalid certs
    try:
        context.load_verify_locations(cafile="invalid_ca.crt")
    except Exception as e:
        print(f"Error loading invalid CA: {e}")
    print("Default SSL context created successfully.")
except Exception as e:
    print(f"Error in ssl context fuzzing: {e}")


# Demonstrate copy.replace() (fuzzing with different input types and error cases)
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __replace__(self, a=None, b=None):
        return MyClass(a if a is not None else self.a, b if b is not None else self.b)


try:
  obj = MyClass(1,2)
  replaced_obj = copy.replace(obj, a="invalid")  # Try a string
  print(replaced_obj.a, replaced_obj.b)
except Exception as e:
  print(f"Error in copy.replace fuzzing: {e}")

# Example using complex annotations and exceptions.
data = [1, 2, "3", "abc", "def"] # Added more strings
result = complex_annotation_example(data)
print(result)

#Multithreaded example (more comprehensive)
data_list = [1, 2, 3, 4, 5, "a", "b", 10000]
result_threads = multithreaded_example(data_list)
print(result_threads)


# ... (rest of the code remains the same)
# ...



import threading
import time
import copy
import os
import ssl
import dbm
import typing
import functools

def worker(data):
    # Simulate a potentially JIT-compiled hot loop
    for _ in range(10000):
        data = data + 1
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
        results.append(threading.get_ident())
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
                # Handle non-convertible strings
                return []
    return results

# Simulate using dbm.sqlite3
try:
    db = dbm.sqlite3.open('test.db', 'c')
    db['key'] = 'value'
    db.close()
except Exception as e:
  print(f"Error interacting with dbm.sqlite3: {e}")



# Fuzzing `os` module timer functions
try:
    start_time = time.perf_counter()
    os.times()
    end_time = time.perf_counter()
    print(f"OS time elapsed: {end_time - start_time:.4f}")
except Exception as e:
    print(f"Error in timer fuzzing: {e}")

# Fuzzing `ssl.create_default_context()`
try:
    context = ssl.create_default_context()
    print("Default SSL context created successfully.")
except Exception as e:
    print(f"Error in ssl context fuzzing: {e}")

# Demonstrate copy.replace() (using a custom class)
class MyClass:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __replace__(self, a=None, b=None):
    return MyClass(a if a is not None else self.a, b if b is not None else self.b)


try:
  obj = MyClass(1,2)
  replaced_obj = copy.replace(obj, a=3)
  print(replaced_obj.a, replaced_obj.b)
except Exception as e:
  print(f"Error in copy.replace fuzzing: {e}")


# Example using complex annotations and exceptions.
data = [1, 2, "3", "abc"]
result = complex_annotation_example(data)
print(result)  # Output should be [2, 4, 9] or an empty list

# Multithreaded example
data_list = [1, 2, 3, 4, 5]
result_threads = multithreaded_example(data_list)
print(result_threads)

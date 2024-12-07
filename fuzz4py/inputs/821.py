
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


def my_function(data: typing.List[int]) -> int:
    """
    This function demonstrates a potential race condition.
    """
    total = 0
    for i in data:
        try:
            total += i
        except (TypeError, ValueError):  # Catch ValueError as well
            return "Error: Non-numeric type encountered."
    return total


def test_replace_protocol(obj):
  """
  Demonstrates the use of copy.replace()
  """
  try:
    return copy.copy(obj)  # Use copy to avoid modifying original
  except (TypeError, AttributeError) as e:  # Catch more general errors
    return f"Error: {e}"


def fuzz_dbm():
    """
    Fuzzes dbm.sqlite3, adding potentially malformed data.
    """
    try:
        db = dbm.open("mydatabase", 'c')
        db['key1'] = "value1"
        db['key2'] = "a very long string" * 1000
        db['key3'] = ""
        db['key4'] = None
        db['key5'] = b"binary data"
        db['key6'] = 123
        db['key7'] = 3.14
        db['key8'] = True
        db['key9'] = {'nested': 'dict'}
        db['key10'] = [1, 2, 3]
        try:
          data = db['key2']
        except KeyError as e:
          return f"Error: {e}"  # More specific error message
        db.close()
        return "dbm fuzzing successful"
    except (dbm.error, OSError) as e:
        return f"Error during dbm fuzzing: {e}"
    except Exception as e:  # Handle any other potential exceptions
        return f"Error during dbm fuzzing: {e}"

def fuzz_ssl():
    """
    Fuzzes ssl module.
    """
    try:
        ctx = ssl.create_default_context()
        try:
            ctx.load_verify_locations(cafile="invalid_ca.crt")
        except FileNotFoundError:
            print("invalid_ca.crt not found, skipping SSL verification load")
        except Exception as e:
            return f"Error loading CA: {e}"
        return "SSL fuzzing successful"
    except Exception as e:
        return f"Error during SSL fuzzing: {e}"

# Fuzzing with varying inputs
data1 = list(range(1000))
data2 = [1] * 10000
data3 = [-1] * 500 + [1] * 500
data4 = []
data5 = [1, 2, "3"]  # Type error input
data6 = [1,2,3,4,5,6,7,8,9,0]
data7 = [1,2,3,"a", "b", "c"]

results = []
threads = [
    threading.Thread(target=my_function, args=(data1,)),
    threading.Thread(target=my_function, args=(data2,)),
    threading.Thread(target=my_function, args=(data3,)),
    threading.Thread(target=my_function, args=(data4,)),
    threading.Thread(target=my_function, args=(data5,)),
    threading.Thread(target=my_function, args=(data6,)),
    threading.Thread(target=my_function, args=(data7,))
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

result_replace_list = test_replace_protocol([1, 2, 3])
print(f"Result of copy.copy() on list: {result_replace_list}")
result_replace_tuple = test_replace_protocol((1, 2, 3))
print(f"Result of copy.copy() on tuple: {result_replace_tuple}")
result_replace_str = test_replace_protocol("hello")
print(f"Result of copy.copy() on string: {result_replace_str}")

dbm_result = fuzz_dbm()
print(f"Result of dbm fuzzing: {dbm_result}")

ssl_result = fuzz_ssl()
print(f"Result of SSL fuzzing: {ssl_result}")


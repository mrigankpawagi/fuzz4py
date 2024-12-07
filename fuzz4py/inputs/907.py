
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random


def my_function(data: typing.List[int], sleep_time: float) -> None:
    """
    This function demonstrates threading and database operations.
    """
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        for i in data:
            # Robust handling of potential errors, including non-string values
            try:
                db[str(i)] = str(i * 2 + random.randint(-100, 100))
            except Exception as e:
                print(f"Error writing to database for key {i}: {e}")
        db.close()
    except (dbm.error, Exception) as e:  # More specific exception handling
        print(f"Database error: {e}")

    time.sleep(sleep_time)
    local_var = 10
    local_var2 = [1, 2, 3]
    print(f"Local var in thread: {local_var}, {local_var2}, {type(local_var2)}")


def main():
    data = list(range(1000))
    threads = []
    for i in range(5):
        sleep_time = float(i) / 2
        t = threading.Thread(target=my_function, args=(copy.deepcopy(data), sleep_time))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads finished.")

# Separate the fuzzing parts to improve clarity
if __name__ == "__main__":
    main()

# Fuzzing for free-threading (PEP 703)
shared_data = {}
num_threads = 5

def worker(arg):
    global shared_data
    time.sleep(random.random() * 0.5)
    try:
        shared_data[arg] = shared_data.get(arg, 0) + random.randint(-10, 10)
    except Exception as e:
        print(f"Error in worker thread {arg}: {e}")

threads = []
for i in range(num_threads):
    x = threading.Thread(target=worker, args=(i,))
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()

print(f"Shared data: {shared_data}")

# Fuzzing for JIT compiler (PEP 744)
def jit_test(n: int) -> int:
    result = 0
    for i in range(n):
        try:
            result += i * 2 + random.randint(-100, 100)
        except Exception as e:
          print(f"Error in jit_test loop {i}: {e}")
    return result


print(jit_test(1000000))

# Fuzzing os module timer functions
try:
    start_time = time.perf_counter()
    res = os.times()
    end_time = time.perf_counter()
    print(f"Time taken for os.times() (perf_counter): {end_time - start_time:.6f}")
    print(res)

    start_time = time.process_time()
    res = os.times()
    end_time = time.process_time()
    print(f"Time taken for os.times() (process_time): {end_time - start_time:.6f}")
    print(res)
    # Fuzzing with invalid flags and types.  More robust error handling.
    try:
        os.times(10)
    except TypeError as e:
        print(f"Error when calling os.times with extra arguments (TypeError): {e}")
    except Exception as e:
        print(f"Error when calling os.times with extra arguments (other error): {e}")


except OSError as e:
    print(f"Error in os.times(): {e}")

# Fuzzing dbm.sqlite3 - more robust testing
try:
    db = dbm.sqlite3.open('mydatabase2', 'c')
    db['key1'] = 'value1'
    db['key2'] = b'\x00\x01\x02\x03'
    db['key3'] = None
    db.close()
except (dbm.error, Exception) as e:
    print(f"Error with dbm.sqlite3: {e}")

# Fuzzing complex type annotations
def process_data(data: typing.List[typing.Union[int, str, float, bool, type(None), list, dict]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
            try:
                result.append(int(item))
            except ValueError:
                pass
        elif isinstance(item, float):
            result.append(int(item))
        elif item is None:
            result.append(0)
        else:
            pass  # Ignore other types
    return result

fuzz_data = [1, 2, "3", "abc", 5, "10.5", "invalid", "", "12345678901234567890", None, 3.14, True, False, [], {}]
result = process_data(fuzz_data)
print(f"Processed data: {result}")

# Fuzzing copy.replace() - more comprehensive testing (using try...except)
try:
    class MyReplaceable:
        def __init__(self, value):
            self.value = value
        def __replace__(self, **kwargs):
            if 'value' in kwargs:
                try:
                    self.value = kwargs['value']
                except Exception as e:
                    print(f"Error in __replace__: {e}")
            return self

    obj = MyReplaceable(10)
    new_obj = copy.replace(obj, value=20)
    print(f"Original object: {obj.value}, New object: {new_obj.value}")
    try:
        new_obj2 = copy.replace(obj, value="new value")
    except Exception as e:
        print(f"Error during replace with string: {e}")


except Exception as e:
    print(f"Error in copy.replace(): {e}")



try:
    context = ssl.create_default_context()
    print("SSL context created successfully")
except ssl.SSLError as e:
    print(f"SSL error: {e}")



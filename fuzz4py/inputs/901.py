
import threading
import time
import copy
import os
import ssl
import dbm
import typing

# Fuzzing for free-threading (PEP 703)
def worker(arg):
    global shared_data
    time.sleep(0.1)
    shared_data[arg] += 1  # Potential race condition if not properly protected
    return

shared_data = {}
num_threads = 5

# Create and run threads
threads = []
for i in range(num_threads):
    x = threading.Thread(target=worker, args=(i,))
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()

# Fuzzing for JIT compiler (PEP 744)
def jit_test(n: int) -> int:
    result = 0
    for i in range(n):
        result += i * 2  # Likely JIT candidate, highly repetitive
    return result


# Fuzzing os module timer functions
try:
    start_time = time.perf_counter()
    res = os.times()
    end_time = time.perf_counter()
    print(f"Time taken for os.times(): {end_time - start_time:.6f}")
    print(res)

    start_time = time.process_time()
    res = os.times()
    end_time = time.process_time()
    print(f"Time taken for os.times(): {end_time - start_time:.6f}")
    print(res)

except OSError as e:
    print(f"Error in os.times(): {e}")



# Fuzzing dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c')  # Create a new database
    db['key1'] = 'value1'
    db.close()
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")



# Fuzzing complex type annotations
def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
            try:
                result.append(int(item))
            except ValueError:
                pass  # Handle cases where string cannot be converted
    return result




# Fuzzing copy.replace() - placeholder (needs actual implementation)
try:
    class MyReplaceable:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **kwargs):
            if 'value' in kwargs:
                self.value = kwargs['value']
            return self

    obj = MyReplaceable(10)
    new_obj = copy.replace(obj, value=20)  # Fuzzing replace protocol
    print(f"Original object: {obj.value}, New object: {new_obj.value}")

except Exception as e:
    print(f"Error in copy.replace(): {e}")


#Example using ssl.create_default_context()
try:
    context = ssl.create_default_context()
    print("SSL context created successfully")
except ssl.SSLError as e:
    print(f"SSL error: {e}")



import threading
import time
import copy
import dbm
import os
import ssl
import typing

def my_function(data: typing.List[int], sleep_time: float) -> None:
    """
    This function demonstrates threading and database operations.
    """

    # Accessing the GIL (in this case, a simulated GIL)
    # Simulate a database operation
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        for i in data:
            db[str(i)] = str(i * 2)
        db.close()

    except Exception as e:
        print(f"Database error: {e}")


    # Simulate a function that takes a variable amount of time
    time.sleep(sleep_time)

    # Testing local variables
    local_var = 10
    local_var2 = [1, 2, 3]
    print(f"Local var in thread: {local_var}, {local_var2}")

def main():
    data = list(range(1000))

    # Create threads
    threads = []
    for i in range(5):
        sleep_time = float(i) / 2  # Vary sleep time
        t = threading.Thread(target=my_function, args=(copy.deepcopy(data), sleep_time))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()


# Fuzzing for free-threading (PEP 703)
shared_data = {}
num_threads = 5

def worker(arg):
    global shared_data
    time.sleep(0.1)
    shared_data[arg] = shared_data.get(arg, 0) + 1
    return

# Create and run threads
threads = []
for i in range(num_threads):
    x = threading.Thread(target=worker, args=(i,))
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()

print(f"Shared data: {shared_data}")  # Output the results

# Fuzzing for JIT compiler (PEP 744)
def jit_test(n: int) -> int:
    result = 0
    for i in range(n):
        result += i * 2
    return result

# Example usage of jit_test (with fuzzing input)
print(jit_test(1000000))


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
    db = dbm.open('mydatabase', 'c')
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
                pass
    return result

fuzz_data = [1, 2, "3", "abc", 5, "10.5"]  # Fuzzing with varied data types and values
result = process_data(fuzz_data)
print(f"Processed data: {result}")


# Fuzzing copy.replace()
try:
    class MyReplaceable:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **kwargs):
            if 'value' in kwargs:
                self.value = kwargs['value']
            return self

    obj = MyReplaceable(10)
    new_obj = copy.replace(obj, value=20)
    print(f"Original object: {obj.value}, New object: {new_obj.value}")

except Exception as e:
    print(f"Error in copy.replace(): {e}")


#Example using ssl.create_default_context()
try:
    context = ssl.create_default_context()
    print("SSL context created successfully")
except ssl.SSLError as e:
    print(f"SSL error: {e}")

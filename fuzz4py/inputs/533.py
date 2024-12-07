
import threading
import copy
import os
import ssl
import time
import sqlite3
import typing
import random

# Fuzzing for free-threading (PEP 703)
def worker(data):
    try:
        time.sleep(0.1 * random.random())  # Introduce random sleep times
        print(f"Thread {threading.get_ident()} processed: {data}")
        return data
    except Exception as e:
        print(f"Error in worker thread: {e}")


def free_threading_fuzzer():
    data = [1, 2, 3]
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data),))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Fuzzing for JIT compiler (PEP 744)
def jit_fuzzer(n):
    result = 0
    for i in range(n):
        result += random.randint(-100, 100)  # Fuzz with random numbers
    return result

# Fuzzing for docstring whitespace stripping
def my_function(a: int, b: int) -> int:
    """
        This function
        calculates the sum
        of two numbers
    """
    return a + b


# Fuzzing copy.replace()
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        return Point(x if x is not None else self.x, y if y is not None else self.y)


# Fuzzing dbm.sqlite3
def dbm_fuzzer():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")
    
    # Fuzzing with various data types
    values_to_insert = [
        "fuzzed data", 
        b"fuzzed binary data",
        123, 
        123.456,
        True, 
        None,
        'a\n"quoted"string',
        [1, 2, 3],
        {"key": "value"},
        (1, 2, 3),
        #More complex data types
        {"nested": [1, 2]},
        {"empty": {}},
        [],
        (),
        bytearray(b'binary'),
        # Test with a large string
        "a" * 10000

    ]
   
    for value in values_to_insert:
      try:
        cursor.execute("INSERT INTO data (value) VALUES (?)", (value,))
      except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    conn.commit()
    conn.close()


# Fuzzing os module timer functions
def os_timer_fuzzer():
    start_time = time.perf_counter()
    try:
        os.times()
    except OSError as e:
        print(f"Error in os.times(): {e}")
    end_time = time.perf_counter()
    print(f"Time taken by os.times(): {end_time-start_time}")


# Fuzzing ssl.create_default_context()
def ssl_fuzzer():
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    
# Fuzzing annotation scopes (more robust example)
def annotated_function(a: typing.List[int]) -> int:
    try:
        return sum(a)
    except TypeError as e:
        print(f"Error in annotated_function: {e}")
    return 0


# Example usage (calling the fuzzers, with random data for fuzzing):
free_threading_fuzzer()
jit_fuzzer(random.randint(1000, 10000))  # Random range for jit_fuzzer
print(my_function(random.randint(1, 10), random.randint(1, 10)))
p = Point(random.randint(1, 10), random.randint(1, 10))  # Random coordinates
print(p.__replace__(x=random.randint(1, 10)))
dbm_fuzzer()
os_timer_fuzzer()
ssl_fuzzer()
annotated_function([random.randint(1, 10) for _ in range(random.randint(1, 5))])  # Random list length



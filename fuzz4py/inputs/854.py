
import threading
import time
import os
import copy
import dbm

# Fuzzing code for free-threading (PEP 703) and JIT compiler (PEP 744)
def worker(arg):
    x = arg * 2
    time.sleep(0.01)
    return x

def threaded_operation(n):
    threads = []
    results = []
    for i in range(n):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return results


# Fuzzing code for docstring whitespace stripping (and potential JIT compilation)
def example_func(a, b):
    """This docstring has varying whitespace."""
    return a + b


# Fuzzing code for complex type annotations and __static_attributes__
class MyClass:
    __static_attributes__ = {'a': 1, 'b': 'hello'}
    
    def __init__(self, arg: int | str | list[int], num: int = 1) -> None:
        self.arg = arg
        self.num = num

# Fuzzing code for dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'  # Fuzz with different key/value lengths
    db['key2'] = bytes([i for i in range(256)]) # Test with various bytes
    db.close()
    db = dbm.open('mydatabase', 'r')
    value = db.get('key1')
    db.close()
except Exception as e:
    print(f"Error with dbm: {e}")


# Fuzzing code for copy.replace()
class Replaceable:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __replace__(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        return self


r1 = Replaceable(10, 20)
r2 = copy.replace(r1, a=30) # Fuzzing with different inputs
print(r1.a, r1.b)
print(r2.a, r2.b)


# Example of a function likely to be JIT compiled
def hot_loop(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


# Fuzzing for os module timer functions (Replace with specific calls)
try:
    start_time = time.perf_counter()
    result = os.times() # Fuzzing with different time values
    end_time = time.perf_counter()
    print(f"OS times: {result}, Time taken: {end_time - start_time}")
except Exception as e:
    print(f"Error with os.times(): {e}")

# Run threaded operation with varying numbers of threads
threaded_operation(10)
# Execute a potentially JIT-compiled function.  Vary input to uncover edge cases.
print(hot_loop(100000))



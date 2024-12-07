
import threading
import time
import copy
import os
import ssl
import dbm

# Fuzzing free-threading and GIL
def worker(data):
    global counter
    for _ in range(10):
        counter += data
        time.sleep(0.001)
    return counter

def test_free_threading():
    global counter
    counter = 0
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    return counter

# Fuzzing JIT compiler (using a potential hot loop)
def jit_fuzzer(n):
    sum = 0
    for i in range(n):
        sum += i * 2 
    return sum

# Fuzzing docstring whitespace stripping
def my_function():
    """This is a docstring
    with varying whitespace.
    """
    return "test"


# Fuzzing complex type annotations (PEP 696, 702, 705, 742)
from typing import List, Tuple, Generic, TypeVar
T = TypeVar('T')

class MyClass(Generic[T]):
    def __init__(self, data: List[Tuple[T, T]]):
        self.data = data
        
# Fuzzing replace protocol
class MyReplaceableClass(copy.Replacer):
    def __replace__(self, obj):
        if isinstance(obj, list):
          return [x * 2 for x in obj]
        return obj


# Fuzzing dbm.sqlite3
try:
    db = dbm.open('test.db', 'c')
    db['key'] = 'value'
    db.close()
    db = dbm.open('test.db', 'r')
    data = db['key']
    db.close()
except Exception as e:
    print(f"Error accessing dbm.sqlite3: {e}")
    

# Fuzzing timer functions (os module)
try:
  start_time = time.perf_counter()
  result = os.times()
  end_time = time.perf_counter()
  print(f"Time taken: {end_time - start_time}")
except Exception as e:
    print(f"Error accessing os timer: {e}")

# Fuzzing SSL connections
try:
    context = ssl.create_default_context()
    # ...(omitting actual SSL connection code for brevity, focus is on context)
    print("SSL connection attempted (fuzzing context)")
except Exception as e:
    print(f"Error creating default SSL context: {e}")


# Example usage (for different parts)
test_free_threading()
print(jit_fuzzer(100000)) # Example of large input for JIT fuzzing
print(my_function.__doc__) # test docstring whitespace


# Demonstrate use of complex annotations
my_data = [(1, 2), (3, 4)]
obj = MyClass(my_data)
print(obj.data)

#Example for replace protocol:
my_list = [1, 2, 3]
new_list = MyReplaceableClass().__replace__(my_list)
print(new_list)



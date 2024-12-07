
import threading
import time
import copy
import os
import ssl
import dbm
import socket
import typing

def threaded_function(arg):
    # Simulate some work, potentially using C extensions.
    time.sleep(0.1)
    # Demonstrating modification of a shared resource
    global shared_data
    shared_data += arg


def main():
    global shared_data
    shared_data = 0

    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    try:
        # Demonstrating copy.replace()
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __replace__(self, **kwargs):
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']
                return self
        
        p1 = Point(1, 2)
        p2 = copy.replace(p1, x=10)
        assert p1.x == 1
        assert p2.x == 10
        
        # Use of annotations:
        def my_function(arg: typing.List[int]) -> int:
            return sum(arg)
    
        my_list = [1, 2, 3]
        result = my_function(my_list)
        print(f"Result: {result}")

    except Exception as e:
        print(f"Exception caught in main: {e}")


    # Demonstrating os.timer functions (using monotonic for example)
    start_time = time.monotonic()
    time.sleep(0.5)
    end_time = time.monotonic()
    print(f"Time elapsed (monotonic): {end_time - start_time}")
    # Adding ssl for demonstration of new default flags
    try:
        context = ssl.create_default_context()
        # Replace with your actual certificate if you have one
        with context.wrap_socket(socket.socket(), server_hostname='localhost'):
            print("SSL connection successful")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    
# Fuzzing with free-threading (PEP 703)
def thread_func(x):
    global shared_var
    time.sleep(0.1)
    shared_var += x

shared_var = 0
threads = []
for i in range(5):
    t = threading.Thread(target=thread_func, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Fuzzing with JIT compiler (PEP 744) - focus on a tight loop
def jit_test(n):
    sum_val = 0
    for i in range(n):
        sum_val += i * 2
    return sum_val

# Example with large input to trigger JIT
result = jit_test(100000)
print(f"JIT result: {result}")



# Fuzzing dbm.sqlite3
try:
    db = dbm.open('test.db', 'c')
    db['key1'] = 'some data'
    db['key2'] = 'some_more_data'
    db.close()
    
    db = dbm.open('test.db', 'r')
    data1 = db['key1']
    data2 = db['key2']
    db.close()
    print(f"Retrieved data1: {data1}, data2: {data2}")
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")


# Fuzzing os module timer functions
try:
    start_time = time.perf_counter()
    os.sched_yield() #Testing os.sched_yield
    end_time = time.perf_counter()
    print(f"Time taken by sched_yield: {end_time - start_time:.6f} seconds")
except Exception as e:
    print(f"Error with os.sched_yield: {e}")



#Fuzzing ssl.create_default_context() -  (Simplified example)
try:
    context = ssl.create_default_context()
    print("SSL context created successfully.")
except Exception as e:
    print(f"Error creating SSL context: {e}")



# Example of complex type annotation (PEP 696 etc.)
from typing import List, Tuple, Union

def complex_function(data: Union[List[int], Tuple[str, float]]) -> int:
  if isinstance(data, list):
    return sum(data)
  elif isinstance(data, tuple):
    return int(data[1])
  else:
    return 0

# Test cases
print(complex_function([1, 2, 3]))  # Output: 6
print(complex_function(('abc', 4.5))) # Output: 4
print(complex_function(123)) # Output: 0

if __name__ == "__main__":
    main()

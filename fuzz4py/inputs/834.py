
import threading
import time
import copy
import os
import ssl
import dbm
import socket
import typing
import random

shared_data = 0
shared_var = 0

def threaded_function(arg):
    global shared_data
    time.sleep(random.uniform(0.05, 0.15))
    try:
        shared_data += arg
        shared_data += arg*2
        if isinstance(arg, str):
          shared_data += int(arg)
    except (TypeError, ValueError) as e:
        print(f"Caught exception in threaded_function: {e}")
    if random.random() < 0.1:
        raise ValueError("Simulated error in thread")
    try:
        shared_data += float(arg)
    except ValueError:
        print("Could not convert arg to float")


def main():
    global shared_data
    shared_data = 0

    threads = []
    num_threads = random.randint(3, 7)
    for i in range(num_threads):
        t = threading.Thread(target=threaded_function, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Shared data after threads: {shared_data}")


    try:
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
        p2 = copy.replace(p1, x=random.randint(5, 15))
        p3 = copy.replace(p1, y="not an int") # testing non int
        assert p1.x == 1
        assert p2.x == p2.x

        def my_function(arg: typing.List[int]) -> int:
            try:
                return sum(arg)
            except TypeError as e:
                print(f"Caught TypeError in my_function: {e}")
                return 0  # Or handle differently
        
        my_list = [1, 2, 3]
        result = my_function(my_list)
        print(f"Result: {result}")

        try:
            result = my_function("not a list")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        try:
            result = my_function([1,2,"3"]) #bad input
        except TypeError as e:
            print(f"Caught TypeError: {e}")


    except Exception as e:
        print(f"Exception caught in main: {e}")


    start_time = time.monotonic()
    time.sleep(random.uniform(0.3, 0.7))
    end_time = time.monotonic()
    print(f"Time elapsed (monotonic): {end_time - start_time}")
    
    try:
        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH) #adding purpose for robustness
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            print("SSL connection successful")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    
def thread_func(x):
    global shared_var
    time.sleep(random.uniform(0.05, 0.15))
    shared_var += x
    if random.random() < 0.2:
        shared_var = 0
        
def jit_test(n):
    sum_val = 0
    for i in range(n):
        sum_val += i * 2
    return sum_val


result = jit_test(100000)
print(f"JIT result: {result}")


try:
    db_name = 'test' + str(random.randint(1, 100)) + '.db'
    db = dbm.open(db_name, 'c')
    db['key1'] = 'some data'
    db['key2'] = 'more data'
    db.close()
    db = dbm.open(db_name, 'r')
    data1 = db['key1']
    data2 = db['key2']
    db.close()
    os.remove(db_name)
    print(f"Retrieved data1: {data1}, data2: {data2}")
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")


try:
    start_time = time.perf_counter()
    os.sched_yield()
    end_time = time.perf_counter()
    print(f"Time taken by sched_yield: {end_time - start_time:.6f} seconds")
except Exception as e:
    print(f"Error with os.sched_yield: {e}")


# Example of complex type annotation (PEP 696 etc.)
from typing import List, Tuple, Union

def complex_function(data: Union[List[int], Tuple[str, float]]) -> int:
  if isinstance(data, list):
    return sum(data)
  elif isinstance(data, tuple):
    return int(data[1])
  else:
    return 0

print(complex_function([1, 2, 3]))
print(complex_function(('abc', 4.5)))
print(complex_function(random.randint(1000, 10000)))


if __name__ == "__main__":
    main()


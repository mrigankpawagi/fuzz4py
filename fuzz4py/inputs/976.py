
import threading
import copy
import dbm
import os
import ssl
import time
import typing
import socket


def worker(data: typing.List[int], lock: threading.Lock, db: dbm.sqlite3):
    """
    A worker thread that modifies shared data and the database.
    """
    for i in data:
        lock.acquire()
        try:
            # Simulate a database update (potentially race condition)
            db[str(i)] = str(i * 2)
            # Simulate some work...
            os.times()
        finally:
            lock.release()
    # Example of a complex annotation
    assert isinstance(data, typing.List[int])
    return 1


def main():
    # Test data
    data = list(range(10))
    # Initialize shared resources
    lock = threading.Lock()
    # Example of a dynamically created database
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
    except Exception as e:
        print(f"Error opening database: {e}")
        return
    
    threads = []
    for i in range(5):
        thread_data = copy.deepcopy(data)  # Important for each thread to get a copy
        thread = threading.Thread(target=worker, args=(thread_data, lock, db))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    # Cleanup
    try:
        db.close()
    except Exception as e:
        print(f"Error closing database: {e}")


def jit_target_function(input_list):
    """
    A function likely to be JIT-compiled, with a hot loop.
    """
    result = 0
    for i in input_list:
        result += i
    return result


def threaded_function(input_data, thread_id):
    """
    A function likely to be executed in a thread.
    """
    result = jit_target_function(input_data)
    time.sleep(0.01)
    print(f"Thread {thread_id}: Result {result}")
    return result


def fuzz_replace_protocol(data):
    """
    Fuzzing the copy.replace() feature
    """
    try:
        return copy.replace(data)
    except Exception as e:
        print(f"Error replacing data: {e}")
        return None


# Example usage with different types and threads
data = [1, 2, 3, 4, 5]  # Test different kinds of data
threads = []
for i in range(5):
    t = threading.Thread(target=threaded_function, args=(data, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


# Fuzzing replace protocol for a custom object:
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __replace__(self, a=None, b=None):
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        return self


try:
    my_obj = MyClass(10, 20)
    fuzz_replace_protocol(my_obj)
except Exception as e:
    print(f"Error with custom object replace: {e}")



#Example fuzzing ssl
try:
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
        s.connect(('example.com', 443))
        s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        response = s.recv(4096)
        print(response.decode())  # decode for readability
except Exception as e:
    print("Error with ssl connection:", e)


# Example fuzzing os timer functions (replace with actual usage)
try:
    start_time = time.perf_counter()
    result = os.times()
    end_time = time.perf_counter()
    print(result)
except Exception as e:
    print(f"Error with os timer: {e}")


#example annotation
def func(arg: typing.List[int]) -> int:
    return sum(arg)


# --- Added code from the second program ---
import threading
import time
import copy
import dbm
import os
import ssl
import typing


def worker(data: typing.List[int], index: int, lock):
    try:
        lock.acquire()
        data[index] += 1
        lock.release()
    except IndexError:
        print("IndexError caught in worker thread")
    except Exception as e:
        print(f"Worker thread {index} failed: {e}")
    

def main_second(): # Changed function name for clarity
    data = [0] * 10
    lock = threading.Lock()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(data, i, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(data)


    # Example of using copy.replace() (Note: This is not the full fuzzing, but shows the syntax)
    class Point:
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y
        def __replace__(self,  x : int = None, y : int = None):
            return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)

    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=10)
    print(p1.x, p1.y) # Output: 1 2
    print(p2.x, p2.y) # Output: 10 2


    # Example of dbm.sqlite3 (Illustrative, not comprehensive)
    db = dbm.sqlite3.open('mydatabase', 'c')
    try:
        db['key1'] = 'value1'
        value = db['key1']
        print(value)
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    finally:
        db.close()



if __name__ == "__main__":
    main()
    main_second()

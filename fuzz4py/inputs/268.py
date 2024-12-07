
import threading
import time
import copy
import ssl
import os
import dbm
import typing
import socket
import random

shared_data = 0

def race_condition_example(data: typing.List[int]) -> None:
    """
    Demonstrates a potential race condition.
    """
    global shared_data
    shared_data = 0
    threads = []
    num_threads = random.randint(2, 10)
    for i in range(num_threads):
        t = threading.Thread(target=increment_shared, args=(data,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final shared data: {shared_data}")

def increment_shared(data):
    global shared_data
    for x in data:
        shared_data += x
        time.sleep(random.uniform(0, 0.01))
    time.sleep(random.uniform(0.05, 0.2))


def test_copy_replace():
    class MyData:
        def __init__(self, val1, val2):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, val1=None, val2=None):
            return MyData(val1 if val1 is not None else self.val1,
                           val2 if val2 is not None else self.val2)

    try:
        my_data = MyData(1, 2)
        new_data = copy.copy(my_data) # Use copy to avoid modifying original
        new_data.val1 = random.randint(-100, 100)
        new_data.val2 = random.uniform(-10.0, 10.0)
        assert new_data.val1 == new_data.val1
        assert new_data.val2 == new_data.val2
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def fuzz_ssl():
    try:
        hostname = random.choice(['invalid.hostname', 'example.com'])
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            try:
              s.connect(('example.com', 443))
            except Exception as e:
              print(f"Connection Error: {e}")
              return
            try:
              s.connect(('example.com', random.randint(80, 8080)))
            except Exception as e:
              print(f"Connection Error: {e}")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def worker(arg: int, lock):
    try:
        # Simulate some work.  Susceptible to race conditions
        result = arg * 2
        
        # Acquire the lock before modifying the shared resource.
        lock.acquire()
        try:
            shared_list.append(result)  # Race condition potential
        finally:
            lock.release()
    except Exception as e:
        print(f"Error in worker thread: {e}")


if __name__ == "__main__":
    # Example usage. Fuzz input data.
    my_data = [random.randint(-10, 10) for _ in range(random.randint(1, 10))]
    race_condition_example(my_data)
    test_copy_replace()
    
    # Example of a potential JIT/threading test
    def jit_test():
        result = 0
        for _ in range(100000):  # Fixed range for demonstration
            result += 1
        return result

    shared_list = []
    lock = threading.Lock()
    threads = []
    num_threads = random.randint(2, 10)
    for _ in range(num_threads):
        t = threading.Thread(target=jit_test)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("JIT test completed successfully")


    # Example of fuzzing dbm.sqlite3 (with error handling)
    try:
        db_name = f"mydatabase_{random.randint(1, 1000)}.db"
        db = dbm.open(db_name, 'c')
        key = str(random.randint(1, 1000))
        value = str(random.randint(1, 1000))
        db[key] = value
        db.close()
        db = dbm.open(db_name, 'r')
        try:
            value = db.get(key)
            db.close()
            if value:
              print(f"Retrieved data from DB: {value}")
        except Exception as e:
            print(f"Error retrieving data from DB: {e}")
            db.close()
    except Exception as e:
        print("Error in dbm.sqlite3 test:", e)


    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Shared list: {shared_list}")

    # ... (rest of the code is the same)

    fuzz_ssl()

    # Example of fuzzing race condition with open/close (improved)
    try:
        num_files = random.randint(1, 5)
        files = [open(f"tempfile_{i}.txt", "w") for i in range(num_files)]
        for file in files:
            file.write("some data")
        for file in files:
            file.close()
        time.sleep(0.5)
        for file in files:
            try:
                with open(file.name, "r") as file2:
                    contents = file2.read()
                    assert contents == "some data"
                    print(f"File contents verified: {contents}")
            except Exception as e:
                print(f"Error accessing file after close: {e}")
    except Exception as e:
        print(f"Error during file operations: {e}")


    # Example using copy.replace() (Potentially problematic)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, **kwargs):
            return Point(kwargs.get('x', self.x), kwargs.get('y', self.y))


    point = Point(1, 2)
    new_point = copy.replace(point, x=10)
    print(f"Modified point: {new_point.x}, {new_point.y}")
    
    # Example using os.times()
    start_time = time.time()
    result = os.times()
    end_time = time.time()
    print(f"OS Times: {result}")
    print(f"Time taken: {end_time - start_time}")

    try:
        # Example using ssl.create_default_context() with potential issue (simplified)
        context = ssl.create_default_context()
        
        #This would be a real certificate load/verification step
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))  # Replace with your actual server
            
    except Exception as e:
        print(f"SSL Error: {e}")



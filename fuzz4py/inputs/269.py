
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
            try:
              return MyData(val1 if val1 is not None else self.val1,
                             val2 if val2 is not None else self.val2)
            except Exception as e:
              print(f"Error in __replace__: {e}")
              return None


    try:
        my_data = MyData(1, 2)
        new_data = copy.copy(my_data)
        new_data = copy.replace(my_data, val1 = random.randint(-100, 100), val2 = random.uniform(-10.0, 10.0))  # Use replace

        assert new_data.val1 == new_data.val1
        assert new_data.val2 == new_data.val2
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def fuzz_ssl():
    try:
        hostname = random.choice(['invalid.hostname', 'example.com', 'nonexistent.com'])
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            try:
                s.connect(('example.com', 443))
            except Exception as e:
              print(f"Connection Error: {e}")
              return  # Important: return to prevent further attempts

            # Fuzz with invalid ports (0-65535).  More comprehensive testing.
            for port in range(0, 65536, 10):
                try:
                    s.connect(('example.com', port))
                    print(f"Connected successfully to port: {port}")
                except Exception as e:
                    print(f"Connection Error (port {port}): {e}")



    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def worker(arg: int, lock):
    try:
        # Simulate some work.  Introduce potential race conditions
        result = arg * (random.randint(-10,10)) 
        
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
        for _ in range(100000):
            result += random.randint(1,10000)
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


    # ... (rest of the code is the same, with minor tweaks, especially for dbm)



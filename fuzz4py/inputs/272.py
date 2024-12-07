
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
        # Introduce random sleep before starting threads
        time.sleep(random.uniform(0, 0.05))
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
    # Introduce a potentially problematic sleep duration
    time.sleep(random.uniform(0.05, 1))


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
        # Test with potentially invalid inputs
        new_data = copy.replace(my_data, val1=None, val2="invalid")
        assert new_data.val1 == 1
        assert new_data.val2 == "invalid"  # This would be an error if type checking
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def fuzz_ssl():
    try:
        hostname = random.choice(['example.com', 'nonexistent.com', 'invalid.hostname'])
        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH) # Added
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            try:
                # Introduce a random delay.  More extensive fuzzing required.
                time.sleep(random.uniform(0, 0.1))
                s.connect(('example.com', 443))
            except Exception as e:
                print(f"Connection Error: {e}")
                return
            
            # Fuzz with invalid ports (0-65535).  More comprehensive testing.
            for port in range(0, 65536, 10):
                try:
                    s.connect(('example.com', port))
                    print(f"Connected successfully to port: {port}")
                    time.sleep(0.01) # added for more comprehensive testing
                except Exception as e:
                    print(f"Connection Error (port {port}): {e}")

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def worker(arg: int, lock):
    try:
        # Simulate some work.  Introduce potential race conditions with more complex logic
        result = arg * (random.randint(-100, 100))
        
        lock.acquire()
        try:
            shared_list.append(result)  # Race condition potential
        finally:
            lock.release()
    except Exception as e:
        print(f"Error in worker thread: {e}")


if __name__ == "__main__":
    # Example usage. Fuzz input data with more varied data.
    my_data = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]
    race_condition_example(my_data)
    test_copy_replace()
    
    # Example of a potential JIT/threading test with random data, potentially causing jitter
    def jit_test():
        result = 0
        for _ in range(100000):
            result += random.randint(1, 100000)
        return result
    
    shared_list = []
    lock = threading.Lock()
    threads = []
    num_threads = random.randint(2, 10)
    for _ in range(num_threads):
        arg = random.randint(-1000, 1000)
        t = threading.Thread(target=worker, args=(arg, lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("JIT test completed successfully. Shared List:", shared_list)
    fuzz_ssl() # Added fuzz_ssl call


import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket
import random

def jit_test_function(input_list):
    """
    A function designed to be JIT-compiled, exhibiting a hot loop.
    """
    result = 0
    for i in input_list:
        result += i * random.random()  # Introduce randomness
    return result

def race_condition_example(data):
    """
    Illustrates a potential race condition.
    """
    global shared_data
    lock = threading.Lock()
    lock.acquire()
    try:
        shared_data += data * random.randint(1, 10)  # Random multiplier
    finally:
        lock.release()


def test_dbm():
    """Tests the dbm.sqlite3 module."""
    try:
        db = dbm.open('test.db', 'c')
        key = str(random.randint(1, 1000))  # Random key
        db[key] = str(random.randint(1, 1000))  # Random value
        value = db[key]
        db.close()
        os.remove('test.db')  # Clean up
    except Exception as e:
        print(f"Error during dbm operation: {e}")



def test_copy_replace(obj):
    """Tests the copy.replace() method"""
    try:
        new_obj = copy.replace(obj, value=random.randint(1, 100)) # Modify replace with random value
    except AttributeError as e:
        print(f"Error during replace: {e}")


def main():
    # Test free-threading with race conditions
    shared_data = 0
    threads = []
    for i in range(5):
        x = i * 10 + random.randint(-5, 5) # Add random offset
        t = threading.Thread(target=race_condition_example, args=(x,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Shared data: {shared_data}")
    
    # Test JIT compiler
    test_list = list(range(100000))
    start_time = time.time()
    result = jit_test_function(test_list)
    end_time = time.time()
    print(f"JIT Test result: {result}, Time taken: {end_time - start_time}s")

    # Test dbm module (with random data)
    test_dbm()

    # Test ssl module with default context. (More robust)
    try:
        ctx = ssl.create_default_context()
        # Try a connection with a random hostname
        hostname = "host" + str(random.randint(1, 100)) + ".com"
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            pass  # Expect an error, but this tests the setup
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

    # Test copy.replace,  replace needs a custom class that implements it.
    class ReplaceableClass:
        def __init__(self, value):
            self.value = value
        def __replace__(self, other=None):
            if other:
                self.value = other
            return self

    test_obj = ReplaceableClass(5)
    test_copy_replace(test_obj)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


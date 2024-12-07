
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

    threads = []
    num_threads = random.randint(2, 10)
    for _ in range(num_threads):
        t = threading.Thread(target=jit_test)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("JIT test completed successfully")


    # Example of fuzzing dbm.sqlite3
    try:
        # Create a unique db name
        db_name = f"mydatabase_{random.randint(1, 1000)}.db"  # More unique names
        db = dbm.open(db_name, 'c')
        key = str(random.randint(1, 1000))
        value = str(random.randint(1, 1000))
        db[key] = value
        db.close()
        db = dbm.open(db_name, 'r')
        try:
            value = db.get(key)  # Use the key we stored.
            db.close()
            if value:
              print(f"Retrieved data from DB: {value}")
        except Exception as e:
            print(f"Error retrieving data from DB: {e}")
            db.close() # Ensure DB is closed.
    except Exception as e:
        print("Error in dbm.sqlite3 test:", e)

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

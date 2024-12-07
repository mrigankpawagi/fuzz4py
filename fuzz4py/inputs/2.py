
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys


def my_custom_class(a: int, b: str = "default") -> typing.Tuple[int, str]:
    """
    A custom class for testing replace protocol.
    """
    return (a, b)


try:
    # Test free threading and the GIL
    def worker(i):
        global counter
        try:
            counter += i * random.randint(1, 100)  # Introduce random factors
        except Exception as e:
            print(f"Error in worker thread {i}: {e}")

    threads = []
    counter = 0
    for i in range(10):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Counter value: {counter}")
    


    # Test copy.replace() - fuzzing with potential errors
    obj = my_custom_class(5, "hello")
    new_obj = copy.copy(obj)
    try:
        new_obj = copy.replace(new_obj, a=10, b="fuzzed_string" * random.randint(1, 10))
    except Exception as e:
        print(f"Error with copy.replace(): {e}")

    print(f"Original object: {obj}")
    print(f"Replaced object: {new_obj}")

    # Test dbm.sqlite3 - fuzzing with malformed data and non-string keys
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()
        db = dbm.open('mydatabase')
        key = str(random.randint(0, 1000))
        value = db.get(key)
        if value:
            print(f"Value retrieved: {value}")

        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Test os module timer functions - fuzzing with non-numeric inputs
    try:
        start_time = time.perf_counter()
        try:
            result = os.times(random.randint(1, 100))
        except TypeError:
            result = os.times()

        end_time = time.perf_counter()
        print(f"Time taken by os.times(): {end_time - start_time}")
    except Exception as e:
        print(f"Error with os.times(): {e}")


    # Test ssl - fuzzing with invalid certificates (using a dummy placeholder)
    try:
        context = ssl.create_default_context()
        dummy_cert = b"DUMMY CERTIFICATE"  # Replace with a real invalid certificate
        context.load_verify_locations(cadata=dummy_cert)
        print("SSL Context Created (with fuzzed certificate)")

    except Exception as e:
        print(f"Error creating SSL context: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
    
    # Added cleanup to delete the database file
    try:
        os.remove('mydatabase')
    except Exception as e:
        print(f"Error deleting database file: {e}")
    

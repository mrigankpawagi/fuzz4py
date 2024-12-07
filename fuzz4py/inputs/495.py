
import threading
import time
import copy
import dbm.sqlite3
import os
import ssl
import typing
import random
import sys

def worker(data: typing.List[int]) -> None:
    """
    Demonstrates multi-threading issues and docstring whitespace.

    Args:
        data: A list of integers to process.
    """
    sleep_time = random.uniform(0.05, 0.15)
    time.sleep(sleep_time)  # Vary delay for fuzzing
    try:
        db_mode = random.choice(["c", "w", "n", "a", "r"])
        if random.random() < 0.1:
            db_mode = b"xyz"  # Try a bytes object
        db = dbm.sqlite3.open("test.db", db_mode)
        for i in data:
            try:
                value = i * random.randint(-100, 100)
                if random.random() < 0.1:
                    value = None
                if value is not None:
                    try:
                        if random.random() < 0.1:
                            db[str(i)] = b"some bytes"
                        elif random.random() < 0.1:
                            db[str(i)] = True  # Test boolean values
                        elif random.random() < 0.1:
                            db[str(i)] = 3.14159 # Test floats
                        elif random.random() < 0.1:
                            db[str(i)] = {"inner_key": "inner_value"} # Test dict
                        else:
                            db[str(i)] = str(value) # Test string representation.
                            # Attempt to write with incorrect encoding
                            db[str(i)] = str(value).encode("utf-16-le") if random.random() < 0.1 else str(value)
                    except Exception as e:
                        print(f"Error writing to database: {e}", file=sys.stderr)
            except Exception as e:
                print(f"Error processing data: {e}", file=sys.stderr)

        db.close()
    except Exception as e:
        print(f"Error in worker ({threading.current_thread().name}): {e}", file=sys.stderr)


def main():
    """Main function for testing."""
    data = list(range(10))
    threads = []
    num_threads = random.randint(3, 7)

    for i in range(num_threads):
        sub_list = [x for x in data if x % (i + 1) == 0]
        if not sub_list:
            continue
        t = threading.Thread(target=worker, args=(sub_list.copy(),))
        threads.append(t)
        try:
            t.start()
        except Exception as e:
            print(f"Error creating thread {i}: {e}", file=sys.stderr)

    for t in threads:
        t.join()

    print("All threads finished.")

    try:
      db = dbm.sqlite3.open("test.db", "r")
    except dbm.error as e:
      print(f"Error opening database: {e}", file=sys.stderr)
      sys.exit(1)

    for key in db:
        try:
            value = db[key]
            print(type(value))
            if not isinstance(value, (bytes, str, int, float, bool, type(None), dict)): # Allow more types
                print("Unexpected value type!", file=sys.stderr)
                continue
            print(f"Key: {key}, Value: {value}")
        except Exception as e:
            print(f"Error reading key {key}: {e}", file=sys.stderr)
    db.close()

    try:
        if os.path.exists("test.db"):
            os.remove("test.db")
    except OSError as e:
        print(f"Error removing database: {e}", file=sys.stderr)


import threading
import time
import copy
import os
import ssl
import dbm
import typing

def my_function(arg1: typing.List[int], arg2: int = 10) -> typing.Tuple[int, str]:
    """
    This function demonstrates various Python 3.13 features.
    """
    result = 0
    for i in arg1:
        result += i
    
    my_list = copy.copy(arg1)
    my_list.append(arg2)
    try:
        replaced_list = copy.replace(my_list, arg1)
    except Exception as e:
        return result, str(e)

    try:
        with dbm.open('test.dbm', 'c') as db:
            db['key1'] = str(result)
    except Exception as e:
        return result, str(e)


    for i in range(1000000):
        if i % 10 == 0:
            result += i

    try:
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE
    except Exception as e:
      return result, str(e)

    return result, "Success"



def threaded_function(data: typing.List[int], thread_id: int):
    global shared_result
    try:
        shared_result = my_function(data)[0] + shared_result
    except Exception as e:
        print(f"Error in threaded function {thread_id}: {e}", file=sys.stderr)



if __name__ == "__main__":
    shared_result = 0
    data = [1, 2, 3, 4, 5]
    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(data, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    print(f"Final Result: {shared_result}")



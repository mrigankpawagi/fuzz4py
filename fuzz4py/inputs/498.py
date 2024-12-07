
import threading
import time
import copy
import dbm.sqlite3
import os
import ssl
import typing
import random
import sys

def jit_test_function(arg1: int, arg2: str, arg3: typing.List[int]):
    """
    This function is designed to be JIT compiled.
    """
    result = 0
    for i in range(100000):
        result += arg1 * arg3[i % len(arg3)]
    return result

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


    # Fuzzing free-threading and JIT compiler (from first snippet)
    try:
        threads = []
        for i in range(5):
            thread = threading.Thread(target=jit_test_function, args=(i, "string_" + str(i), [j * 100 for j in range(10)]))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"Error in main thread: {e}")


    # Fuzzing docstring whitespace stripping (from first snippet)
    def test_docstring(arg:str):
        """Docstring example with
        some extra lines.
        """
        print(arg)

    test_docstring("Test")


    # Fuzzing copy.replace() (from first snippet)
    class ReplaceableClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, **changes):
            return ReplaceableClass(changes.get('a', self.a), changes.get('b', self.b))

    obj1 = ReplaceableClass(1, 2)
    obj2 = copy.replace(obj1, a=3)


    # Fuzzing os.timer (from first snippet)
    try:
        timer_result = os.times()
        print(f"OS times: {timer_result}")
    except Exception as e:
      print(f"Error with OS timer: {e}")


    # Fuzzing ssl.create_default_context() - requires a target certificate (from first snippet)
    try:
        context = ssl.create_default_context()
        # Replace with your actual certificate
        with open("my_certificate.pem", "rb") as f:
            cert = f.read()

        context.load_verify_locations(cadata=cert)

    except Exception as e:
        print(f"Error with SSL: {e}")



if __name__ == "__main__":
    main()


import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def jit_target_function(input_list: typing.List[int]) -> int:
    """
    A function designed to be JIT compiled.
    """
    total = 0
    for i in input_list:
        total += i
    return total

def test_free_threading():
    """Tests free-threading with potential race conditions."""
    shared_var = 0
    lock = threading.Lock()

    def incrementer(i: int):
        nonlocal shared_var
        with lock:
            try:
                shared_var += i
                time.sleep(random.uniform(0.001, 0.01))  # Vary delay
            except Exception as e:
                print(f"Error in incrementer: {e}")

    threads = [threading.Thread(target=incrementer, args=(i,)) for i in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return shared_var

def test_dbm_sqlite3():
    """Test dbm.sqlite3 module with varied data."""
    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1' * random.randint(1, 100)  # Vary data size
        db['key2'] = b'binarydata' * random.randint(1, 10)  # Vary data size
        db.close()
        os.remove('test.db')  # Clean up
        return True
    except Exception as e:
        return str(e)


def test_complex_annotations(annotation_data: typing.Union[typing.List[int], typing.Dict[str, str]]) -> typing.Any:
    """Tests complex type annotations."""
    if isinstance(annotation_data, list):
        try:
            return sum(annotation_data)  # Handle potential errors in list
        except Exception as e:
             return f"Error processing list: {e}"

    elif isinstance(annotation_data, dict):
        return annotation_data.get('key', None)
    else:
        return f"Unexpected type: {type(annotation_data)}"
   

def main():
    try:
        result = jit_target_function(list(range(random.randint(10000, 20000))))  # Vary input size
        print("JIT result:", result)

        free_threading_result = test_free_threading()
        print("Free threading result:", free_threading_result)

        dbm_result = test_dbm_sqlite3()
        print("dbm result:", dbm_result)

        complex_annotation_result = test_complex_annotations([random.randint(1, 100) for _ in range(random.randint(1,10))])  # Vary input data
        print("Complex annotation result:", complex_annotation_result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

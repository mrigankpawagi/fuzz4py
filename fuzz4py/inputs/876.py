
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def jit_sensitive_function(data: list[int]) -> int:
    """
    A function designed to be JIT compiled, potentially.
    """
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total


def multithreaded_function(data: list[int], delay: int) -> list:
    """
    A multithreaded function to stress free-threading.
    """
    results = []
    threads = []
    for item in data:
        t = threading.Thread(target=lambda x: results.append(x * 2), args=(item,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    time.sleep(delay)
    return results


def complex_annotation_example(data: typing.List[typing.Union[int, str]]) -> typing.Dict[str, int]:
    """
    Example using complex type annotations.
    """
    result_dict = {}
    for item in data:
        if isinstance(item, int):
            result_dict[str(item)] = item * 2
        elif isinstance(item, str):
            try:
                result_dict[item] = int(item)
            except ValueError:
                result_dict[item] = -1  # Handle invalid string
    return result_dict

# Fuzzing examples
if __name__ == "__main__":
    # Free-threading & JIT
    data = [i for i in range(1000)]
    results = multithreaded_function(data, 1)  # Introduce delay for potential race conditions

    try:
        #Test JIT compilation
        jit_sensitive_function(data)
    except Exception as e:
        print("Exception during JIT function:", e)

    # Complex Annotation Testing
    annotated_data = [1, 2, 3, "4", "five", 6, 7]
    annotated_results = complex_annotation_example(annotated_data)
    print("Complex annotation results:", annotated_results)


    # dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c') # 'c' for create
        db['key'] = 'value'
        db.close()
    except Exception as e:
        print("Error with dbm.sqlite3:", e)


    # Test with different SSL contexts (if available). Replace with appropriate SSL test data.
    try:
        context = ssl.create_default_context()
        # ... (SSL connection test code) ...
    except Exception as e:
        print("SSL error:", e)

    # os module example (replace with appropriate timer usage)
    try:
        start_time = time.time()
        time.sleep(2) # Replace with os.timer function
        end_time = time.time()
        print(f"OS timer elapsed: {end_time - start_time}")
    except Exception as e:
        print("Error with OS timer:", e)



import threading
import time
import copy
import dbm
import os
import ssl
import typing

def complex_function(data: typing.List[int], key: str) -> str:
    """
    A complex function demonstrating various Python 3.13 features.
    """

    # Test free-threading and GIL
    thread_local_data = threading.local()
    thread_local_data.value = data

    t = threading.Thread(target=complex_function2, args=(thread_local_data,))
    t.start()
    t.join()

    # Test __replace__ method (copy module).
    replaced_data = copy.replace(data, [123])  
    print("replaced:", replaced_data)

    # Test annotation scope complexity.
    nested_comp = [(lambda x: x + 1)(i) for i in data]
    print(f"nested_comp: {nested_comp}")

    # Test dbm.sqlite3
    try:
        db = dbm.open('test.db', 'c')
        db[key] = str(data)
        db.close()
        with dbm.open('test.db', 'r') as db:
            retrieved_data = db[key]
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")


def complex_function2(thread_local_data):
    print(f"Thread {threading.get_ident()} accessing data:", thread_local_data.value)
    time.sleep(1)


if __name__ == "__main__":
    #Fuzzing data - try different inputs.
    test_data = list(range(10))
    test_key = "some_key"
    
    try:
        complex_function(test_data, test_key)
    except Exception as e:
        print(f"Error in complex_function: {e}")

    #Test os timer functions.
    try:
        start_time = time.monotonic()
        time.sleep(2)
        end_time = time.monotonic()
        print(f"Time difference: {end_time - start_time} seconds.")
    except Exception as e:
        print(f"Error using os.timer functions: {e}")


    # Test ssl functionality (simplified).  Replace with more comprehensive fuzzing later
    try:
        context = ssl.create_default_context()
        print("Default SSL context created successfully.")
    except Exception as e:
        print(f"Error creating default SSL context: {e}")


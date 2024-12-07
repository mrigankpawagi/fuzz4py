
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys

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

    # Test __replace__ method (copy module).  Fuzzing with different types.
    try:
        replaced_data = copy.replace(data, [random.randint(-100, 100)])
        print("replaced:", replaced_data)
    except Exception as e:
        print(f"Error in copy.replace(): {e}")

    # Test annotation scope complexity.  Fuzzing with different operations in lambdas.
    try:
        nested_comp = [(lambda x: x * 2 if x % 2 == 0 else x + 1)(i) for i in data]
        print(f"nested_comp: {nested_comp}")
    except Exception as e:
        print(f"Error in annotation scope: {e}")

    # Test dbm.sqlite3 (fuzzing malformed data)
    try:
        db = dbm.open('test.db', 'c')
        db[key] = str(random.randint(10000, 100000))  # Malformed data attempt
        db.close()
        with dbm.open('test.db', 'r') as db:
            retrieved_data = db[key]
            print("Retrieved data:", retrieved_data)
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    
    try:
        os.remove('test.db')
    except OSError:
        pass

def complex_function2(thread_local_data):
    print(f"Thread {threading.get_ident()} accessing data:", thread_local_data.value)
    try:
        time.sleep(random.uniform(0.5, 2)) # Fuzzing with different sleep times.
    except Exception as e:
        print(f"Error in thread sleep: {e}")

def my_function(arg1: typing.List[int], arg2: str) -> typing.Tuple[int, str]:
    """
    This function demonstrates various features of Python 3.13.

    Args:
        arg1: A list of integers.
        arg2: A string.

    Returns:
        A tuple containing an integer and a string.
    """
    try:
        result_int = sum(arg1)
        result_str = arg2 + str(result_int)
        return result_int, result_str
    except Exception as e:
        print(f"Exception: {e}")
        return 0, "Error"



def threaded_function(data):
    result = my_function(data[0], data[1])
    print(f"Thread {threading.get_ident()}: {result}")



if __name__ == "__main__":
    # Fuzzing data - try different inputs (lists of varying types).
    test_data = [random.randint(-100,100) for _ in range(random.randint(5,20))]
    test_key = f"key_{random.randint(0,1000)}"
    try:
        complex_function(test_data, test_key)
    except Exception as e:
        print(f"Error in complex_function: {e}")

    # Test os timer functions.
    try:
        start_time = time.monotonic()
        # Simulate some operation that takes a random time
        time.sleep(random.uniform(0.5,2))
        end_time = time.monotonic()
        print(f"Time difference: {end_time - start_time} seconds.")
    except Exception as e:
        print(f"Error using os.timer functions: {e}")

    # Testing SSL.  Keep this basic for now
    try:
        context = ssl.create_default_context()
        print("Default SSL context created successfully.")
    except Exception as e:
        print(f"Error creating default SSL context: {e}")


    #Fuzzing with different data types and values.
    list_of_integers = [1, 2, 3, 4, 5]
    string_input = "Hello"
    my_data = [[1, 2, 3], "Hello"]

    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(copy.deepcopy(my_data),)) #Copy to prevent modification
        threads.append(t)
        t.start()
        time.sleep(0.1)


    for thread in threads:
        thread.join()



    # Test dbm.sqlite3 with an empty key
    try:
        db = dbm.open('mydatabase', 'c')
        db[''] = 'empty key'
        print("Successfully stored data with empty key.")
        db.close()
    except Exception as e:
        print(f"dbm error: {e}")




    #Test os.times()
    try:
        start_time = time.time()
        result = os.times()
        end_time = time.time()
        print(f"os.times() result: {result}, duration: {end_time - start_time}")
    except Exception as e:
        print(f"os error: {e}")

    #Test SSL
    try:
        ctx = ssl.create_default_context()
        print("SSL default context created successfully.")

    except Exception as e:
        print(f"SSL error: {e}")



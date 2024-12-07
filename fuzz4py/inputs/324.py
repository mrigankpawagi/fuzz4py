
import threading
import time
import copy
import dbm
import ssl
import os
import typing

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



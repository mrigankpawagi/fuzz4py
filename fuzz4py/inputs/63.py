
import threading
import copy
import dbm
import os
import ssl
import time
import typing
import random

def threaded_function(data: int, context: ssl.SSLContext) -> int:
    """
    A multithreaded function with complex inputs.

    Args:
        data: An integer input.
        context: An SSL context for testing.

    Returns:
        The input data +1.
    """
    try:
        # Simulate a potentially long-running operation
        time.sleep(random.uniform(0.05, 0.15))  # Introduce randomness

        # Example of manipulating data (replace with actual DB operation)
        db_name = f"mydatabase_{data}"  # Using a different database for each thread
        db = dbm.open(db_name, 'c')
        db[str(data)] = str(data + 1)
        db.close()
        return data + 1
    except Exception as e:
        print(f"Error in threaded function: {e} for data {data}")
        return -1
    

def main():
    # Example of using copy.replace (introducing potential errors)
    a = copy.copy({"a": 1, "b": 2})
    try:
        b = copy.replace(a, {"a": 3, "c": 4}) #Trying to replace more than one element, and a non-existent key
    except Exception as e:
        print(f"Error in copy.replace: {e}")
    
    # Test complex type annotations (fuzzing with different types)
    complex_data: typing.List[typing.Tuple[int, str]] = [(1, "hello"), (2, "world")]
    try:
        complex_data.append((random.randint(-100, 100), "fuzzing data"))  # Fuzz with random data
    except Exception as e:
        print(f"Error adding to complex_data: {e}")
    
    # Example usage of ssl.create_default_context() (using a different context)
    context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)  # add purpose
    
    # Test with a varied number of threads
    num_threads = random.randint(2, 10) # Vary the number of threads randomly
    data_list = list(range(num_threads))
    threads = []
    
    for i in data_list:
        thread = threading.Thread(target=threaded_function, args=(i, context))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    #Example of using os module timer functions (fuzzing with negative time)
    try:
        start_time = os.times()[0]
        time.sleep(-1) # Fuzz with negative time delay
        end_time = os.times()[0]
    except Exception as e:
        print(f"Error in os.times: {e}")


    # Check for potential issues within the threads
    for data in data_list:
        db_name = f"mydatabase_{data}"
        try:
            db_temp = dbm.open(db_name, 'r')
            if db_temp.get(str(data)) != str(data + 1):
                print(f"Data {data} was not processed correctly in database {db_name}.")
            db_temp.close()
        except Exception as e:
            print(f"Error checking database {db_name}: {e}")


if __name__ == "__main__":
    main()

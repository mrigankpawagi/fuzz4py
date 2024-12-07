
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing
import random

def my_function(data: typing.List[int]) -> int:
    """
    This function takes a list of integers and returns their sum.

    Args:
        data: A list of integers.

    Returns:
        The sum of the integers in the list.
    """
    total = 0
    for item in data:
        # Introduce potential for integer overflow
        try:
            total += item
        except OverflowError as e:
            print(f"Overflow Error in my_function: {e}")
            return -1  # Indicate error
    return total


def my_thread_func(data: typing.List[int]) -> None:
    """
    This function is intended to be run in a separate thread.
    """
    # Introduce potential race condition and time-dependent behaviour
    time.sleep(random.uniform(0.005, 0.02))
    try:
        result = my_function(data)
        if result == -1:
          raise Exception("Integer Overflow")  # Propagate error
        print(f"Thread: {threading.get_ident()}, Result: {result}")
    except Exception as e:
        print(f"Thread Error: {threading.get_ident()}, {e}")


if __name__ == "__main__":
    # Using a list of varying data types for fuzzing
    data = [1, 2, 3, 'a', 5]

    # Create multiple threads (for free-threading)
    threads = []
    for i in range(5):
        try:
          thread = threading.Thread(target=my_thread_func, args=(copy.deepcopy(data),))
          threads.append(thread)
          thread.start()
        except Exception as e:
          print(f"Thread creation error: {e}")

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


    try:
        # Simulate database access (for dbm.sqlite3) with potentially invalid data
        db = dbm.open("mydatabase", 'c')
        db['key'] = b'value\x00'  # Add null byte for fuzzing
        db.close()
    except Exception as e:
        print(f"Database Error: {e}")


    # Example using ssl (for testing ssl changes)
    try:
        ctx = ssl.create_default_context()
        # Replace with your certificate file if needed
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Introduce a potential invalid hostname
        with ctx.wrap_socket(s, server_hostname='invalid.hostname') as s:
            pass
    except Exception as e:
        print(f"SSL Error: {e}")


    # Fuzzing os timer function with potential errors
    try:
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        print(f"Time elapsed: {end_time - start_time}")

        # Incorrectly calling the function
        try:
          time.sleep(-1)  # Example of an invalid argument
        except Exception as e:
          print(f"Error in sleep: {e}") #Handle the exception properly


        #Example with a large time value
        try:
          time.sleep(1000000000)  # Very large delay
        except Exception as e:
          print(f"Error in sleep with large value: {e}") #Handle the exception properly


    except Exception as e:
        print(f"OS Timer Error: {e}")



    # Demonstrating a possible complex type annotation (fuzzing)
    try:
      my_list = [i for i in range(10) if i%2==0]
      my_list = [i for i in range(10) if type(i) == str] #invalid type
      my_list = [] #empty list
      my_list = [1, 2, "a", True] #Mixed data types

      my_function(my_list) #call function to test
    except Exception as e:
      print(f"Error in list fuzzing: {e}")



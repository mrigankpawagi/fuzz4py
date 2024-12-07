
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing

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
        total += item
    return total


def my_thread_func(data: typing.List[int]) -> None:
    """
    This function is intended to be run in a separate thread.
    """
    # Introduce potential race condition
    time.sleep(0.01)
    try:
        result = my_function(data)
        print(f"Thread: {threading.get_ident()}, Result: {result}")
    except Exception as e:
        print(f"Thread Error: {threading.get_ident()}, {e}")


if __name__ == "__main__":
    # Using a list of complex integers for fuzzing
    data = [1, 2, 3, 4, 5]


    # Create multiple threads (for free-threading)
    threads = []
    for i in range(5):
        thread = threading.Thread(target=my_thread_func, args=(copy.deepcopy(data),))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    try:
        # Simulate database access (for dbm.sqlite3)
        db = dbm.open("mydatabase", 'c')
        db['key'] = 'value'
        db.close()
    except Exception as e:
        print(f"Database Error: {e}")


    # Example using ssl (for testing ssl changes)
    try:
        ctx = ssl.create_default_context()
        # Replace with your certificate file if needed
        # Create a dummy socket to wrap
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with ctx.wrap_socket(s, server_hostname='example.com') as s:
            pass
    except Exception as e:
        print(f"SSL Error: {e}")


    # Fuzzing os timer function
    try:
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        print(f"Time elapsed: {end_time - start_time}")
    except Exception as e:
        print(f"OS Timer Error: {e}")



    # Demonstrating a possible complex type annotation
    my_list = [i for i in range(10) if i%2==0]

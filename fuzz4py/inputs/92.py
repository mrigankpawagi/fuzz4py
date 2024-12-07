
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import sys


def jit_test_function(x):
    """
    A function likely to be JIT compiled due to its tight loop.
    """
    total = 0
    for i in range(10000):
        total += x * i  # This is a simple calculation, but it's repeated
    return total


def race_condition_example(data: typing.List[int]) -> None:
    """
    Illustrates a potential race condition.
    """
    lock = threading.Lock()

    def incrementer(idx):
        with lock:
            data[idx] += 1
    
    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=incrementer, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()



def main():
    # Fuzzing for free-threading
    data = [0] * 5
    race_condition_example(data)
    print(data)


    # Fuzzing for JIT compiler
    result = jit_test_function(10)
    print(f"JIT result: {result}")



    # Fuzzing for docstring whitespace stripping
    def my_function():
        """This is a docstring
        with some whitespace"""
        pass


    # Fuzzing dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        db.close()
    except Exception as e:
        print(f"dbm error: {e}")

    # Fuzzing os module timer functions
    try:
        start_time = time.perf_counter()
        time.sleep(0.1)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Elapsed time: {elapsed}")
    except Exception as e:
        print(f"os timer error: {e}")
    



    # Fuzzing ssl
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))
            print("SSL connection established")
    except Exception as e:
        print(f"SSL error: {e}")

    #Fuzzing Copy module
    orig_list = [1, 2, 3]
    new_list = copy.copy(orig_list)
    print(new_list)



if __name__ == "__main__":
    import socket
    main()


import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random


def complex_function(data: typing.List[int], timeout: float = 1.0) -> int:
    """
    This function performs complex operations.  
    """
    result = 0
    try:
        # Simulate a long-running operation
        time.sleep(timeout)
        for item in data:
            result += item
        return result
    except Exception as e:
        return -1


def main():
    # Fuzzing with different inputs and threading
    data = [i for i in range(100)]
    
    # Fuzz with different data types
    fuzz_data = [random.randint(-100, 100) for _ in range(100)]
    fuzz_data2 = [random.random() for _ in range(100)]
    fuzz_data3 = ["fuzz" for _ in range(100)] #add string data

    thread_local_data = copy.deepcopy(data)  # Demonstrate copying
    thread_local_data2 = copy.deepcopy(fuzz_data)
    thread_local_data3 = copy.deepcopy(fuzz_data2)

    def worker(local_data):
        try:
            result = complex_function(local_data, random.uniform(0.05, 0.2)) #Vary timeout
            print(f"Thread {threading.get_ident()} result: {result}")
        except Exception as e:
            print(f"Thread {threading.get_ident()} failed: {e}")


    threads = []
    for i in range(3): #Fuzzing with multiple threads
        t = threading.Thread(target=worker, args=(thread_local_data,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    # Fuzzing dbm (simulated, not interacting with a real db).  Fuzzing different types
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db['key2'] = 123
        db['key3'] = b'binary_data' #add binary data
        value1 = db['key1']
        value2 = db['key2']
        value3 = db['key3']
        print(f"DB value key1: {value1}, key2: {value2}, key3: {value3}")
        db.close()
    except Exception as e:
        print(f"DB error: {e}")

    # Fuzzing os.times()  
    try:
        t = os.times()
        print(f"System time: {t}") 
        #Attempt to access a non-existent member
        try:
            print(f"System time second: {t[0]}")
        except Exception as e:
           print(f"Trying to access invalid array element: {e}")

    except Exception as e:
        print(f"OS time error: {e}")

    # Fuzzing ssl.create_default_context() - simplified (no actual connection)
    #Adding SSL context variations (not robust but demonstrates fuzzing)
    try:
        context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        print(f"SSL context created: {context}")
    except Exception as e:
        print(f"SSL error: {e}")


if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import dbm
import typing


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
    thread_local_data = copy.deepcopy(data)  # Demonstrate copying

    def worker():
        nonlocal thread_local_data
        try:
            result = complex_function(thread_local_data, 0.1) #Very Short timeout
            print(f"Thread {threading.get_ident()} result: {result}")
        except Exception as e:
            print(f"Thread {threading.get_ident()} failed: {e}")


    threads = []
    for i in range(3): #Fuzzing with multiple threads
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

    # Fuzzing dbm (simulated, not interacting with a real db).
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(f"DB value: {value}")
        db.close()
    except Exception as e:
        print(f"DB error: {e}")


    # Fuzzing os.times()
    try:
        t = os.times()
        print(f"System time: {t}")
    except Exception as e:
        print(f"OS time error: {e}")

    # Fuzzing ssl.create_default_context() - simplified (no actual connection)
    try:
        context = ssl.create_default_context()
        print(f"SSL context created: {context}")
    except Exception as e:
        print(f"SSL error: {e}")


if __name__ == "__main__":
    main()


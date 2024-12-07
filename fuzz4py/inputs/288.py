
import threading
import time
import copy
import dbm
import ssl
import os
import typing

def worker(data, lock):
    # Simulate a long-running operation with a possible race condition
    time.sleep(0.1)
    try:
        lock.acquire()
        data.append("Thread Output")  
        lock.release()
    except Exception as e:
        lock.acquire()
        print(f"Exception in thread: {e}")
        lock.release()


def main():
    data = []
    lock = threading.Lock()
    threads = []

    # Create and start multiple threads
    for i in range(5):
        t = threading.Thread(target=worker, args=(data, lock))
        threads.append(t)
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()
    
    #Check if the data contains all expected threads' output.
    # This demonstrates the use of a critical section (lock)
    expected_outputs = 5
    actual_outputs = len(data)
    print(f"Expected Outputs: {expected_outputs}, Actual Outputs: {actual_outputs}")

    #Example of testing os.times()
    start = time.time()
    print(f"Time of start {start}")
    process_time = os.times()[0]
    end = time.time()
    print(f"Process time: {process_time}, Time of end {end}")



    #Example of using typing with complex type annotation
    def process_data(data: typing.List[typing.Union[str, int]]) -> typing.List[str]:
        results: typing.List[str] = []
        for item in data:
            if isinstance(item, str):
                results.append(item.upper())
            elif isinstance(item, int):
                results.append(str(item))
        return results

    sample_data = [1, 2, "hello", 4, "world"]
    result = process_data(sample_data)
    print("Processed data:", result)


    #Example using dbm.sqlite3 with complex input 
    try:
        db = dbm.open('mydatabase', 'c') # 'c' for create
        db['key1'] = 'value1'
        db['key2'] = 'value2'
        db.close()
    except Exception as e:
        print(f"Error opening or closing DB: {e}")




if __name__ == "__main__":
    main()

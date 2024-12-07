
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket
import random

def worker(data: list, lock):
    data_copy = copy.deepcopy(data)
    with lock:
        for i in range(len(data_copy)):
            try:
                sleep_time = data_copy[i] / 1000.0
                time.sleep(sleep_time)
                data_copy[i] += 1
                sleep_time = 0.001 * (data_copy[i] % 3)
                time.sleep(sleep_time)
                if data_copy[i] % 2 == 0:
                    try:
                        data_copy.pop(data_copy.index(data_copy[i]))
                    except ValueError:
                        pass
                    
                fuzz_factor = random.random()
                append_val = None
                if fuzz_factor < 0.8:
                    append_val = data_copy[i] + random.randint(-5, 5)
                elif fuzz_factor < 0.9:
                    append_val = None
                elif fuzz_factor < 0.91:
                   append_val = "fuzz" 
                else:
                   append_val = 10**100
                
                data_copy.append(append_val)
            except IndexError as e:
                print(f"Error in worker (index): {e}, data_copy: {data_copy}, i: {i}")
            except Exception as e:
                print(f"Unexpected error in worker: {e}, data_copy: {data_copy}, i: {i}")
    # Update the original list outside the lock
    with lock:
        data[:] = data_copy[:]



def main():
    data_size = random.randint(50, 200)
    data = list(range(data_size))
    lock = threading.Lock()
    num_threads = random.randint(10, 30)
    threads = []

    for i in range(num_threads):
        threads.append(threading.Thread(target=worker, args=(data, lock)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for i, item in enumerate(data):
        if not isinstance(item, (int, type(None), str)):
            print(f"Error: Data element {i} is not an int, None or str. It is: {type(item)}")
        elif isinstance(item, int) and item != i + 1:
            print(f"Error: Data element {i} should be {i+1}, but it is {item}")

    try:
        fuzz_hostname = "not_a_real_host"
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=fuzz_hostname) as s:
            s.connect(('example.com', 443))
            print("SSL connection established successfully.")
            s.sendall(b"Fuzzing test string")
            response = s.recv(1024)
            print(f"Received: {response.decode()}")
    except ssl.SSLError as e:
        print(f"SSL connection failed: {e}")


    try:
        db = dbm.open('test.db', 'c')
        fuzz_key = b'\x00' * random.randint(100, 500)
        db['key'] = fuzz_key
        db.close()
        print('Database operation successful.')
    except dbm.error as e:
        print(f"Error opening/accessing database: {e}")

def complex_function(arg1: list, arg2: str) -> dict:
    result = {}
    for i in range(len(arg1)):
        result[str(i)] = arg1[i] * 2
    return result

def process_data(data_item: int, lock: threading.Lock):
    lock.acquire()
    try:
        # Simulate some work
        time.sleep(0.1)
        print(f"Processed {data_item}")
    finally:
        lock.release()

def race_condition_example(data: list):
    lock = threading.Lock()
    threads = []
    for item in data:
        thread = threading.Thread(target=process_data, args=(item, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def main2():
    try:
        data = list(range(10))
        race_condition_example(data)
        complex_result = complex_function([1, 2, 3, 4, 5], "test")
        print(complex_result)
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()
        class MyObject:
            def __init__(self, val):
                self.val = val
            def __replace__(self, **kws):
                return copy.copy(self)  #Simplified as per PEP 703
        obj = MyObject(10)
        new_obj = obj.__replace__(new_val=20)
        print(f"Original object: {obj.val}, New object: {new_obj.val}")
        start_time = time.time()
        result = os.times()
        end_time = time.time()
        print(result)
    except Exception as e:
        print(f"An error occurred in main2: {e}")


if __name__ == "__main__":
    main()
    main2()

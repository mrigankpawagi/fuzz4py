
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket
import random

def worker(data: typing.List[int], lock):
    with lock:
        for i in range(len(data)):
            try:
                sleep_time = data[i] / 1000.0
                time.sleep(sleep_time)
                data[i] += 1
                sleep_time = 0.001 * (data[i] % 3)
                time.sleep(sleep_time)
                if data[i] % 2 == 0:
                    try:
                        data.pop(data.index(data[i]))
                    except ValueError:
                        pass
                    
                
                # Fuzzing: Introduce potential for IndexError
                # Add a possibility of appending None, a string, or a large integer
                fuzz_factor = random.random()
                append_val = None
                if fuzz_factor < 0.8:
                    append_val = data[i] + random.randint(-5, 5)
                elif fuzz_factor < 0.9:
                    append_val = None
                elif fuzz_factor < 0.91:
                   append_val = "fuzz" 
                else:
                   append_val = 10**100
                
                
                try:
                    data.append(append_val)
                except IndexError:
                    print(f"Error in worker (appending): {i}, {data[i]}")
                except TypeError as e:
                    print(f"Error in worker: {e}")
            except IndexError as e:
                print(f"Error in worker (index): {e}")
            except Exception as e:
                print(f"Unexpected error in worker: {e}")
                

def main():
    # Fuzzing: Varying data sizes
    data_size = random.randint(50, 200)
    data = list(range(data_size))
    lock = threading.Lock()
    threads = []

    # Fuzzing: Varying number of threads
    num_threads = random.randint(10, 30)

    for i in range(num_threads):
        threads.append(threading.Thread(target=worker, args=(copy.deepcopy(data), lock)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    try:
        # Fuzzing: Check for unexpected data types in list
        for i, item in enumerate(data):
            if not isinstance(item, int):
                print(f"Error: Data element {i} is not an integer. It is: {type(item)}")
            elif item != i + 1:
                print(f"Error: Data element {i} should be {i+1}, but it is {item}")
    except IndexError as e:
        print(f"Error: Index out of bounds: {e}")

    # Fuzzing: Using a potentially invalid host
    try:
        fuzz_hostname = "not_a_real_host"  # Introduce a fuzzed value.
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
        # Fuzzing: Using malformed database key.
        db = dbm.open('test.db', 'c')
        # Fuzzing: Varying key size and data types
        fuzz_key = b'\x00' * random.randint(100, 500)
        db['key'] = fuzz_key
        db.close()
        print('Database operation successful.')
    except dbm.error as e:
        print(f"Error opening/accessing database: {e}")


import threading
import copy
import os
import ssl
import dbm
import time
import typing

def complex_function(arg1: typing.List[int], arg2: str) -> typing.Dict[str, int]:
    """
    A function demonstrating complex type annotations and potential JIT compilation targets.
    """
    result = {}
    for i in range(len(arg1)):
        result[str(i)] = arg1[i] * 2
    return result


def race_condition_example(data: list):
    """
    A function demonstrating multi-threading and potential race conditions.
    """
    lock = threading.Lock()
    threads = []
    
    for i in range(len(data)):
        thread = threading.Thread(target=process_data, args=(data[i], lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def process_data(data_item: int, lock: threading.Lock):
    lock.acquire()
    try:
        # Simulate some work
        time.sleep(0.1)
        print(f"Processed {data_item}")
    finally:
        lock.release()



def main2():
    try:
        data = list(range(10))
        race_condition_example(data)
        # Example usage of complex function. Note that a non-trivial return type
        # is crucial for testing type annotation handling.
        complex_result = complex_function([1, 2, 3, 4, 5], "test")
        print(complex_result)

        # Example with dbm.sqlite3 (very basic)
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()

        # Example with copy.replace() (for custom classes)
        class MyObject:
            def __init__(self, val):
                self.val = val

            def __replace__(self, **kws):
                return copy.replace(self, val=kws.get('new_val', self.val))

        obj = MyObject(10)
        new_obj = obj.__replace__(new_val=20)
        print(f"Original object: {obj.val}, New object: {new_obj.val}")

        # Example with os timer function
        start_time = time.time()
        result = os.times()
        end_time = time.time()
        print(result)

        # Example with ssl, extremely basic as a POC
        context = ssl.create_default_context()
        # ... (further SSL operations)



    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
    main2()

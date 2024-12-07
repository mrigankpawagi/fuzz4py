
import threading
import time
import copy
import os
import ssl
import typing
import random
import dbm

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    This function demonstrates complex logic with possible race conditions.
    """
    result = []
    for i in data:
        try:
            result.append(i * 2)
        except (TypeError, OverflowError) as e:
            error_message = f"Error in complex_function: {e}, data: {data}, i: {i}"
            print(error_message)
            try:
                if isinstance(i, int):
                    result.append(None)
                elif isinstance(i, float):
                    result.append(float('nan'))
                elif isinstance(i, str):
                    result.append(i + i)  # Concatenate strings
                else:
                    result.append(i)
            except Exception as e2:
                print(f"Error appending to result: {e2}")
                result.append(i)
    return result


def thread_function(data, lock):
    """
    Illustrates a multithreaded function with threading operations.
    """
    time.sleep(random.uniform(0, 0.05))  # Introduce random delays
    with lock:
        try:
            processed_data = complex_function(data)
            time.sleep(random.uniform(0, 0.03)) #Variable delay
            if processed_data:
                print(f"Thread {threading.current_thread().name}: {processed_data}")
            else:
                print(f"Thread {threading.current_thread().name}: Data processing failed.")
        except Exception as e:
            print(f"Error in thread_function: {e}, Data: {data}")
            
        #Potential race condition
        try:
            global global_counter
            global_counter = global_counter + 1 if global_counter is not None else 1
        except Exception as e3:
            print(f"Error accessing global counter: {e3}")

        #Potential exceptions from non-existent files
        try:
          with open("nonexistent_file.txt", "r") as f:
              data = f.read()
        except FileNotFoundError as e:
          print("File not found", e)

def worker(data, lock):
    try:
        result = sum(data) * 2
        local_data = locals() 
        local_data['inner_data'] = result
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: {result}")
        lock.release()
    except Exception as e:
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: Error: {e}")
        lock.release()


def main():
    global global_counter #Make global variable available in thread function
    global_counter = 0

    # Example data
    data = list(range(1000))
    lock = threading.Lock()

    threads = []
    for i in range(5):
      thread = threading.Thread(target=worker, args=(data, lock))
      threads.append(thread)
      thread.start()
    
    for thread in threads:
      thread.join()
    

    #Example fuzzing
    data_types = [
        list(range(10)),
        [1, 2, 'a'],
        [1, 2, 3, 10**9], # Large integer
        [],
        [None],
        [True, False],
        [1.5, 2.7, 3.14],
        [-1, -2, -3],
        [0] * 100,
        [random.randint(-100, 100) for _ in range(20)],
        [random.random() for _ in range(10)],
        [None, 1, 2, None],
        [],
        [1, 2, 3, 10**9, 1.1],  # Combine int and float
        [b"abc", 1, 2],
        [1, 2, complex(3,4)],
        [None, True, False, [], {}],
        [""],
        [1, 2, 3, None, "a"],
        [None, None, None],
        [1, 2, None, 4, "hello"],
        [complex(1,2), complex(3,4)],
        [None, [1, 2, 3], (4, 5, 6)],
        [{"a": 1}, {"b": 2}],
        [lambda x: x + 1, 2],  # Functions
        [lambda:None],
        [1000000.0, 2000000.0, 3000000.0],  #Large floats
        [1, 2, 1j],  #Complex numbers
        [1.5, 2.7, 3.14, "str", 10**20]  # Larger numbers and mixed data
    ]

    for data in data_types:
        try:
            lock = threading.Lock()
            threads = []
            num_threads = random.randint(2, 5)

            for i in range(num_threads):
              thread = threading.Thread(target=thread_function, args=(copy.deepcopy(data), lock))
              threads.append(thread)
              thread.start()
            
            for thread in threads:
              thread.join()
        except RuntimeError as e:
            print(f"Error during thread execution: {e}")
        except Exception as e:
            print(f"An unhandled error occurred: {e}")

        print("All threads finished for current data set\n")

if __name__ == "__main__":
    main()


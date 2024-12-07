
import threading
import time
import copy
import os
import ssl
import typing
import random

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    This function demonstrates complex logic with possible race conditions.
    """
    result = []
    for i in data:
        try:
            result.append(i * 2)
        except (TypeError, OverflowError) as e:
            print(f"Error in complex_function: {e}, data: {data}, i: {i}")
            result.append(None)  # Handle errors gracefully
    return result


def thread_function(data, lock):
    """
    Illustrates a multithreaded function with threading operations.
    """
    
    # Introduce random delays
    time.sleep(random.uniform(0, 0.05))  
    
    with lock:
        processed_data = complex_function(data)
        # Simulate some slow operation
        time.sleep(random.uniform(0, 0.03)) #Variable delay
        if processed_data:
            print(f"Thread {threading.current_thread().name}: {processed_data}")
        else:
            print(f"Thread {threading.current_thread().name}: Data processing failed.")


def main():
    try:
        # Fuzzing with different data types and sizes
        data_types = [[1, 2, 3], [1, 2, 'a'], [1, 2, 3, 10000000000], [], [None], [True, False],
                      [1.5, 2.7, 3.14], [-1, -2, -3], [0] * 100,  # Larger lists
                      [random.randint(-100, 100) for _ in range(20)], #Randomly generated list
                      [random.random() for _ in range(10)], #Floats
                      [None, 1, 2, None],
                      [],
                      [1, 2, 3, 10000000000, 1.1], # Mixed Types
                      [b"abc", 1, 2]  #Bytes
                      ]
        
        for data in data_types:
            print(f"Running with data: {data}")

            lock = threading.Lock()
            threads = []

            num_threads = random.randint(2, 5)  # Vary number of threads
            for i in range(num_threads):
               thread = threading.Thread(target=thread_function, args=(copy.deepcopy(data), lock))
               threads.append(thread)
               thread.start()


            for thread in threads:
                thread.join()
            
            print("All threads finished for current data set\n")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    main()

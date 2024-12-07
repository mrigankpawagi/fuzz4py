
import threading
import time
import copy
import os
import ssl
import typing

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    This function demonstrates complex logic with possible race conditions.
    """
    result = []
    for i in data:
        result.append(i * 2)
    return result


def thread_function(data, lock):
    """
    Illustrates a multithreaded function with threading operations.
    """
    with lock:
        processed_data = complex_function(data)
        # Simulate some slow operation
        time.sleep(0.01)
        print(f"Thread {threading.current_thread().name}: {processed_data}")



def main():
    try:
        data = [1, 2, 3, 4, 5]
        lock = threading.Lock()


        threads = []
        for i in range(1,3): # Create multiple threads
           thread = threading.Thread(target=thread_function, args=(copy.deepcopy(data), lock))
           threads.append(thread)
           thread.start()

        for thread in threads:
            thread.join()
        
        print("All threads finished")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    main()


import threading
import copy
import os
import time
import ssl
import typing

def worker(arg: int):
    """
    A worker function that demonstrates thread interaction.

    Args:
        arg: An integer argument.
    """
    print(f"Thread {threading.current_thread().name} started with arg: {arg}")
    time.sleep(0.1)  # Simulate work
    print(f"Thread {threading.current_thread().name} finished with arg: {arg}")

def main():
    """
    A main function to test multithreading and potential race conditions.
    """
    args = [1, 2, 3]
    threads = []
    for arg in args:
        thread = threading.Thread(target=worker, args=(arg,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Example using copy.replace() (potentially problematic)
    try:
        data = {'a': 1, 'b': 2}
        new_data = copy.deepcopy(data)
        new_data.replace({'b':3})  # potential issues with replace
        print("data after replace:", new_data)
    except Exception as e:
        print("Error during replace:", e)

if __name__ == "__main__":
    main()


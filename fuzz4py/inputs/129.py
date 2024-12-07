
import threading
import copy
import os
import time
import ssl
import typing
import random

def worker(arg: int):
    """
    A worker function that demonstrates thread interaction.

    Args:
        arg: An integer argument.
    """
    print(f"Thread {threading.current_thread().name} started with arg: {arg}")
    try:
        time.sleep(0.1 * random.random())  # Simulate varying work time
        print(f"Thread {threading.current_thread().name} finished with arg: {arg}")
        # Introduce potential race condition
        global_var = threading.local()
        global_var.value = arg + 1
    except Exception as e:
        print(f"Error in worker thread {threading.current_thread().name}: {e}")


def main():
    """
    A main function to test multithreading and potential race conditions.
    """
    num_threads = 10 # Changed to a larger number of threads
    args = [random.randint(1, 100) for _ in range(num_threads)] # Random arguments
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
        # Inject a more complex replace operation.
        try:
          new_data.replace({"b": 3, "c": 4})
        except AttributeError as e:
          print(f"AttributeError during replace: {e}")
          
        print("data after replace:", new_data)
        # Add a test with a non-dictionary type
        non_dict_data = [1, 2, 3]
        try:
            copy.copy(non_dict_data).replace(4) #testing replace on non-dict type
        except Exception as e:
            print(f"Error replacing non-dictionary type: {e}")

    except Exception as e:
        print("Error during replace:", e)

    # Introduce a test with bad data types
    try:
        bad_data = 123
        copy.copy(bad_data).replace(10) #testing replace on non-dict type

    except Exception as e:
        print(f"Error replacing a non-dict type: {e}")

if __name__ == "__main__":
    main()

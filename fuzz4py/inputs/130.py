
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
		# Introduce a possible exception
        if arg % 2 == 0:
            raise ValueError("Forced exception in worker thread")

    except ValueError as e:
        print(f"Caught ValueError: {e} in thread {threading.current_thread().name}")
    except Exception as e:
        print(f"Error in worker thread {threading.current_thread().name}: {e}")


def main():
    """
    A main function to test multithreading and potential race conditions.
    """
    num_threads = 20  # Increased for more concurrency stress
    args = [random.randint(1, 100) for _ in range(num_threads)]  # Random arguments
    threads = []
    for arg in args:
        thread = threading.Thread(target=worker, args=(arg,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    # Example using copy.replace() (potentially problematic)
    try:
        data = {'a': 1, 'b': 2, 'c': 3}
        new_data = copy.deepcopy(data)
        #Inject a potentially problematic replace operation
        try:
          new_data.replace({'b': 3, 'd': 4})  
          new_data.replace({'a': 5, 'b': 6})  # Test multiple replacements
          new_data = new_data.replace({'c': 7}) # Test with different objects
        except AttributeError as e:
          print(f"AttributeError during replace: {e}")
          
        print("data after replace:", new_data)
		# Test with a list
        list_data = [1, 2, 3]
        try:
          list_data.replace([4, 5, 6])  #Attempt to use replace on a list object
        except AttributeError as e:
          print(f"AttributeError replacing list: {e}")
        
        # Attempt to replace with a lambda
        try:
            data.replace(lambda x: x + 1) #Test replace with lambda
        except TypeError as e:
          print(f"Type Error during replace: {e}")
          

    except Exception as e:
        print("Error during replace:", e)

    # Introduce a test with bad data types
    try:
        bad_data = 123
        copy.copy(bad_data).replace(10) #testing replace on non-dict type
        # Introduce a test using a custom object.
        class CustomObject:
            def __init__(self, val):
                self.val = val
        custom_obj = CustomObject(10)
        try:
            copy.copy(custom_obj).replace(20)
        except Exception as e:
            print(f"Error replacing a custom object type: {e}")

    except Exception as e:
        print(f"Error replacing a non-dict type: {e}")

if __name__ == "__main__":
    main()

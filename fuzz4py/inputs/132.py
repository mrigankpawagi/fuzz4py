
import threading
import copy
import os
import time
import ssl
import typing
import random
import sys

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
        # Introduce a new error condition
        if arg > 50:
            raise TypeError("Type error in worker thread")

    except ValueError as e:
        print(f"Caught ValueError: {e} in thread {threading.current_thread().name}")
        
    except TypeError as e:
        print(f"Caught TypeError: {e} in thread {threading.current_thread().name}")
    except Exception as e:
        print(f"Error in worker thread {threading.current_thread().name}: {e}")
        # Ensure the program doesn't crash with unhandled exceptions


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

        # Inject a potentially problematic replace operation (with various types)
        try:
            new_data.replace({'b': 3, 'd': 4})  
            new_data = new_data.replace({'a': 5, 'b': 6})
            new_data.replace({'c': 7, 'b': 8, 'e': 9}) #More complex replacements
            new_data.replace([1,2,3]) #replace with a list!
            new_data.replace(lambda x: x+1) #Testing with a function

        except AttributeError as e:
          print(f"AttributeError during replace: {e}")
        except TypeError as e:
            print(f"TypeError during replace: {e}")  # Handle potential type errors
        except Exception as e:
          print(f"An unexpected error during replace: {e}")
        finally:
            print("data after replace:", new_data)


    except Exception as e:
        print("Error during replace:", e)

    try:

        #Introduce a test using None
        data_with_none = {'a': 1, 'b': None, 'c': 3}
        try:
            copy.deepcopy(data_with_none).replace({'b': 'abc'})
        except Exception as e:
            print(f"Error trying to replace with None: {e}")
            
    except Exception as e:
      print("Error trying to replace with none:", e)

	#Adding a test case with a custom object to replace.
    try:
      class CustomObject:
        def __init__(self, val):
            self.val = val
      custom_object = CustomObject(10)
      copy.deepcopy(custom_object).replace(20) #Test replace with a custom object.
      # Adding a more complex case.
      complex_object = {"a": 1, "b": custom_object}
      copy.deepcopy(complex_object).replace({"b": CustomObject(20)})


    except Exception as e:
      print(f"Error with custom objects and replace : {e}")

if __name__ == "__main__":
    main()

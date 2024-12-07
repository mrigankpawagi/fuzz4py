
import threading
import time
import copy
import os
import ssl
import typing
import random

def worker(arg: int):
    """
    A worker function to demonstrate free-threading.
    """
    try:
        print(f"Thread {threading.current_thread().name} received {arg}")
        time.sleep(random.uniform(0.05, 0.15))  # Simulate varying work times
        return arg * 2
    except Exception as e:
        print(f"Error in worker thread: {e}")
        return None


def main():
    """
    Main function demonstrating multi-threading and the new os timer.
    """
    threads = []
    args = [i for i in range(random.randint(3, 7))]  # Vary number of threads
    
    for arg in args:
        thread = threading.Thread(target=worker, args=(arg,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    #Demonstrating error handling with os.times()
    try:
        start_time = time.perf_counter()
        # ...some code that takes time...
        os_times_result = os.times()
        end_time = time.perf_counter()
        print(f"Time spent in the process (os.times): {end_time - start_time:.4f} seconds")
        print(f"CPU times (user, system, children, elapsed): {os_times_result}")
    except Exception as e:
        print(f"Error in os.times(): {e}")


    # Example of complex type annotation with lambda and error handling
    try:
        my_data: typing.List[typing.Callable[[int], int]] = [
            lambda x: x * 2,
            lambda x: x + 5,
            lambda x: x / 0  # Introducing a potential error
        ]
        result = my_data[0](10)
        print(result)
        result = my_data[1](10)
        print(result)
    except ZeroDivisionError as e:
        print(f"Error in lambda: {e}")
    except Exception as e:
        print(f"Unhandled Error in lambda: {e}")

    #Example of a problematic function that can be JIT compiled.  Add input variations
    try:
        def problematic_function(input_list):
            res = 0
            for i in input_list:
                res += i
            return res

        input_data = random.choices(range(-100, 100), k=random.randint(10000, 20000)) #Varying list length & contents
        result = problematic_function(input_data)
        print("Result of problematic_function:", result)
    except Exception as e:
      print(f"Error in problematic_function: {e}")


    # Demonstrating __replace__ with potential errors
    my_list = [1,2,3]
    try:
        new_list = copy.replace(my_list, 2, random.randint(10, 1000))
        print(f"Replacing 2 with random value in my_list: {new_list}")
    except Exception as e:
        print(f"Error in replace: {e}")

if __name__ == "__main__":
    main()


import threading
import time
import os
import copy
import ssl
import typing
import random


def multithreaded_function(data: typing.List[int], delay: int) -> typing.List[int]:
    """
    A multithreaded function that potentially suffers from race conditions.
    """
    results = [0] * len(data)

    threads = []
    for i, num in enumerate(data):
        # Introduce random delay.  Adding more variability.
        delay_factor = random.uniform(0.05,0.8)  # Wider range

        thread = threading.Thread(target=process_element, args=(i, num, results, delay * delay_factor))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def process_element(i, num, results, delay):
    """
    Simulates a potentially slow operation.
    """
    try:
        time.sleep(delay)  #Simulate potentially slow operation.
        # potential race condition: introduce a random integer
        random_int = random.randint(0, 100)
        results[i] = num * 2 + random_int
        # Adding potential for exception within the loop
        if random.random() < 0.1:
          raise ValueError("Random exception")
    except Exception as e:
        print(f"Error in process_element: {e}, for index: {i}")
        #  Record the error in results for testing
        results[i] = -1


def main():
    # Example usage
    data = [1, 2, 3, 4, 5, 100]  # Added a larger number
    delay = 0.1  # Adjust for varying execution times.

    try:
        results = multithreaded_function(data, delay)
        print(f"Results: {results}")


        # Test copy module with replace protocol if available
        if hasattr(copy, 'replace'):
            original_list = copy.deepcopy(data)
            # Mutate the list - replace a single item with a different type.
            try:
                new_list = copy.replace(original_list, 0, "hello") # replace with a string!
                print(f"List after replace: {new_list}")
                print(f"Original list unchanged: {original_list}")
            except Exception as e:
                print(f"Error using copy.replace: {e}")
            try:
                # Try to replace with an incompatible type
                new_list = copy.replace(original_list,0, 2.5)
            except Exception as e:
                print(f"Error using copy.replace (incompatible type): {e}")


        # Test os module timer functions (if available)
        if hasattr(os, 'times'):
            start_time = os.times()
            # sleep with a random duration for more comprehensive testing.
            time.sleep(random.uniform(1, 3))
            end_time = os.times()
            print("OS time results:", end_time)
            print("OS time results:", start_time)
            # Attempting a negative value to see what it does.
            try:
                time_result = os.times(-1)
                print(f"time_result:{time_result}")
            except Exception as e:
                print(f"Error in os.times call: {e}")



        #Illustrate a more complex usage case with ssl context
        if hasattr(ssl, 'create_default_context'):
            context = ssl.create_default_context()
            try:
                # Introduce invalid context (more robust error handling)
                invalid_context = ssl.SSLContext("invalid_protocol")
            except Exception as e:
                print(f"Error creating invalid context: {e}")
            print(f"Default SSL context: {context}")

            #Fuzzing with various inputs
            try:
                context_with_invalid_arg = ssl.create_default_context(flags='invalid_flags')
            except Exception as e:
                print(f"Error creating SSL context with invalid argument: {e}")


    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

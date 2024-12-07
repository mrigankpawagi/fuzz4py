
import threading
import time
import copy
import os
import ssl
import typing

def race_condition_example(data: list[int], lock: threading.Lock) -> None:
    """
    Illustrative example of a potential race condition.
    """
    with lock:
        for i in range(len(data)):
            data[i] += 1

def jit_test_function(n: int) -> int:
    """
    A function with a loop designed to be JIT-compiled.
    """
    sum = 0
    for i in range(n):
        sum += i
    return sum
    
def fuzz_replace_protocol(obj: typing.Union[list, tuple]) -> list[int]:
    """
    Test the replace protocol with a list.
    """
    try:
        new_obj = copy.replace(obj,0)
        if new_obj is not None:  # Check for None before iteration
            return [i for i in new_obj]
        else:
            return [0]  # Return a default value for errors
    except Exception as e:
        return [0]  # Return a default value for errors


if __name__ == "__main__":
    data = [1, 2, 3]
    lock = threading.Lock()

    threads = []
    for _ in range(5):
        thread = threading.Thread(target=race_condition_example, args=(data, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print("Data after threads:", data) # Observe potential race conditions

    # Testing JIT compiler
    n = 1000000
    start_time = time.time()
    result = jit_test_function(n)
    end_time = time.time()
    print(f"JIT test result {result} calculated in {end_time-start_time:.4f} seconds")
    
    #Test replace protocol
    my_list = [1,2,3,4,5]
    replaced_list = fuzz_replace_protocol(my_list)
    print(f"Replaced list: {replaced_list}")


    try:
        # Example of using os module timer functions with large values.
        time_value = 1000.5
        try:
            delay = os.get_clock_info("monotonic")  # Get clock info
            result = os.times()  # Get system CPU time
            print(f"Get clock info: {delay}")
            print(f"CPU time: {result}")
        except (OSError, AttributeError) as e:
            print(f"Error in os module test (likely non-supported clock): {e}")
    except Exception as e:
      print(f"Error in os module test: {e}")


    #Test ssl
    try:
        context = ssl.create_default_context()
        print("Default ssl context created.")
    except Exception as e:
        print(f"Error creating ssl context: {e}")



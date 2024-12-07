
import threading
import time
import copy
import os
import ssl
import typing

def worker(arg: int):
    """
    A worker function to demonstrate free-threading.
    """
    print(f"Thread {threading.current_thread().name} received {arg}")
    time.sleep(0.1)  # Simulate some work
    return arg * 2


def main():
    """
    Main function demonstrating multi-threading and the new os timer.
    """
    threads = []
    args = [i for i in range(5)]
    
    # Using a list comprehension for diverse threading arguments
    for arg in args:
        thread = threading.Thread(target=worker, args=(arg,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    # Demonstrate os.times() usage
    start_time = time.perf_counter()
    # ...some code that takes time...
    os_times_result = os.times()
    end_time = time.perf_counter()
    print(f"Time spent in the process (os.times): {end_time - start_time:.4f} seconds")
    print(f"CPU times (user, system, children, elapsed): {os_times_result}")
    
    # Example of complex type annotation with lambda
    my_data: typing.List[typing.Callable[[int], int]] = [
        lambda x: x * 2,
        lambda x: x + 5,
    ]
    result = my_data[0](10)
    print(result)


    #Example of a problematic function that can be JIT compiled
    def problematic_function(input_list):
        res = 0
        for i in input_list:
            res += i
        return res

    #This section can be easily JIT compiled due to the loop
    large_list = list(range(10000))
    result = problematic_function(large_list)
    print("Result of problematic_function:", result)

    # Demonstrating __replace__ (although no custom class)
    my_list = [1,2,3]
    try:
      new_list = copy.replace(my_list, 2, 10) #Built-in list
      print(f"Replacing 2 with 10 in my_list: {new_list}")
    except Exception as e:
      print(f"Error in replacing: {e}")

if __name__ == "__main__":
    main()

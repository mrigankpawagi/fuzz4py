
import threading
import time
import copy
import os
import ssl
import typing
import random
import sys

def worker(arg: int):
    """
    A worker function to demonstrate free-threading.
    """
    try:
        print(f"Thread {threading.current_thread().name} received {arg}")
        time.sleep(random.uniform(0.05, 0.15))  # Simulate varying work times
        if arg % 2 == 0:
          raise ValueError("Even numbers cause errors!")
        return arg * 2
    except ValueError as e:
        print(f"Error in worker thread: {e}")
        return None
    except Exception as e:
        print(f"Error in worker thread: {type(e).__name__}: {e}")
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

    try:
        start_time = time.perf_counter()
        for i in range(random.randint(1000, 5000)):
          pass
        os_times_result = os.times()
        end_time = time.perf_counter()
        print(f"Time spent in the process (os.times): {end_time - start_time:.4f} seconds")
        print(f"CPU times (user, system, children, elapsed): {os_times_result}")
    except Exception as e:
        print(f"Error in os.times(): {e}")


    try:
        my_data: typing.List[typing.Callable[[int], int]] = [
            lambda x: x * 2,
            lambda x: x + 5,
            lambda x: x / random.randint(1, 5)
        ]

        for func in my_data:
          try:
            result = func(10)
            print(result)
          except ZeroDivisionError as e:
            print(f"Error in lambda: {e}")
          except Exception as e:
            print(f"Unhandled Error in lambda: {type(e).__name__}: {e}")



    except Exception as e:
        print(f"Unhandled Error in complex annotation: {type(e).__name__}: {e}")
    try:
        def problematic_function(input_list):
            res = 0
            for i in input_list:
                res += i
                if res > sys.maxsize:
                    raise OverflowError("Result exceeds maximum integer value")
            return res

        input_data = random.choices(range(-100, 100), k=random.randint(10000, 20000))
        result = problematic_function(input_data)
        print("Result of problematic_function:", result)
    except OverflowError as e:
      print(f"Error in problematic_function: Integer overflow occurred! {e}")
    except Exception as e:
      print(f"Error in problematic_function: {type(e).__name__}: {e}")


    my_list = [1,2,3]
    new_list = copy.copy(my_list)  # Prevent potential issues
    new_list[1] = random.randint(10, 1000)
    print(f"Replacing 2 with random value in my_list: {new_list}")


if __name__ == "__main__":
    main()

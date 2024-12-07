
import threading
import time
import copy
import os
import ssl
import typing
import dbm
import random
import sys


def my_function(arg1: int, arg2: str = "default") -> str:
    """
    This function demonstrates several Python 3.13 features.
    """
    try:
        # Test Free-threading and GIL with varying sleep times and thread counts
        thread_local_var = 0
        num_threads = random.randint(1, 10)
        sleep_time = random.uniform(0.01, 0.5)
        
        # Introduce potential race condition by directly modifying a global
        global_var = 0
        
        def worker():
            nonlocal thread_local_var
            
            thread_local_var += random.randint(-100, 100)
            try:
                time.sleep(sleep_time)
                # Introducing random exceptions
                if random.random() < 0.1:  
                    raise ValueError("Random Exception in worker")
            except Exception as e:
                print(f"Thread error: {e}", file=sys.stderr)  # Use stderr for errors
                # Log the error to a file (robust error handling)
                with open("thread_errors.log", "a", encoding='utf-8', errors='ignore') as err_file:
                    try:
                        err_file.write(f"Thread error: {e}\n")
                    except Exception as e2:
                        print(f"Error writing to log file: {e2}", file=sys.stderr)


            # Adding a race condition
            global global_var
            global_var += random.randint(1, 10)  # Random increment
            
            try:
                with open("random_file.txt", "a", encoding='utf-8', errors='ignore') as f:  # append to file
                    f.write(str(random.randint(1, 100)) + "\n")  # write random data
            except Exception as e:
                print(f"File error: {e}", file=sys.stderr)
                with open("file_errors.log", "a", encoding='utf-8', errors='ignore') as err_file:
                    try:
                        err_file.write(f"File error: {e}\n")
                    except Exception as e2:
                        print(f"Error writing to log file: {e2}", file=sys.stderr)


        threads = [threading.Thread(target=worker) for _ in range(num_threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Test annotation scopes, complex types with random inputs
        list_len = random.randint(1, 10)
        list1 = [random.randint(-1000, 1000) for _ in range(list_len)]  # Wider range
        list2 = [str(random.randint(-1000, 1000)) for _ in range(list_len)]  # Allow non-numeric strings
        result = [(x, y) for x, y in zip(list1, list2)]
        
        if not isinstance(thread_local_var, int):
            raise TypeError("thread_local_var is not an integer.")

        return f"Free Threading result: {thread_local_var}, global_var: {global_var}"
    
    except Exception as e:
        return f"Error: {e}"
    

def main():
  
    # ... (rest of the code is the same, but with minor adjustments)
    # ...


if __name__ == "__main__":
    main()


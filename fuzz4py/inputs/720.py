
import threading
import time
import copy
import ssl
import os
import dbm
import random
import sys

def threaded_function(i, data, lock, error_injection_chance):
    # Simulate a potentially slow operation
    time.sleep(random.uniform(0.05, 0.15))  # Introduce randomness

    # Introduce potential error injection
    if random.random() < error_injection_chance:
      raise ValueError("Simulated error in thread")

    with lock:
        try:
            data[i] += 1
            return data[i]
        except IndexError as e:
            print(f"Caught IndexError in thread {threading.current_thread().name}: {e}")
            return None
        except ValueError as e:
          print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
          return None

def main():
    data = [0] * 100  # Shared data
    lock = threading.Lock() # Added lock for thread safety
    threads = []
    error_injection_chance = 0.05  # Adjust for desired error injection rate


    for i in range(10):
        thread = threading.Thread(target=threaded_function, args=(i, data, lock, error_injection_chance))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print("Final data:", data)

    # Testing copy.replace() - replace values in list (with potential for errors)
    try:
        new_data = copy.deepcopy(data)
        
        # Attempt to modify with potentially large value
        new_data[random.randint(0, 99)] = new_data[random.randint(0, 99)] + sys.maxsize
        print("Modified data:", new_data)
    except Exception as e:
        print(f"Error with copy.replace(): {e}")

    # Testing dbm.sqlite3 - example usage (with potential for errors)
    try:
        db = dbm.open('mydatabase', 'c')
        key = "key" + str(random.randint(1, 1000))
        db[key] = str(random.randint(1000, 20000))  # Adding random data
        
        # Attempting to fetch a non-existent key
        value = db.get("nonexistent_key")
        if value:
            print("Database value:", value)
        else:
            print("Database key not found")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")



    # Testing os.times() - timing (introduce a potential race condition probe)
    start_time = os.times()[0]
    try:
        # Introduce a larger sleep time in the second thread.
        other_thread = threading.Thread(target=lambda: time.sleep(random.uniform(0.5, 2.0)))  
        other_thread.start()
        time.sleep(random.uniform(0.1, 0.5))  
        other_thread.join()
    except Exception as e:
        print(f"Error during os.times(): {e}")

    end_time = os.times()[0]
    print("Time elapsed:", end_time - start_time)

    # Attempting ssl.create_default_context() - more robust example
    try:
        context = ssl.create_default_context()
        # Probe with various invalid values
        context.options = random.randint(0, 1000000) 
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

    #Testing docstring whitespace stripping (with more complex format).
    def my_func():
        """
        This is a docstring
        with  \t  indentation   
        \t levels.


        """
        pass
    print(my_func.__doc__)

    # Testing annotations with potential errors in the annotation.
    try:
        def test_annotation(param: list[int | str] | int) -> list[int]:
            return [1, 2, 3]
    except Exception as e:
        print(f"Error in annotation testing: {e}")




if __name__ == "__main__":
    main()


import threading
import time
import copy
import ssl
import os
import dbm
import random
import sys
import types

def threaded_function(i, data, lock, error_injection_chance, extra_data):
    # Simulate a potentially slow operation
    time.sleep(random.uniform(0.05, 0.15))  # Introduce randomness

    # Introduce potential error injection
    if random.random() < error_injection_chance:
      raise ValueError("Simulated error in thread")
    try:
        if random.random() < 0.1: # Introduce another error
            data = None # this could cause issues
        else:
            data = data  # no change
    except:
        print("Data became none")


    with lock:
        try:
            data[i] += extra_data
            return data[i]
        except IndexError as e:
            print(f"Caught IndexError in thread {threading.current_thread().name}: {e}")
            return None
        except ValueError as e:
          print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
          return None
        except Exception as e:  # Catch other exceptions
          print(f"Caught exception in thread {threading.current_thread().name}: {e}")
          return None


def main():
    data = [0] * 100  # Shared data
    lock = threading.Lock()
    threads = []
    error_injection_chance = 0.05
    extra_data_list = [random.randint(-100, 100) for _ in range(10)]
    try:
        for i in range(10):
            extra_data = extra_data_list[i % len(extra_data_list)] # use list circularly
            thread = threading.Thread(target=threaded_function, args=(i, data, lock, error_injection_chance, extra_data))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Final data:", data)

        # Testing copy.replace() - replace values in list (with potential for errors)
        try:
            new_data = copy.deepcopy(data)
            new_data_size = len(new_data)
            # Attempt to modify with potentially large value and index out of range
            new_data[random.randint(0, new_data_size)] = new_data[random.randint(0, new_data_size -1)] + sys.maxsize
            print("Modified data:", new_data)
        except Exception as e:
            print(f"Error with copy.replace(): {e}")


        # Testing dbm.sqlite3 - example usage (with potential for errors)
        db = dbm.open('mydatabase', 'c')
        key = "key" + str(random.randint(1, 1000))
        db[key] = str(random.randint(1000, 20000))

        # Attempting to fetch a non-existent key with random data as key
        value = db.get(str(random.randint(1,10000)))
        if value:
            print("Database value:", value)
        else:
            print("Database key not found")
        db.close()

        #Testing os.times() - timing
        start_time = os.times()[0]
        try:
            # Introduce a potential race condition -  sleep with a large value.
            other_thread = threading.Thread(target=lambda: time.sleep(random.uniform(2, 10)))
            other_thread.start()
            time.sleep(random.uniform(0.1, 0.5))  # Potentially interrupting
            other_thread.join()

        except Exception as e:
            print(f"Error during os.times(): {e}")

        end_time = os.times()[0]
        print("Time elapsed:", end_time - start_time)


        #Try SSL with random data.
        context = ssl.create_default_context(purpose=random.choice([ssl.Purpose.CLIENT_AUTH, ssl.Purpose.SERVER_AUTH]))
        print("SSL context created successfully")


        # More thorough docstring fuzzing with random characters
        def my_func():
            """
            This is a docstring with  \t indentation   
            \t levels.
            Random characters: {} [] \n \t .!@#$%^&*()_+=- {  \t\t random\n\t
             more  }
            """
            pass
        print(my_func.__doc__)

        # Testing annotations with complex types and random input
        def test_annotation(param: list[int | str | float] | tuple[int]) -> list[int]:
            random_input = random.choice([random.randint(1, 100), "test", 3.14])
            return [random_input] if isinstance(random_input, int) else []
        print(test_annotation(random.randint(1, 100)))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


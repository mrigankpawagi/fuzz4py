
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
        if random.random() < 0.1:  # Introduce another error
            data = None  # this could cause issues
        elif random.random() < 0.2:  # Introduce an IndexError
            data[i] = "random data" # Incorrect data type

        else:
            data[i] += extra_data
    except ValueError as e:
        print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
        return None
    except IndexError as e:
        print(f"Caught IndexError in thread {threading.current_thread().name}: {e}")
        return None
    except TypeError as e:  # Catch potential type errors
        print(f"Caught TypeError in thread {threading.current_thread().name}: {e}")
        return None
    except Exception as e:  # Catch other exceptions
        print(f"Caught exception in thread {threading.current_thread().name}: {e}")
        return None

    with lock:
        try:
            return data[i]
        except Exception as e:
            print(f"Exception in lock block {threading.current_thread().name}: {e}")
            return None


def main():
    data = [0] * 100  # Shared data
    lock = threading.Lock()
    threads = []
    error_injection_chance = 0.05
    extra_data_list = [random.randint(-100, 100) for _ in range(10)]
    try:
        for i in range(10):
            extra_data = extra_data_list[i % len(extra_data_list)]  # use list circularly
            thread = threading.Thread(target=threaded_function, args=(i, data, lock, error_injection_chance, extra_data))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Final data:", data)


        #Testing copy.replace() - replace values in list (with potential for errors)
        try:
            new_data = copy.deepcopy(data)
            new_data_size = len(new_data)
            # Attempt to modify with potentially large value and index out of range
            new_data_index = random.randint(0, new_data_size) if new_data_size > 0 else 0
            new_data[new_data_index] = new_data[random.randint(0, new_data_size - 1)] + random.randint(-sys.maxsize, sys.maxsize)
            print("Modified data:", new_data)
        except Exception as e:
            print(f"Error with copy.replace(): {e}")


        # Testing dbm.sqlite3 - example usage (with potential for errors)
        db = dbm.open('mydatabase', 'c')
        key = "key" + str(random.randint(1, 1000))
        db[key] = str(random.randint(1000, 20000))

        # Attempting to fetch a non-existent key with random data as key
        key2 = str(random.randint(1, 10000))
        value = db.get(key2)
        if value:
            print("Database value:", value)
        else:
            print("Database key not found")
        db.close()



        #Testing os.times() - timing, adding race condition for potential issues.
        start_time = os.times()[0]
        try:
            other_thread = threading.Thread(target=lambda: time.sleep(random.uniform(2, 10)))  # Introduce potentially long sleep
            other_thread.start()

            time.sleep(random.uniform(0.1, 0.5)) # Potentially interrupting


            other_thread.join()
            os.times()


        except Exception as e:
            print(f"Error during os.times(): {e}")
        end_time = os.times()[0]
        print("Time elapsed:", end_time - start_time)



        try:
            context = ssl.create_default_context()
            print("SSL context created successfully")
        except Exception as e:
            print("Error with SSL context creation:",e)

        #Docstring fuzzing
        def my_func():
            """Docstring with random characters: !@#$%^&*()_+=-{}[]|;:'\",.<>/?`~"""
            pass
        print(my_func.__doc__)


        #Testing annotations with complex types and random input, including potential errors.
        def test_annotation(param: list[int | str | float] | tuple[int]) -> list[int]:
            random_input = random.choice([random.randint(1, 100), "test", 3.14, None, []]) # More varied inputs
            try:
                return [random_input] if isinstance(random_input, int) else []
            except Exception as e:
                print(f"Error in annotation function: {e}")
                return []

        try:
            result = test_annotation(random.randint(1, 100))
            print("Annotation result:", result)
        except Exception as e:
            print(f"Error in annotation call: {e}")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


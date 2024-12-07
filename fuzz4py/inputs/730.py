
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
            data[i] = None  # Assign None
        elif random.random() < 0.2:  # Introduce an IndexError
            try:
                data[i] = random.choice([None, True, 123, "abc", b"bytes"])  # Fuzz data type
            except IndexError:
                print(f"Caught IndexError in thread {threading.current_thread().name}")
                return None
        elif random.random() < 0.3: #Adding a TypeError
            try:
                data[i] =  1 if isinstance(data[i], int) else data[i]
            except TypeError:
                print(f"Caught TypeError in thread {threading.current_thread().name}")
                return None
        else:
            try:
                if data[i] is not None:
                    data[i] = data[i] + extra_data  # Avoid adding to None
                data[i] = random.choice([data[i], None, "string"])  # Fuzz data type
            except (TypeError, IndexError) as e:
                print(f"Caught {type(e).__name__} in thread {threading.current_thread().name}: {e}")
                return None
    except ValueError as e:
        print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
        return None
    except Exception as e:  # Catch other exceptions
        print(f"Caught exception in thread {threading.current_thread().name}: {e}")
        return None

    with lock:
        try:
            return data[i] if data[i] is not None else None  # Handle potential None values
        except (IndexError, TypeError) as e:
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
            extra_data = extra_data_list[i % len(extra_data_list)]
            thread = threading.Thread(target=threaded_function, args=(i, data, lock, error_injection_chance, extra_data))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Final data:", data)


        #Testing copy.replace() - replace values in list (with potential for errors)
        try:
            new_data = copy.copy(data)
            new_data_size = len(new_data)
            new_data_index = random.randint(0, new_data_size - 1)  # Corrected index check
            new_data[new_data_index] = new_data[new_data_index] + random.randint(-sys.maxsize, sys.maxsize)
            print("Modified data:", new_data)
        except Exception as e:
            print(f"Error with copy.replace(): {e}")



        # Testing dbm.sqlite3 - example usage (with potential for errors)
        try:
            db = dbm.open('mydatabase', 'c')
            key = "key" + str(random.randint(1, 1000))
            db[key] = str(random.randint(1000, 20000))
            key2 = "key" + str(random.randint(1, 10000))
            value = db.get(key2)
            if value:
                print("Database value:", value)
            else:
                print("Database key not found")
            db.close()
        except Exception as e:
            print(f"Error with dbm.sqlite3: {e}")



        #Fuzzing os.times() - adding more potential issues
        try:
            start_time = os.times()[0]
            other_thread = threading.Thread(target=lambda: time.sleep(random.uniform(2, 10)))
            other_thread.start()
            time.sleep(random.uniform(0.1, 0.5))
            other_thread.join()
            end_time = os.times()[0]
            print("Time elapsed:", end_time - start_time)
        except Exception as e:
            print(f"Error during os.times(): {e}")



        try:
            context = ssl.create_default_context()
            print("SSL context created successfully")
        except Exception as e:
            print("Error with SSL context creation:", e)

        #Docstring fuzzing (adding more complex characters)
        def my_func():
            """Docstring with random characters: !@#$%^&*()_+=-{}[]|;:'\",.<>/?`~ \t\n"""
            pass
        print(my_func.__doc__)

        #Testing annotations with complex types and random input, including potential errors
        def test_annotation(param: list[int | str | float] | tuple[int]) -> list[int]:
            random_input = random.choice([random.randint(1, 100), "test", 3.14, None, [], (1,2)]) #Added more choices
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

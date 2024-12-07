
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
                data[i] = random.choice([None, True, 123, "abc", b"bytes", [], {}, (1, 2)])
            except IndexError:
                print(f"Caught IndexError in thread {threading.current_thread().name}")
                return None
        elif random.random() < 0.3:
            try:
              if isinstance(data[i], (int, float)):  # Check for numeric types
                  data[i] = 1 if isinstance(data[i], int) else random.randint(1,100)  # More type error possibilities
              else:
                  data[i] = random.choice([None, True, 123, "abc", b"bytes", [], {}, (1, 2)]) # If not numeric
            except TypeError:
                print(f"Caught TypeError in thread {threading.current_thread().name}")
                return None
        elif random.random() < 0.4:
            try:
                if isinstance(data[i], dict):
                    data[i][random.choice(['key1', 'key2'])] = random.randint(1, 100)
            except KeyError:
                print(f"Caught KeyError in thread {threading.current_thread().name}")
                return None
        else:
            try:
                if data[i] is not None:
                    try:
                        data[i] += extra_data  # Only add if not None
                    except TypeError:
                        pass # Do nothing if not numeric

                data[i] = random.choice([data[i], None, "string", b"bytes", 123.45])
            except (TypeError, IndexError, KeyError) as e:
                print(f"Caught {type(e).__name__} in thread {threading.current_thread().name}: {e}")
                return None
    except ValueError as e:
        print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
        return None
    except Exception as e:
        print(f"Caught exception in thread {threading.current_thread().name}: {e}")
        return None


    with lock:
        try:
          return data[i] if data[i] is not None else None
        except (IndexError, TypeError, KeyError) as e:
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

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

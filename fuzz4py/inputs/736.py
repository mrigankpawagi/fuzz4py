
import threading
import time
import random
import sys
import types
import copy
import ssl
import os
import dbm
import datetime

def threaded_function(i, data, lock, error_injection_chance, extra_data, some_complex_object):
    # Simulate a potentially slow operation
    time.sleep(random.uniform(0.05, 0.15))

    # Introduce potential errors
    if random.random() < error_injection_chance:
        raise ValueError("Simulated error in thread")

    try:
        # Introduce errors with varying probabilities
        rand = random.random()
        if rand < 0.1:
            data[i] = None
        elif rand < 0.2:
            data[i] = random.choice([None, True, 123, "abc", b"bytes", [], {}, (1, 2), datetime.datetime.now()])
        elif rand < 0.3:
            if isinstance(data[i], (int, float)):
                data[i] = 1 if isinstance(data[i], int) else random.randint(1, 100)
            else:
                data[i] = random.choice([None, True, 123, "abc", b"bytes", [], {}, (1, 2), some_complex_object])
        elif rand < 0.4:
            if isinstance(data[i], dict) and isinstance(data[i], dict):
                data[i][random.choice(['key1', 'key2'])] = random.randint(1, 100)
        elif rand < 0.5:
            try:
                data[i].append(extra_data)  # Attempt list append
            except AttributeError:
                pass
        elif rand < 0.6:
            try:
                data[i][0] = extra_data  # Attempt dict access
            except (KeyError, IndexError, AttributeError):
                pass

        elif data[i] is not None:
            try:
                data[i] += extra_data
            except (TypeError, IndexError):
                pass
            except Exception as e:
                print(f"Unexpected exception during addition: {e}")
        data[i] = random.choice([data[i], None, "string", b"bytes", 123.45, True, False, some_complex_object])  # Wider range of choices, includes complex object
    except (IndexError, KeyError, TypeError) as e:
        print(f"Caught exception during data manipulation: {type(e).__name__} in thread {threading.current_thread().name}: {e}")
        return None
    except ValueError as e:
        print(f"Caught ValueError in thread {threading.current_thread().name}: {e}")
        return None
    except Exception as e:  # Catch all other exceptions
        print(f"Unhandled exception in thread {threading.current_thread().name}: {e}")
        return None

    with lock:
        try:
            return data[i]
        except (IndexError, KeyError, TypeError) as e:
            print(f"Exception accessing data in lock block {threading.current_thread().name}: {e}")
            return None


def main():
    data = [0] * 100
    lock = threading.Lock()
    threads = []
    error_injection_chance = 0.05
    extra_data_list = [random.randint(-100, 100) for _ in range(10)]
    some_complex_object = {"nested_key": [1, 2, 3]} # Introduce a complex object

    try:
        for i in range(10):
            extra_data = extra_data_list[i % len(extra_data_list)]
            thread = threading.Thread(target=threaded_function, args=(i, data, lock, error_injection_chance, extra_data, some_complex_object))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Final data:", data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

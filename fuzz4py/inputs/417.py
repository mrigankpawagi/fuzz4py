
import threading
import copy
import os
import ssl
import time
import random
import typing

def worker(data: typing.List[int]) -> None:
    result = 0
    for item in data:
        try:
            if isinstance(item, int):
                result += item * random.randint(1, 100)
            else:
                raise TypeError(f"Invalid data type: {type(item)}")
        except TypeError as e:
            print(f"Error in worker: {e}, Data: {data}")
            return
    sleep_time = random.uniform(0.001, 0.05)
    time.sleep(sleep_time)
    print(f"Thread {threading.current_thread().name} result: {result}")


def main():
    try:
        data = list(range(10))
        threads = []
        for i in range(5):
            if random.random() < 0.2:
                data_copy = copy.copy(data)
                data_copy.append(None)  # Potentially problematic value
                thread = threading.Thread(target=worker, args=(data_copy,))
            else:
                thread = threading.Thread(target=worker, args=(copy.copy(data),))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        start = time.perf_counter()
        try:
            os.times() # Use default flags
        except Exception as e:
            print(f"Error in os.times: {e}")
        end = time.perf_counter()
        print(f"Time taken to get os.times(): {end - start}")
        
        try:
            random_data = [1, 2, 'a', 4]
            worker(random_data)
        except Exception as e:
            print(f"Error processing random data: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


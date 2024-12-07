
import threading
import copy
import os
import ssl
import time
import typing
import random

def worker(data: typing.List[int]) -> None:
    # Simulate a CPU-bound task
    result = 0
    for i in data:
        try:
          # Introduce potential error by multiplying by random value
          result += i * random.randint(1,100)
        except TypeError as e:
          print(f"Error in worker: {e}, Data: {data}")
          return
    time.sleep(random.uniform(0.001, 0.05)) # Variable sleep time
    print(f"Thread {threading.current_thread().name} result: {result}")


def main():
    try:
        data = list(range(10))
        threads = []
        for i in range(5):
            # Mutated:  Randomly choose to pass a modified list (potential for error)
            if random.random() < 0.2:
                data_copy = copy.copy(data)
                data_copy.append(None) # Add a potentially problematic value
                thread = threading.Thread(target=worker, args=(data_copy,))
            else:
                thread = threading.Thread(target=worker, args=(copy.copy(data),))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


        # Mutated:  Get process times with different flags (potential for error)
        start = time.perf_counter()
        try:
          os.times(random.randint(0,100))  # Use random flags (potential error)
        except Exception as e:
           print(f"Error in os.times: {e}")
        end = time.perf_counter()
        print(f"Time taken to get os.times(): {end - start}")
        
        #Mutated:  Error handling on potentially corrupted data.
        try:
          random_data = [1, 2, 'a', 4]
          worker(random_data)
        except Exception as e:
          print(f"Error processing random data: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


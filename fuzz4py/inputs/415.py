
import threading
import copy
import os
import ssl
import time
import typing

def worker(data: typing.List[int]) -> None:
    # Simulate a CPU-bound task
    result = 0
    for i in data:
        result += i * i
    time.sleep(0.01)  # Introduce a delay
    print(f"Thread {threading.current_thread().name} result: {result}")

def main():
    try:
        data = list(range(10))
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker, args=(copy.copy(data),))  # Critical: Copying the data
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Example of using the new os timer functions
        start = time.perf_counter()
        os.times()  # Get process times (new)
        end = time.perf_counter()
        print(f"Time taken to get os.times(): {end - start}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()



import threading
import time
import copy
import os
import ssl
import typing

def worker(arg: int, lock: threading.Lock):
    lock.acquire()
    try:
        print(f"Thread {threading.get_ident()} received: {arg}")
        time.sleep(arg % 5)  # Introduce varying sleep times
    finally:
        lock.release()
    

def main():
    lock = threading.Lock()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


    # Example using copy.replace() (Illustrative)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y
        def __replace__(self, **kwargs):
            return copy.copy(self)

    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=3)  # should copy p1 and modify x

    # Demonstration of dbm.sqlite3
    # ... (omitting dbm.sqlite3 example as it requires a database for a complete test)

    # Testing os module timer functions
    start_time = time.perf_counter()
    result = os.times()
    end_time = time.perf_counter()
    print(f"Time taken to call os.times(): {end_time - start_time}")
    
    try:
        # Testing ssl.create_default_context()
        context = ssl.create_default_context()  
        # ... (example of using the context to connect to a server)
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    

    # Illustrative testing of a complex annotation
    def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
        result = []
        for item in data:
            if isinstance(item, int):
                result.append(item * 2)
            elif isinstance(item, str):
                try:
                  result.append(int(item) * 3)
                except ValueError:
                  print("ValueError: Not a valid integer string")
        return result
    
    annotated_data: typing.List[typing.Union[int, str]] = [1, 2, "3", "abc"]
    processed_data = process_data(annotated_data)
    print(f"Processed data: {processed_data}")


if __name__ == "__main__":
    main()

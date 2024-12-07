
import threading
import time
import os
import copy
import ssl
import typing

def worker(data, lock):
    try:
        # Simulate some work
        time.sleep(0.1)
        # Access shared data (race condition potential)
        with lock:
            data[0] += 1
    except Exception as e:
        print(f"Error in worker thread: {e}")
    

def main():
    data = [0]
    lock = threading.Lock()
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=worker, args=(data, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    print(f"Final count: {data[0]}")
  
    # Demonstrating replace protocol using a simple class
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __replace__(self, x=None, y=None):
            new_point = copy.copy(self)  # Crucial for avoiding modifying the original
            if x is not None:
                new_point.x = x
            if y is not None:
                new_point.y = y
            return new_point

    # Using copy.replace()
    p = Point(1, 2)
    p_new = copy.replace(p, x=3)
    print(f"Original Point: {p.x}, {p.y}")
    print(f"New Point: {p_new.x}, {p_new.y}")
    
    # Example using a complex type annotation with lambdas
    def process_data(data: typing.List[int]) -> typing.List[int]:
        return list(map(lambda x: x * 2, data))
    
    #Test the function
    processed_data = process_data([1, 2, 3])
    print("Processed Data", processed_data)
    
    # Example to show the usage of a timer on Linux (using os.times) 
    start_time = time.time()
    os.times()
    end_time = time.time()
    print("Time taken by os.times:", end_time - start_time)
    
    # SSL example - (Simplified for demonstration)
    context = ssl.create_default_context()

    # ... (your SSL connection code) ...
    # ... you would test the connect on this context ...


if __name__ == "__main__":
    main()

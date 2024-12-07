
import threading
import copy
import os
import time
import ssl
import typing

def worker(arg: int, lock):
    try:
        # Simulate some work.  Susceptible to race conditions
        result = arg * 2
        
        # Acquire the lock before modifying the shared resource.
        lock.acquire()
        try:
            shared_list.append(result)  # Race condition potential
        finally:
            lock.release()
    except Exception as e:
        print(f"Error in worker thread: {e}")


if __name__ == "__main__":
    shared_list = []
    lock = threading.Lock()
    
    threads = []
    
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Shared list: {shared_list}")

    # Example using copy.replace() (Potentially problematic)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, **kwargs):
            return Point(kwargs.get('x', self.x), kwargs.get('y', self.y))


    point = Point(1, 2)
    new_point = copy.replace(point, x=10)
    print(f"Modified point: {new_point.x}, {new_point.y}")
    
    # Example using os.times()
    start_time = time.time()
    result = os.times()
    end_time = time.time()
    print(f"OS Times: {result}")
    print(f"Time taken: {end_time - start_time}")

    try:
        # Example using ssl.create_default_context() with potential issue (simplified)
        context = ssl.create_default_context()
        
        #This would be a real certificate load/verification step
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))  # Replace with your actual server
            
    except Exception as e:
        print(f"SSL Error: {e}")



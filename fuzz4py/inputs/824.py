
import threading
import time
import copy
import os
import ssl
import typing

def threaded_function(arg):
    # Simulate some work, potentially using C extensions.
    time.sleep(0.1)
    # Demonstrating modification of a shared resource
    global shared_data
    shared_data += arg


def main():
    global shared_data
    shared_data = 0

    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    try:
        # Demonstrating copy.replace()
        # Define a custom class for demonstration
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __replace__(self, **kwargs):
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']
                return self
        
        p1 = Point(1, 2)
        p2 = copy.replace(p1, x=10)
        assert p1.x == 1
        assert p2.x == 10
        
        # Use of annotations:
        def my_function(arg: typing.List[int]) -> int:
            return sum(arg)
    
        my_list = [1, 2, 3]
        result = my_function(my_list)
        print(f"Result: {result}")

    except Exception as e:
        print(f"Exception caught in main: {e}")


if __name__ == "__main__":
    main()

    # Demonstrating os.timer functions (using monotonic for example)
    start_time = time.monotonic()
    time.sleep(0.5)
    end_time = time.monotonic()
    print(f"Time elapsed (monotonic): {end_time - start_time}")
    # Adding ssl for demonstration of new default flags
    try:
        context = ssl.create_default_context()
        # Replace with your actual certificate if you have one
        with context.wrap_socket(socket.socket(), server_hostname='localhost'):
            print("SSL connection successful")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    


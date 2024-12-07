
import threading
import time
import os
import copy
import ssl
import typing
import dbm

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


    # Example from the second program
    def complex_function(data: typing.List[int], sleep_time: float = 0.1) -> typing.List[int]:
        """
        A function that performs some operations on a list, potentially causing race conditions.
        """
        try:
            if not isinstance(data, list):
                raise TypeError("Input must be a list")
            
            # Simulate some time-consuming operation
            time.sleep(sleep_time)

            results = []
            for item in data:
                results.append(item * 2)
            
            # Simulate a race condition (potential problem to find)
            results[0] = -1  # This is highly dependent on the interpreter's threading model
            return results
        except TypeError as e:
            print(f"Error in complex_function: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error in complex_function: {e}")
            raise
    
    data = list(range(10))
    threads = []
    for i in range(5):
        thread = threading.Thread(target=complex_function, args=(copy.copy(data),))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    #Example with potentially problematic type annotation
    def problematic_annotation(a: typing.Union[int, str, complex]) -> typing.Union[int, str, complex]:
        return a

    # Example using the new dbm module
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()
        
        db = dbm.open('mydatabase', 'r')
        value = db['key1']
        db.close()

    except Exception as e:
        print(f"Error in dbm example: {e}")
    
    
    # Example using os module timer functions
    try:
        start_time = os.times()[4]
        time.sleep(0.2)
        end_time = os.times()[4]
        print(f"Time taken: {end_time - start_time}")
    except Exception as e:
        print(f"Error in os module example: {e}")
    
    # Example using ssl (fuzz testing)
    try:
        context = ssl.create_default_context()
        # ... (Code to establish a connection with a certificate) ...
    except Exception as e:
        print(f"Error in ssl example: {e}")
        
if __name__ == "__main__":
    main()

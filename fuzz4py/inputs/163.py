
import threading
import time
import copy
import os
import ssl
import typing
import random

def complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    This function demonstrates complex logic with possible race conditions.
    """
    result = []
    for i in data:
        try:
            result.append(i * 2)
        except (TypeError, OverflowError) as e:
            print(f"Error in complex_function: {e}, data: {data}, i: {i}")
            try:
                if isinstance(i, int):
                  result.append(None)
                elif isinstance(i, float):
                    result.append(float('nan'))
                elif isinstance(i, str):
                    result.append(i + i)  # Concatenate strings
                else:
                    result.append(i)
            except Exception as e2:
                print(f"Error appending to result: {e2}")
                result.append(i)
    return result


def thread_function(data, lock):
    """
    Illustrates a multithreaded function with threading operations.
    """
    
    # Introduce random delays
    time.sleep(random.uniform(0, 0.05))  
    
    with lock:
        try:
          processed_data = complex_function(data)
          # Simulate some slow operation
          time.sleep(random.uniform(0, 0.03)) #Variable delay
          if processed_data:
              print(f"Thread {threading.current_thread().name}: {processed_data}")
          else:
              print(f"Thread {threading.current_thread().name}: Data processing failed.")
        except Exception as e:
            print(f"Error in thread_function: {e}, Data: {data}")
            
        #Adding a potential race condition
        try:
          global_counter = 0
          global_counter += 1
        except Exception as e3:
          print(f"Error accessing global counter: {e3}")
          
        #Introducing potential exceptions from non-existent files
        try:
          with open("nonexistent_file.txt", "r") as f:
            data = f.read()
        except FileNotFoundError as e:
          print("File not found",e)


def worker(data, lock):
    try:
        # Simulate a potentially JIT-compiled operation
        result = sum(data) * 2
        
        # Accessing locals() in a multithreaded context
        local_data = locals() 
        local_data['inner_data'] = result
        
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: {result}")
        lock.release()
        
    except Exception as e:
        lock.acquire()
        print(f"Thread {threading.current_thread().name}: Error: {e}")
        lock.release()


def main():
    # Example data, could be dynamically generated or from a file
    data = list(range(1000))
    
    # Test with and without GIL
    
    lock = threading.Lock()

    threads = []
    for i in range(5):
      thread = threading.Thread(target=worker, args=(data, lock))
      threads.append(thread)
      thread.start()

    for thread in threads:
      thread.join()


    # Fuzzing Docstrings with varying indentation
    docstring = """This is a test docstring
        with varying indentation levels
      ."""

    # Fuzzing complex type annotations
    annotation_data: typing.List[typing.Tuple[int, str]] = [(1, "a"), (2, "b")]

    # Testing dbm.sqlite3 (replace with a proper dbm.sqlite3 test)
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        db.close()

        db = dbm.open('test.db', 'r')
        print(db['key'])
        db.close()
        os.remove('test.db') # Clean up
    except Exception as e:
      print(f"dbm error: {e}")

    # Fuzzing os module timer functions (Linux specific)
    try:
        time_result = os.times()
        print(f"os.times() result: {time_result}")

    except Exception as e:
        print(f"os timer error: {e}")

    # Fuzzing ssl.create_default_context() (test with different certificates)
    try:
        context = ssl.create_default_context()
        # ... use the context to create a secure connection ...
        print("SSL context created successfully.")

    except Exception as e:
        print(f"SSL error: {e}")

    # Fuzzing with different data types and sizes (from the first code block)
    data_types = [
        [1, 2, 3],
        [1, 2, 'a'],
        [1, 2, 3, 10000000000],
        [],
        [None],
        [True, False],
        [1.5, 2.7, 3.14],
        [-1, -2, -3],
        [0] * 100,
        [random.randint(-100, 100) for _ in range(20)],
        [random.random() for _ in range(10)],
        [None, 1, 2, None],
        [],
        [1, 2, 3, 10000000000, 1.1],
        [b"abc", 1, 2],
        [1, 2, complex(3,4)],
        [None, True, False, [], {}],
        [""],
        [1,2,3,None,"a"],
        [None, None, None],
        [1, 2, None, 4, "hello"],
        [complex(1,2), complex(3,4)],
        [None, [1, 2, 3], (4, 5, 6)],
        [{"a": 1}, {"b": 2}],
        [lambda x: x + 1, 2], #Functions
        [lambda:None],
        [1000000.0, 2000000.0, 3000000.0], #Large floats
        [1, 2, 1j], #Complex numbers
        [1.5, 2.7, 3.14, "str", 10000000000000000000] # Larger numbers and mixed data
    ]
    
    for data in data_types:
        print(f"Running with data: {data}")
        lock = threading.Lock()
        threads = []
        num_threads = random.randint(2, 5)
        try:
            for i in range(num_threads):
                thread = threading.Thread(target=thread_function, args=(copy.deepcopy(data), lock))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
        except RuntimeError as e:
            print(f"Error during thread execution: {e}")
        except Exception as e:
            print(f"An unhandled error occurred: {e}")

        print("All threads finished for current data set\n")



if __name__ == "__main__":
    main()


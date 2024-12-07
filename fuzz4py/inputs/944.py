
import threading
import time
import copy
import os
import ssl
import dbm.sqlite3
import typing
import random

def worker(data: typing.List[int], lock, thread_id):
    for i in data:
        # Simulate some work that can be JIT-compiled.
        time.sleep(0.001 + random.random() * 0.001)  # Introduce randomness
        lock.acquire()
        try:
            # Potential race condition.
            # Notice this thread is not using the GIL.
            # This code now can be executed by multi-threading.
            temp = i * 2
            
            # Introduce potential corruption by overwriting with a string.
            if random.random() < 0.5:  #Increased chance
                if i % 2 == 0:
                    data[i] = "hello"  # Potentially corrupting the data list
            
            #Error induction
            if random.random() < 0.1:
                raise ValueError(f"Error from thread {thread_id}")
            
            # Add fuzzing:  attempt to write a None value to the list.
            if random.random() < 0.2:
                data[i] = None  # Trying to write a None value

            # Attempt to divide by zero
            if random.random() < 0.1:
                try:
                   temp = temp / 0 
                except ZeroDivisionError as e:
                    print(f"Error from thread {thread_id}: {e}")


        finally:
            lock.release()


def main():
    data = list(range(1000))
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data, lock, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")

    # Example using dbm.sqlite3
    try:
        db = dbm.sqlite3.open("mydatabase.db", 'c')  # 'c' mode creates the DB
        db['key1'] = 'value1'
        
        # Fuzzing the dbm module with malformed key
        try:
            db[str(123) * 1000] = 'value2'
            db[b'\x00' * 1000] = 'value3'  # Try binary data
            db[None] = 'value4' # Null key
        except Exception as e:
           print(f"Error writing to database: {e}")
        
        db.close()
    except Exception as e:
        print(f"Database error: {e}")

    # Introducing a potential copy issue.
    copied_data = copy.copy(data)
    print("Copied data:", copied_data)


    # Add the other main function (with fuzzing for data_list)
    global shared_resource
    shared_resource = 0
    num_threads = 5
    
    #Fuzzing data_list
    data_list = [random.randint(-100, 100) for i in range(num_threads)]  # Random numbers

    for i in data_list:
        thread = threading.Thread(target=threaded_function, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print(f"Final shared resource: {shared_resource}")
    
    # Test copy.replace() (more thorough testing)
    class Replaceable:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b
        def __replace__(self, a=None, b=None):
            if a is not None: self.a = a
            if b is not None: self.b = b
            return self

    r1 = Replaceable(10, "hello")
    r2 = copy.replace(r1, a=20)
    r3 = copy.replace(r1, b= "world")

    print(f"r1.a: {r1.a}, r2.a: {r2.a}, r3.b: {r3.b}")

    # Fuzzing dbm.sqlite3 (create a dummy database)
    try:
        db = dbm.open('mydatabase', 'c')
        db[str(123) * 10] = 'value1' # more complex key
        db.close()
    except Exception as e:
        print(f"Error accessing dbm.sqlite3: {e}")

    # Test os.times() (with more data)
    t = os.times()
    print(f"Time Information: {t}")

    # Test ssl.create_default_context() (simplified)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

    # Example with complex typing (more thorough)
    try:
      result = my_function(10)
      result2 = my_function("123abc45")
      result3 = my_function("abc")
      print(f"Result 1: {result}, Result 2: {result2}, Result 3: {result3}")
    except Exception as e:
      print(f"Error in my_function: {e}")

def my_function(arg: typing.Union[int, str]) -> typing.List[int]:
    if isinstance(arg, int):
        return list(range(arg))
    elif isinstance(arg, str):
        return [int(c) for c in arg if c.isdigit()]
    else:
        return []

def threaded_function(data: int) -> int:
    global shared_resource
    try:
        shared_resource += data
    except TypeError as e:
        print(f"Error in threaded_function: {e}")
    return shared_resource


if __name__ == "__main__":
    main()



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
            temp = i * 2
            
            # Introduce potential corruption by overwriting with a string, list, or None.
            if random.random() < 0.5:  #Increased chance
                try:
                    if i % 2 == 0:
                        data[i] = "hello"
                    data[i] = [1, 2, 3]
                    data[i] = None
                    data[i] = 1234  #Adding more types
                    data[i] = b"binary data" #Fuzz with bytes
                    data[i] = {'key': 'value'} #Fuzz with dict
                    data[i] = lambda: None #Fuzz with lambda
                    data[i] = [1, 2, data[i]]  #Recursive list
                    data[i] = object() #add object type
                    data[i] = float('inf') #Fuzz with float
                    data[i] = float('-inf') #Fuzz with float
                    data[i] = complex(1,2)  #Fuzz with complex number
                    data[i] = frozenset([1,2,3])  #Fuzz with frozenset
                    data[i] = set([1,2,3])  #Fuzz with set
                    data[i] = tuple([1,2,3])  #Fuzz with tuple
                    data[i] = True #fuzz with boolean
                    data[i] = False
                    data[i] = 1.0/0  #fuzz with infinity
                    data[i] = bytearray(b"bytearray") # Fuzz with bytearray
                    data[i] = memoryview(b"memoryview") #Fuzz with memoryview
                    data[i] = type("MyClass", (), {})() #Fuzz with user-defined class
                    data[i] = "a" * 1000 #Fuzz with long string
                    data[i] = [x for x in range(1000)] #Fuzz with list comprehensions
                    data[i] = {x : x * 2 for x in range(1000)} #Fuzz with dict comprehensions


                except (IndexError, TypeError, AttributeError) as e:
                    print(f"IndexError/TypeError/AttributeError in worker: {e}, thread: {thread_id}, i: {i}")

            #Error induction
            if random.random() < 0.1:
                raise ValueError(f"Error from thread {thread_id}")
            
            # Attempt to write a None value to the list.  Added more robust error handling.
            if random.random() < 0.2:
                try:
                    data[i] = None
                except (IndexError, TypeError, AttributeError) as e:
                    print(f"IndexError/TypeError/AttributeError in worker: {e}, thread: {thread_id}, i: {i}")

            # Attempt to divide by zero
            if random.random() < 0.1:
                try:
                    temp = temp / (1 if temp else 1) if temp else 0  # Prevent ZeroDivisionError if temp is zero
                except (ZeroDivisionError, TypeError, AttributeError) as e:
                    print(f"Error from thread {thread_id}: {e}")


        except Exception as e:  # Catch any unhandled exceptions
            print(f"Unhandled exception in worker: {e}, thread: {thread_id}, i: {i}")


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
        db = dbm.sqlite3.open("mydatabase.db", 'c')
        # Fuzzing with different data types and invalid values.
        for key_type in [str, bytes, int, float, bool, type(None), object, list, dict, set, frozenset, tuple]:
           try:
               db[key_type(123) * 1000] = 'value2'  # Larger keys
               db[key_type(b'\x00' * 1000)] = 'value3'  #Binary data
               db[key_type(None)] = 'value3'
               db[key_type(True)] = 'value3'
               db[key_type(False)] = 'value3'
               db[key_type(1.0/0)] = 'inf'   # Test with infinity
               
           except Exception as e:
               print(f"Error with key type {key_type}: {e}")
        db.close()

    except Exception as e:
        print(f"Database error: {e}")



if __name__ == "__main__":
    main()

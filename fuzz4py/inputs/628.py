
import threading
import time
import copy
import os
import ssl
import typing
import dbm
import gc
import sys
import datetime

def multithreaded_function(input_data, lock):
    try:
        # Simulate a long-running operation
        time.sleep(0.1)
        # Simulate side effect on global variable (vulnerability!)
        # Vulnerable line - potential for errors due to incorrect data types
        try:
            if isinstance(global_var, str) and isinstance(input_data, str):  # Important check
                global_var = input_data.replace("A", "B")
            elif isinstance(global_var, list) and isinstance(input_data, list):
                global_var.extend(input_data)
            elif isinstance(global_var, dict) and isinstance(input_data, dict):
                global_var.update(input_data)
            else:
                print(f"Thread {threading.get_ident()}: Incompatible types for replace operation.")
                return
        except AttributeError as e:
            print(f"Thread {threading.get_ident()} error: {e}")
            return
        except TypeError as e:
            print(f"Thread {threading.get_ident()} error: {e}")
            return
        lock.acquire()
        print(f"Thread {threading.get_ident()} processed {input_data} and global var is {global_var}")
        lock.release()
    except Exception as e:
        print(f"Thread {threading.get_ident()} error: {e}")


def main():
    global global_var
    global_var = "Starting value"  #Important: Make global_var global
    lock = threading.Lock()

    # Example of using copy.replace()
    # Fuzzing with non-string values for 'y' and potential errors
    try:
        data = copy.copy({"x": 10, "y": 20})
        # Fuzzing with different input types
        data_replaced = data.replace("y", 30)  
        data_replaced = data.replace("z", 30) #Add a test with missing key.
        data_replaced = data.replace(3, 30)  # Test with non-string key
    except Exception as e:
        print(f"copy.replace() error: {e}")


    threads = []
    for i in range(5):
        # Fuzzing with various input types and malformed data
        # Now including a variety of data types
        thread_data = [i, str(i), {"key": i}, datetime.datetime.now()]
        thread = threading.Thread(target=multithreaded_function, args=(thread_data, lock))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    # Example of using dbm.sqlite3, note the potential for errors without appropriate setup
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'  #fuzzing with different types
        db['key2'] = 123
        db['key3'] = b"binary_data"  #Test binary data
        db.close()
    except Exception as e:
        print(f"Database error: {e}")

    # ... (rest of the code is the same, with minimal changes for clarity and to be more fuzzing focused)
    #Example using lists
    try:
      list_data = [1, 2, 3]
      global_var = list_data
      for i in range(5):
          thread_data = str(i) + " - AAAAAA" + str(i) + "some_special_characters;:"
          thread = threading.Thread(target=multithreaded_function, args=(thread_data, lock))
          threads.append(thread)
          thread.start()

    except Exception as e:
      print(f"Error during list test: {e}")


if __name__ == "__main__":
    main()

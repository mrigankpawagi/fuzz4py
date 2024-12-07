
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def multithreaded_function(arg1, arg2, use_gil=True):
    """
    A multithreaded function demonstrating free-threading.

    Args:
        arg1: An integer argument.
        arg2: A string argument.
        use_gil: A boolean indicating whether to use the GIL.
    """
    if use_gil:
        result = arg1 + len(arg2)
    else:
        result = arg1 * len(arg2)
    time.sleep(0.1)
    return result

def fuzz_replace_protocol():
    class MyReplaceable:
        def __init__(self, value):
            self.value = value

        def __replace__(self, other):  # using the new method
            return type(self)(other)  # return a new instance

    a = MyReplaceable(1)
    b = copy.replace(a, 2)
    print(a.value)
    print(b.value)

def fuzz_dbm_sqlite():
    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1'
        db['key2'] = 'another value'
        value = db['key1']
        db.close()
        print(f"Retrieved value: {value}")
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")
        
    try:
        # Attempt to open a non-existent file
        db = dbm.open('nonexistent.db', 'c')
        db.close()
    except Exception as e:
        print(f"Error opening non-existent db: {e}")
    
def fuzz_os_timer():
    try:
        start_time = time.time()
        seconds = os.times()[4]
        end_time = time.time()
        diff = end_time - start_time
        print(f"Time elapsed using os.times() : {diff:.6f} seconds")
    except Exception as e:
        print(f"Error with os timer: {e}")
        
def fuzz_ssl():
    try:
        context = ssl.create_default_context()
        print("Default SSL context created.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

def main():
    fuzz_replace_protocol()
    fuzz_dbm_sqlite()
    fuzz_os_timer()
    fuzz_ssl()

    # Free-threading test
    thread1 = threading.Thread(target=multithreaded_function, args=(10, "testString"), kwargs={'use_gil': False})
    thread2 = threading.Thread(target=multithreaded_function, args=(20, "anotherString"))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    try:
        result = multithreaded_function(10, "test")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error in multithreaded function: {e}")

if __name__ == "__main__":
    main()


import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def multithreaded_function(arg1, arg2, use_gil=True):
    """
    A multithreaded function demonstrating free-threading.

    Args:
        arg1: An integer argument.
        arg2: A string argument.
        use_gil: A boolean indicating whether to use the GIL.
    """
    if use_gil:
        try:
            result = arg1 + len(arg2)
        except TypeError:
            return "Type Error!"
    else:
        try:
            result = arg1 * len(arg2)
            if not isinstance(result, int):
                result = "Non-integer result"
        except TypeError:
            return "Type Error!"
    time.sleep(random.uniform(0.05, 0.15))  # Introduce variability
    return result


def fuzz_replace_protocol():
    try:
        class MyReplaceable:
            def __init__(self, value):
                self.value = value

            def __replace__(self, other):
                return type(self)(other)

        a = MyReplaceable(1)
        b = copy.replace(a, "test")  # Fuzz with a string
        print(a.value)
        print(b.value)

        # Fuzzing with a different type
        c = MyReplaceable("hello")
        d = copy.replace(c, 123)
        print(c.value)
        print(d.value)
    except Exception as e:
        print(f"Error in fuzz_replace_protocol: {e}")

def fuzz_dbm_sqlite():
    try:
        db_filename = 'test_db.db'  
        db = dbm.open(db_filename, 'c')
        db['key1'] = 'value1'
        db['key2'] = b'\x00\x01\x02'  # Binary data
        try:
            value = db['key1']
            print(f"Retrieved value: {value}")
        except KeyError as e:
            print(f"KeyError in fuzz_dbm_sqlite: {e}")

        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")
    

def fuzz_os_timer():
    try:
        start_time = time.perf_counter()
        seconds = os.times()[4]
        try:
          result = os.times()[4] * 100 #Introduce calculation
        except Exception as e:
          print(f"Error calculating os.times(): {e}")
        end_time = time.perf_counter()
        diff = end_time - start_time
        print(f"Time elapsed using os.times() : {diff:.6f} seconds")
    except Exception as e:
        print(f"Error with os timer: {e}")


def fuzz_ssl():
    try:
        context = ssl.create_default_context()
        print("Default SSL context created.")
        #Fuzzing with a string
        context = ssl.create_default_context(purpose=b'client')
        print("Default SSL context with specific purpose created.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")



def main():
    fuzz_replace_protocol()
    fuzz_dbm_sqlite()
    fuzz_os_timer()
    fuzz_ssl()

    # Free-threading test (improved error handling)
    try:
        thread1 = threading.Thread(target=multithreaded_function, args=(10, "testString"), kwargs={'use_gil': False})
        thread2 = threading.Thread(target=multithreaded_function, args=(20, "anotherString"))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    except Exception as e:
        print(f"Error in free-threading setup: {e}")

    try:
        result = multithreaded_function(10, "test")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error in multithreaded function: {e}")

if __name__ == "__main__":
    main()

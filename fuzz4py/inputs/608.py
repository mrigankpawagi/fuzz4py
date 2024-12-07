
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random

def threaded_function(arg: int) -> int:
    """A threaded function that demonstrates the usage of the free-threading model and the GIL."""
    result = arg * 2
    try:
        time.sleep(random.uniform(0.05, 0.15))  # Introduce a variable delay
    except Exception as e:
        print(f"Error in sleep: {e}")
    return result


def main():
    """Main function for testing multithreading and new features."""

    # Test free-threading and JIT (potential race condition)
    args = [i for i in range(10)]
    threads = []
    for arg in args:
        threads.append(threading.Thread(target=threaded_function, args=(arg,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    #Introduce potential race condition
    global_var = 0
    for i in range(5):
        threading.Thread(target=lambda: global_var + 1).start()

    # Test copy.replace() for custom classes (with some potential issue)
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

        def __replace__(self, a: int, b: str):
            return MyClass(a, b)  # Adding a second parameter to __replace__

        def __repr__(self):
            return f"MyClass(a={self.a}, b={self.b})"


    obj = MyClass(10, "hello")
    new_obj = copy.replace(obj, a=20, b="world")  #fuzz with a b parameter
    try:
        print(obj.a, new_obj.a)
    except Exception as e:
        print(f"Error: {e}")


    #Test the dbm.sqlite3 module with invalid data (important for new modules)
    try:
        db = dbm.open('mydatabase', 'c')
        invalid_data = bytes(random.choices(range(256), k=1024))  # Random byte string
        db['key'] = invalid_data  #fuzz with bytes data
        db.close()
    except Exception as e:
        print("dbm error:", e)

    #Test  with incorrect file mode
    try:
        db = dbm.open('mydatabase2', 'x')  #Incorrect file mode will generate exception
        db['key'] = 'test'
        db.close()
    except Exception as e:
        print(f"Exception with incorrect mode: {e}")


    # Test os module timer functions (Linux-specific)
    try:
        start_time = time.perf_counter()
        result = os.times()
        end_time = time.perf_counter()
        print("os.times() execution time:", end_time - start_time)

        #fuzzing with invalid parameters
        invalid_input = "invalid_input"
        try:
            os.times(invalid_input)
        except Exception as e:
            print(f"Error with invalid parameter to os.times(): {e}")

    except Exception as e:
        print("os.times() error", e)


    # Test ssl module with a custom certificate (for new ssl changes)
    try:
        context = ssl.create_default_context()
        #Replace with a proper certificate path if you want to test with a specific one
        context.load_verify_locations("badcert.pem")  # replace with test cert  (replace with proper test certificate)
        print("SSL connection established (potentially with errors).")
    except Exception as e:
        print("ssl error:", e)
    
    #Fuzzing with a very large data and try for overflow errors
    large_data = "x" * 1024 * 1024 #1 MB
    try:
        context.check_hostname(large_data)
    except Exception as e:
        print(f"Fuzzing check_hostname with large data: {e}")


if __name__ == "__main__":
    main()


import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def worker(arg, lock):
    """A worker thread function to test free-threading."""
    # Simulate work (introducing randomness)
    sleep_time = random.uniform(0.05, 0.15)
    time.sleep(sleep_time)
    with lock:
        arg.append(1)


def main():
    # Example demonstrating free-threading with JIT potential
    arg = []
    lock = threading.Lock()
    threads = []
    
    for i in range(5):
        thread = threading.Thread(target=worker, args=(arg, lock))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
    try:
        # Introduce potential for JIT compilation via a loop (uncomment to test)
        for i in range(10000):
            arg.append(i) # This loop might be optimized by JIT
        print(arg)  # output added to test JIT compilation (will be large)


    except Exception as e:
        print(f"Error with JIT testing: {e}")
    
    # Testing docstring whitespace stripping:
    def my_function():
        """
        This is a docstring.

        """
        pass
    
    # Testing copy.replace()
    class MyClass:
        def __init__(self, a: int, b: str = "default"):  # Added default
            self.a = a
            self.b = b
        def __repr__(self):
            return f"MyClass(a={self.a}, b='{self.b}')"
        def __replace__(self, a: int = None, b: str = None):
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyClass(1, "hello")
    try:
        new_obj = copy.replace(obj, a=2, b=None) # Added b=None to mutate
        print(obj)
        print(new_obj)
    except Exception as e:
        print(f"Error with copy.replace: {e}")

    # Testing dbm.sqlite3
    try:
        d = dbm.open('mydatabase', 'c')
        d['key'] = 'value'
        d.close()
        d = dbm.open('mydatabase', 'r')
        print(d['key'])
        try:
           d['key'] = 'new_value'  # Attempt to update
        except Exception as e:
            print(f"Error Updating DBM: {e}")
        d.close()
        os.remove('mydatabase') # Clean up the database file

    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")

    # Testing os module timer functions (more robust)
    try:
        start_time = time.perf_counter()
        times_result = os.times()
        for i in range(10):  # Add a loop
            os.times()  # Repeated calls for potential issues
        end_time = time.perf_counter()
        print(f"os.times() took: {end_time - start_time} seconds")
        print(f"times_result: {times_result}") # Output the result of os.times()

    except Exception as e:
        print(f"Error with os timer: {e}")


    #Testing ssl (more robust)
    try:
        context = ssl.create_default_context()
        # Introducing a potential problem, varying context usage
        invalid_cert_path = 'invalid_cert.pem'
        try:
            context.load_verify_locations(invalid_cert_path)
            print("SSL context loaded with invalid certificate")
        except Exception as e:
            print(f"Error loading invalid certificate: {e}")
        print("SSL context created successfully (with attempts)")

    except Exception as e:
        print(f"Error with SSL: {e}")


if __name__ == "__main__":
    main()

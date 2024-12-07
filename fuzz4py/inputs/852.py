
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(arg, lock):
    """A worker thread function to test free-threading."""
    # Simulate work
    time.sleep(0.1)
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
        
    #print(arg)  # uncomment for output (not very relevant to JIT)
    
    # Testing docstring whitespace stripping:
    def my_function():
        """
        This is a docstring.
        """
        pass
    
    # Testing copy.replace()
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b
        def __repr__(self):
            return f"MyClass(a={self.a}, b='{self.b}')"
        def __replace__(self, a: int = None, b: str = None):
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyClass(1, "hello")
    new_obj = copy.replace(obj, a=2)
    print(obj)
    print(new_obj)
    
    # Testing dbm.sqlite3
    try:
        d = dbm.open('mydatabase', 'c')
        d['key'] = 'value'
        d.close()
        d = dbm.open('mydatabase', 'r')
        print(d['key'])
        d.close()

    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")

    # Testing os module timer functions (simplified)
    try:
        start_time = time.perf_counter()
        os.times()
        end_time = time.perf_counter()
        print(f"os.times() took: {end_time - start_time} seconds")


    except Exception as e:
        print(f"Error with os timer: {e}")

    #Testing ssl (simplified)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error with SSL: {e}")


if __name__ == "__main__":
    main()

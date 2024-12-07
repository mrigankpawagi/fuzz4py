
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def threaded_function(arg: int) -> int:
    """A threaded function that demonstrates the usage of the free-threading model and the GIL."""
    result = arg * 2
    time.sleep(0.1)  # Introduce a delay
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

    # Test copy.replace() for custom classes (with some potential issue)
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

        def __replace__(self, a: int):
            return MyClass(a, self.b)
    
    obj = MyClass(10, "hello")
    new_obj = copy.replace(obj, a=20)
    print(obj.a, new_obj.a) #check for memory corruption

    #Test the dbm.sqlite3 module with invalid data (important for new modules)
    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'some invalid data with \n and other weird characters\n\n\n'
        db.close()
    except Exception as e:
        print("dbm error:",e)


    # Test os module timer functions (Linux-specific)
    try:
        start_time = time.perf_counter()
        result = os.times()
        end_time = time.perf_counter()
        print("os.times() execution time:", end_time - start_time)
    except Exception as e:
        print("os.times() error",e)


    # Test ssl module with a custom certificate (for new ssl changes)
    try:
        context = ssl.create_default_context()
        #Replace with a proper certificate path if you want to test with a specific one
        context.load_verify_locations("badcert.pem")  # replace with test cert
        print("SSL connection established (potentially with errors).") 
    except Exception as e:
        print("ssl error:", e)

if __name__ == "__main__":
    main()

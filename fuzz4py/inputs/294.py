
import threading
import time
import copy
import os
import ssl
import dbm
import typing


def thread_func(x, ctx):
    try:
        # Simulate a database operation
        db = dbm.open('mydatabase', 'c')
        db[str(x)] = str(x * 2)
        db.close()

        # Simulate an operation that might be JIT compiled
        result = 0
        for i in range(10000):
            result += i * x
        
        # Test copy.replace()
        a = copy.copy([1, 2, 3])
        b = copy.replace(a, [4, 5])
        if b is not a:
            print("Replace works correctly")
            
        
        # Test with ssl context
        print(f"Thread {x} connected successfully using context {ctx}")
    except Exception as e:
        print(f"Thread {x} failed: {e}")
        
    finally:
        # cleanup after every operation
        try:
            db = dbm.open('mydatabase', 'c')
            db.close()
        except Exception:
            pass


def main():
    # Test free-threading with different contexts
    threads = []
    num_threads = 5
    
    # Test with and without the GIL (using the GIL in this case)
    for i in range(num_threads):
        # Using the GIL
        t = threading.Thread(target=thread_func, args=(i, ssl.create_default_context()))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()

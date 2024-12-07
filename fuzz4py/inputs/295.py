
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random
import sys

def thread_func(x, ctx, seed):
    try:
        # Simulate a database operation - Introduce potential errors.
        db_filename = f'mydatabase_{x}'  # Different filenames for each thread
        db = dbm.open(db_filename, 'c')
        try:
            db[str(x)] = str(x * 2 + random.randint(0,10)) # Add random data for fuzzing
            db.close()
        except Exception as e:
            print(f"Database error in thread {x}: {e}")
            raise  # Re-raise the exception

        # Simulate an operation that might be JIT compiled - Add randomness.
        result = 0
        for i in range(10000 + random.randint(-500, 500)):  # Random loop range.
            result += i * x + random.randint(-10, 10) # Add random calculation
            
        # Test copy.replace() -  More complex input and error check
        a = copy.copy([1, 2, 3, random.random()]) # Add random float
        try:
            b = copy.replace(a, [4, 5, random.randint(-100,100)])
            if b is not a:
                print("Replace works correctly")
            else:
                print("Replace failed unexpectedly")
        except Exception as e:
            print(f"Copy.replace error in thread {x}: {e}")
            raise  # Re-raise the exception

        # Test with ssl context - Introduce various certificate errors
        if seed % 2 == 0:
            ctx2 = ssl.create_default_context()
            print(f"Thread {x} connected successfully using context {ctx2}")
        else:
            try:
                # Attempt a connection with a potentially bad certificate or other SSL issues
                ctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                ctx2.verify_mode = ssl.CERT_NONE  # Disabling certificate validation
                print(f"Thread {x} connected successfully (insecure) using context {ctx2}")
            except Exception as e:
                print(f"Thread {x} failed due to bad SSL context: {e}")

    except Exception as e:
        print(f"Thread {x} failed: {e}")

        
    finally:
        try:
            # Cleanup with potential errors
            db = dbm.open(db_filename, 'c')  # Using the potentially different name.
            db.close()
        except Exception as e:
            print(f"Error during cleanup in thread {x}: {e}")


def main():
    # Test free-threading with different contexts - Introduce a random seed for variability.
    num_threads = 5
    seed = random.randint(0,100)
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=thread_func, args=(i, ssl.create_default_context(), seed)) #add a random seed
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()

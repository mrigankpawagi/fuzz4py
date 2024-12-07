
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
        db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'  # More random filenames
        db = dbm.open(db_filename, 'c')
        try:
            db[str(x)] = str(x * 2 + random.randint(0,100) * random.random())  # More random data, including a float
            db.close()
        except Exception as e:
            print(f"Database error in thread {x}: {e}")
            raise  # Re-raise the exception


        # Simulate an operation that might be JIT compiled - Add randomness.
        result = 0
        for i in range(10000 + random.randint(-500, 500)):
            result += i * x + random.randint(-10, 10)  # More randomness.
            if random.random() < 0.05:  # Introduce occasional exceptions
                raise ZeroDivisionError("JIT-compiled error") #introduce a random error

        # Test copy.replace() -  More complex input and error check
        a = copy.copy([1, 2, 3, random.random(), random.randint(-100, 100)])
        try:
            b = copy.replace(a, [4, 5, random.randint(-100,100)]) # More complex input
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
                ctx2 = ssl.create_default_context()  #create context.
                ctx2.check_hostname = bool(random.getrandbits(1)) #randomly enable check_hostname
                ctx2.verify_mode = random.choice([ssl.CERT_NONE, ssl.CERT_REQUIRED]) #randomly choose
                ctx2.load_verify_locations(os.path.abspath(random.choice(["bad_certificate.pem", "mycert.pem"]) if os.path.exists("bad_certificate.pem") else "mycert.pem"))
                socket = ctx2.wrap_socket(None, server_hostname="localhost")
                print(f"Thread {x} connected successfully (insecure) using context {ctx2}")
            except Exception as e:
                print(f"Thread {x} failed due to bad SSL context: {e}")
            
    except Exception as e:
        print(f"Thread {x} failed: {e}, seed: {seed}")  # Log the seed.

    finally:
        try:
            # Cleanup with potential errors
            db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'  # Different filenames for each thread, to test random name.
            db = dbm.open(db_filename, 'c')
            db.close()
        except Exception as e:
            print(f"Error during cleanup in thread {x}: {e}")


def main():
    num_threads = 5
    seed = random.randint(0, 100)
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=thread_func, args=(i, ssl.create_default_context(), seed))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()
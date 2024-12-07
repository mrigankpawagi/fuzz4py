
import threading
import time
import copy
import os
import ssl
import dbm
import random
import sys


def thread_func(x, ctx, seed):
    try:
        # Simulate a database operation - Introduce potential errors.
        db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
        db = dbm.open(db_filename, 'c')
        try:
            # Mutate: Introduce potential key error
            key = str(x) if random.random() < 0.5 else str(x) + 'bad_key'
            db[key] = str(x * 2 + random.randint(0, 100) * random.random())
            db.close()
        except Exception as e:
            print(f"Database error in thread {x}: {e}")
            raise

        # Simulate an operation that might be JIT compiled - Add randomness.
        result = 0
        for i in range(10000 + random.randint(-500, 500)):
            result += i * x + random.randint(-10, 10)
            if random.random() < 0.05:
                raise ZeroDivisionError("JIT-compiled error")

        # Test copy.replace() -  More complex input and error check
        a = copy.copy([1, 2, 3, random.random(), random.randint(-100, 100)])
        try:
            # Mutate:  Try to replace with different types
            if random.random() < 0.5:
                b = copy.replace(a, [4, 5, random.randint(-100, 100)])
            else:
                b = copy.replace(a, 42)  # Replace with a single integer
            if b is not a:
                print(f"Thread {x}: Replace works correctly")
            else:
                print(f"Thread {x}: Replace failed unexpectedly")
        except Exception as e:
            print(f"Thread {x}: Copy.replace error: {e}")
            raise

        # Test with ssl context - Introduce various certificate errors
        try:
            ctx2 = copy.copy(ctx)  # Crucial: Copy the context
            ctx2.check_hostname = bool(random.getrandbits(1))
            ctx2.verify_mode = random.choice([ssl.CERT_NONE, ssl.CERT_REQUIRED, ssl.CERT_OPTIONAL])
            # Crucial:  Ensure bad_certificate.pem exists or replace with a valid one.
            ctx2.load_verify_locations(os.path.abspath(random.choice(["bad_certificate.pem", "mycert.pem"]) if os.path.exists("bad_certificate.pem") else "mycert.pem"))

            # Ensure we don't crash by trying to wrap with a None socket
            try:
                ctx2.wrap_socket(None, server_hostname="localhost")
                print(f"Thread {x}: connected successfully (insecure) using context {ctx2}")
            except Exception as e:
                print(f"Thread {x}: wrap_socket failed with insecure context: {e}")



        except Exception as e:
            print(f"Thread {x}: failed due to bad SSL context: {e}")


    except Exception as e:
        print(f"Thread {x} failed: {e}, seed: {seed}")
    finally:
        try:
            db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
            if os.path.exists(db_filename):
                os.remove(db_filename)
        except Exception as e:
            print(f"Error during cleanup in thread {x}: {e}")


def main():
    num_threads = 5
    seed = random.randint(0, 100)
    ctx = ssl.create_default_context()  # Create the context only once
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=thread_func, args=(i, ctx, seed))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()

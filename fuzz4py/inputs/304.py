
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
            db[str(x)] = str(x * 2 + random.randint(0, 100) * random.random())
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
            b = copy.replace(a, [4, 5, random.randint(-100, 100)])
            if b is not a:
                print(f"Thread {x}: Replace works correctly")
            else:
                print(f"Thread {x}: Replace failed unexpectedly")
        except Exception as e:
            print(f"Thread {x}: Copy.replace error: {e}")
            raise

        # Test with ssl context - Introduce various certificate errors
        if seed % 2 == 0:
            try:
                ctx2 = ssl.create_default_context()
                print(f"Thread {x}: connected successfully using context {ctx2}")
            except Exception as e:
                print(f"Thread {x}: Error creating context: {e}")
        else:
            try:
                ctx2 = ssl.create_default_context()
                ctx2.check_hostname = bool(random.getrandbits(1))
                ctx2.verify_mode = random.choice([ssl.CERT_NONE, ssl.CERT_REQUIRED])
                # Crucial:  Ensure bad_certificate.pem exists or replace with a valid one.
                ctx2.load_verify_locations(os.path.abspath(random.choice(["bad_certificate.pem", "mycert.pem"]) if os.path.exists("bad_certificate.pem") else "mycert.pem"))
                ctx2.wrap_socket(None, server_hostname="localhost")
                print(f"Thread {x}: connected successfully (insecure) using context {ctx2}")
            except Exception as e:
                print(f"Thread {x}: failed due to bad SSL context: {e}")

    except Exception as e:
        print(f"Thread {x} failed: {e}, seed: {seed}")
    finally:
        try:
            db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
            db = dbm.open(db_filename, 'c')
            db.close()
            os.remove(db_filename)
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

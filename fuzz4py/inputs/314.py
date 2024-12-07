
import threading
import time
import copy
import os
import ssl
import dbm
import random
import sys
import typing


def thread_func(x, ctx, seed):
    try:
        # Simulate a database operation - Introduce potential errors.
        db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
        try:
            db = dbm.open(db_filename, 'c')
            # Mutate: Introduce potential key error, data corruption
            key = str(x) if random.random() < 0.5 else str(x) + 'bad_key'
            db[key] = str(x * 2 + random.randint(0, 100) * random.random())
            if random.random() < 0.2: # Data corruption attempt
                db[key] = "CORRUPTED_DATA"
            db.close()
        except Exception as e:
            print(f"Database error in thread {x}: {e}")
            raise
        except dbm.error as e:
            print(f"Database error in thread {x}: {e}")
            raise


        # Simulate an operation that might be JIT compiled - Add randomness and potential exceptions.
        result = 0
        for i in range(10000 + random.randint(-500, 500)):
            try:
                result += i * x + random.randint(-10, 10)
                if random.random() < 0.05 and x == 0:  # Introduce potential division by zero later
                   raise ZeroDivisionError
            except ZeroDivisionError as e:
                print(f"ZeroDivisionError in thread {x}: {e}")
                raise


        # Test copy.replace() -  More complex input and error check, type testing
        a = copy.copy([1, 2, 3, random.random(), random.randint(-100, 100)])
        try:
            if random.random() < 0.5:
                b = copy.replace(a, [4, 5, random.randint(-100, 100)])  #Replace with a list
            elif random.random() < 0.3:
                b = copy.replace(a, 42)  # Replace with a single integer
            elif random.random() < 0.2:
                b = copy.replace(a, "string")  # Replace with a string
            else:
                b = copy.replace(a, None) # Replace with None
            if b is not a:
                print(f"Thread {x}: Replace works correctly")
            else:
                print(f"Thread {x}: Replace failed unexpectedly")
        except Exception as e:
            print(f"Thread {x}: Copy.replace error: {e}")
            raise



        # Test with ssl context - Introduce various certificate errors, invalid context
        try:
            ctx2 = copy.copy(ctx)
            ctx2.check_hostname = bool(random.getrandbits(1))
            ctx2.verify_mode = random.choice([ssl.CERT_NONE, ssl.CERT_REQUIRED, ssl.CERT_OPTIONAL])


            # Ensure 'bad_certificate.pem' or 'mycert.pem' exists (or create dummy files)
            try:
                ctx2.load_verify_locations(os.path.abspath(random.choice(["bad_certificate.pem", "mycert.pem", "nonexistent.pem"])))
                ctx2.wrap_socket(None, server_hostname="localhost")
                print(f"Thread {x}: connected successfully (insecure) using context {ctx2}")

            except Exception as e:
                print(f"Thread {x}: wrap_socket failed with insecure context: {e}")
                print(f"Error details: {e.__cause__}") # More detailed error info

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


def race_condition_test(data):
    # Simulate a shared resource
    shared_resource = 0

    def increment():
        nonlocal shared_resource
        shared_resource += data
        time.sleep(0.001)  # Introduce a delay for potential race conditions

    threads = []
    for _ in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return shared_resource



def jit_test():
    i = 0
    while i < 1000000:
        #Likely target for JIT compilation - hot loop
        result = 2 * i + 1
        i += 1
    return result


def complex_annotation_test(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    """A function with complex type annotations to test typing module."""
    results = []
    for item in data:
        if isinstance(item, int):
            results.append(item * 2)
        elif isinstance(item, str):
           # Handle strings in the way you want
           try:
               results.append(int(item)) #Example: convert to integer
           except ValueError as e:
               print(f"Error converting string to integer: {e}")
               results.append(-1)  # Or handle the error in another way
    return results


def test_replace(data):
  #Test for copy.replace()
  class MyData:
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __replace__(self, *, a=None, b=None):
      return type(self)(a if a is not None else self.a, b if b is not None else self.b)
  
  original_data = MyData(1, 2)
  new_data = copy.replace(original_data, a=3)  
  return new_data.a



def main():
    # Test free-threading: race condition with varying inputs
    print(f"Race condition test (using a large integer): {race_condition_test(10000)}")

    # Test JIT compiler
    result = jit_test()
    print(f"JIT test result: {result}")


    #Test Complex Type Annotations
    complex_data = [1, 2, "3", 4, "5", "abc"] # Added a string that can't be converted
    results = complex_annotation_test(complex_data)
    print(f"Complex type annotation test results: {results}")

    #Test for copy.replace()
    result = test_replace(1)
    print(f"Replace test result: {result}")

    # Added error handling for cases where os.times is not available
    try:
        timer_result = os.times()
        print(f"Timer result: {timer_result}")
    except AttributeError as e:
        print(f"AttributeError: {e}. os.times() might not be available on this platform")


if __name__ == "__main__":
    main()

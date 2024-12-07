
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import contextvars
import random
import sys


def threaded_function(arg: int, ctx: contextvars.ContextVar) -> int:
    """
    A threaded function demonstrating free-threading and JIT compilation potential.
    """
    delay = random.uniform(0.0001, 0.01)  # Introduce random delay
    try:
        time.sleep(delay)  # Introduce a small delay
    except (TypeError, ValueError, AttributeError, OSError) as e:
        print(f"Error in time.sleep: {e}")
    try:
        if arg is None:
            result = 0
        elif isinstance(arg, int):
            result = arg * 2
        elif isinstance(arg, str):
            result = len(arg)
        elif isinstance(arg, list):
            result = len(arg)
        else:
            result = 0
    except (TypeError, ValueError, AttributeError):
        result = 0

    current_context = ctx.get()
    if current_context == "JIT_ON":
        print(f"JIT active: Calculated {result}")
    else:
        print(f"No JIT: Calculated {result}")
    return result


def main():
    ctx = contextvars.ContextVar("execution_context")
    ctx.set("No JIT")

    threads = []
    for i in range(5):
        thread = threading.Thread(target=threaded_function, args=(i, ctx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with ctx.set("JIT_ON"):
        print("Context set to JIT_ON")
        for i in range(-5, 5):  # Fuzz with negative and large numbers
            try:
                result = threaded_function(i, ctx)
            except Exception as e:
                print(f"Error in threaded_function: {e}")
    
    # Example of manipulating an object with copy.replace()
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

        def __copy__(self):
            return MyClass(self.a, self.b)

        def __replace__(self, a: typing.Optional[int] = None, b: typing.Optional[str] = None) -> "MyClass":
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)
    
    obj = MyClass(1, "abc")

    fuzz_data = [10, "def", None, True, [], {}, 3.14, "123", b"abc", 2**10, object()]  #Add object() for fuzzing with object type
    for a_val in fuzz_data:
        for b_val in fuzz_data:
            try:
                replaced_obj = copy.copy(obj)
                replaced_obj = replaced_obj.__replace__(a=a_val, b=b_val)
                print(f"Original object: {obj.a}, {obj.b}")
                print(f"Replaced object: {replaced_obj.a}, {replaced_obj.b}")
            except Exception as e:
                print(f"Error during replace: {e}")

    try:
        times = os.times()
        if len(times) >= 5:
            time_value = times[4]
            print(f"Time from os.times(): {time_value}")
        else:
            print("os.times() not available on this platform or doesn't return enough elements")

        # More comprehensive fuzzing of os.times()
        for i in range(0, 1000, 10):
            print(f"fuzzing os.times() with {i}")
            os.times()

    except (AttributeError, IndexError, OSError) as e:
        print(f"Error accessing os.times(): {e}")

    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        print(db['key'])
        for i in range(5):
            fuzz_key = str(random.randint(1, 1000))
            fuzz_value = str(random.randint(1, 1000))
            db[fuzz_key] = fuzz_value
            try:
                db[fuzz_key] = None  # Potential corruption test
                db[fuzz_key] = 1234567890  # Larger value test
            except Exception as e:
                print(f"Database error: {e}")
        db.close()
    except (dbm.error, OSError) as e:
        print(f"Error interacting with dbm.sqlite3: {e}")


    # Simulate an SSL connection - more robust fuzzing
    try:
        context = ssl.create_default_context()
        print("SSL Context Created")
        # Replace with actual certificate fuzzing
        for i in range(5):
            try:
                # Placeholder - needs real certificate handling
                context.load_verify_locations(None)  # Replace with 'badcert.crt' for testing errors
                print(f"Attempting connection {i}")
            except Exception as e:
                print(f"SSL Verification Error {i}: {e}")

    except Exception as e:
        print(f"Error with SSL: {e}")

if __name__ == "__main__":
    main()

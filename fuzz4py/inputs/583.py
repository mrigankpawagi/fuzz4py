
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import contextvars
import random

def threaded_function(arg: int, ctx: contextvars.ContextVar) -> int:
    """
    A threaded function demonstrating free-threading and JIT compilation potential.
    """
    delay = random.uniform(0.0001, 0.01)  # Introduce random delay
    time.sleep(delay)  # Introduce a small delay
    try:
        result = arg * 2 if arg is not None else 0
    except (TypeError, ValueError):  # Catch more potential errors
        result = 0

    current_context = ctx.get()
    if current_context == "JIT_ON":
        print(f"JIT active: Calculated {result}")
    else:
        print(f"No JIT: Calculated {result}")
    return result

def main():
    ctx = contextvars.ContextVar("execution_context")
    ctx.set("No JIT")  # Initialize context

    threads = []
    for i in range(5):
        thread = threading.Thread(target=threaded_function, args=(i, ctx))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    with ctx.set("JIT_ON"):
        print("Context set to JIT_ON")
        for i in range(3):
            try:
                threaded_function(i, ctx)
            except Exception as e:
                print(f"Error in threaded_function: {e}")


    # Example of manipulating an object with copy.replace()
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

        def __copy__(self):
            return MyClass(self.a, self.b)
        
        def __replace__(self, a: typing.Optional[int]=None, b: typing.Optional[str]=None) -> "MyClass":
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyClass(1, "abc")
    
    fuzz_data = [10, "def", None, True, [], {}, 3.14, "123", b"abc"]  # More diverse fuzz data
    for a_val in fuzz_data:
        for b_val in fuzz_data:
            try:
                replaced_obj = copy.copy(obj)  # Ensure a copy is made first
                replaced_obj = replaced_obj.__replace__(a=a_val, b=b_val)
                print(f"Original object: {obj.a}, {obj.b}")
                print(f"Replaced object: {replaced_obj.a}, {replaced_obj.b}")
            except Exception as e:
                print(f"Error during replace: {e}")



    # Example of interacting with the os module's timer functions (only if available)
    try:
        # Access specific element
        if len(os.times()) >= 5:
          time_value = os.times()[4]
          print(f"Time from os.times(): {time_value}")
        fuzz_time = random.randint(1, 1000)  # Fuzzing with random values
        print(f"Fuzzed Time: {fuzz_time}")
    except (AttributeError, IndexError, OSError):  # Handle potential errors more comprehensively
        print("os.times() not available on this platform or doesn't return enough elements")

    # Example using dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')  # Use 'c' for create mode
        db['key'] = 'value'
        print(db['key'])
        # Fuzzing with various data types.
        for i in range(5):
            fuzz_key = str(random.randint(1, 1000))
            fuzz_value = str(random.randint(1, 1000))  # fuzz value
            db[fuzz_key] = fuzz_value
        db.close()
    except (dbm.error, OSError) as e:
        print(f"Error interacting with dbm.sqlite3: {e}")


    # Simulate an SSL connection
    try:
        context = ssl.create_default_context()
        print("SSL Context Created")
    except Exception as e:
        print(f"Error with SSL: {e}")


if __name__ == "__main__":
    main()

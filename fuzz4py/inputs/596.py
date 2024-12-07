
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
import datetime

def threaded_function(arg, ctx):
    """
    A threaded function demonstrating free-threading and JIT compilation potential.
    """
    delay = random.uniform(0.0001, 0.01)
    try:
        time.sleep(delay)
    except (TypeError, ValueError, AttributeError, OSError) as e:
        print(f"Error in time.sleep: {e}")
        return 0  # Return 0 on error

    try:
        if arg is None:
            result = 0
        elif isinstance(arg, (int, float)):
            result = arg * 2
        elif isinstance(arg, str):
            result = len(arg)
        elif isinstance(arg, list):
            result = len(arg)
        elif isinstance(arg, dict):
            result = len(arg)
        elif hasattr(arg, "__len__"):
            result = len(arg)
        elif callable(arg):
            try:
                result = arg()
            except Exception as e:
                print(f"Error calling callable object: {e}")
                result = 0
        else:
            try:
                result = hash(arg)
            except TypeError:
                result = 0
    except TypeError as e:
        print(f"Error during result calculation: {e}")
        return 0  # Return 0 on error

    current_context = ctx.get()
    if current_context == "JIT_ON":
        print(f"JIT active: Calculated {result} at {datetime.datetime.now()}")
    else:
        print(f"No JIT: Calculated {result} at {datetime.datetime.now()}")
    return result


def main():
    ctx = contextvars.ContextVar("execution_context")
    ctx.set("No JIT")

    threads = []
    for i in range(10):
        thread = threading.Thread(target=threaded_function, args=(i, ctx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with ctx.set("JIT_ON"):
        print("Context set to JIT_ON")
        for i in range(-10, 11):
            try:
                result = threaded_function(i, ctx)
                if result > 1000:
                    raise ValueError(f"Result {result} too high")
            except (Exception, ValueError) as e:
                print(f"Error in threaded_function: {e}")


        # Example with complex objects
        try:
            # Fuzzing with various types
            threaded_function("hello", ctx)
            threaded_function([1, 2, 3, 4], ctx)
            threaded_function({"a": 1, "b": 2}, ctx)

            # Example with a custom class
            my_object = MyClass(10, 20)
            threaded_function(my_object, ctx)

            # Callable object
            def my_func():
                return 42
            threaded_function(my_func, ctx)

            # Lambda
            threaded_function(lambda: 10000, ctx)

            # Complex object with __len__
            complex_object = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            threaded_function(complex_object, ctx)

            # Complex object with __hash__
            my_complex_object = MyClass(10, 20)
            threaded_function(my_complex_object, ctx)

        except Exception as e:
            print(f"Error in threaded_function: {e}")


    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __copy__(self):
            return copy.copy(self)

        def __replace__(self, a=None, b=None):
            try:
                return MyClass(a if a is not None else self.a, b if b is not None else self.b)
            except Exception as e:
                print(f"Error in __replace__: {e}")
                return None

        def __len__(self):
            return 5

        def __hash__(self):
            return hash((self.a, self.b))


    # Example usage (unchanged)
    my_object = MyClass(10, 20)
    copied_object = my_object.__copy__()
    try:
        replaced_object = my_object.__replace__(a=30)
    except Exception as e:
        print(f"Error in __replace__: {e}")

if __name__ == "__main__":
    main()


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
        
    try:
      result = 0
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
      elif callable(arg):  # Add check for callable objects
        try:
          result = arg()
        except Exception as e:
            print(f"Error calling callable object: {e}")
            result = 0
      else:
        try:
          result = hash(arg)
        except TypeError:
          result = 0  # Handle potential TypeError here

    except TypeError as e:
        print(f"Error during result calculation: {e}")
        result = 0

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
          
            #Fuzzing with various types, including unexpected types
            result = threaded_function("hello",ctx)
            result = threaded_function([1,2,3,4],ctx)
            result = threaded_function({"a": 1, "b": 2}, ctx)
            
            # Example with a custom class (using a lambda, adding a potential race condition)
            my_object = MyClass(10, 20)
            result = threaded_function(my_object, ctx)
            
            # Add a fuzzing case for a callable object
            def my_func():
                return 42
            result = threaded_function(my_func, ctx)
            
            #Fuzz with a lambda
            result = threaded_function(lambda: 10000, ctx)

            # Example with a complex object with __len__
            complex_object = [1,2,3,4,5,6,7,8,9,10]
            result = threaded_function(complex_object, ctx)

            # Example with a complex object with __hash__
            my_complex_object = MyClass(10, 20)
            result = threaded_function(my_complex_object, ctx)

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
            return 5 #Example: Define a __len__ method.
        def __hash__(self):  # Example of an __hash__ method
            return hash((self.a, self.b))


    #Example usage of MyClass (replace with your intended use case)
    my_object = MyClass(10, 20)
    copied_object = my_object.__copy__()
    replaced_object = my_object.__replace__(a=30)


if __name__ == "__main__":
    main()

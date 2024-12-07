
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
    
    # Add more complex types and checks, including None
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
          try:
            result = len(arg)
          except TypeError:
            result = 0
        else:
            try:
              result = hash(arg)
            except TypeError:
              result = 0
            
    except (TypeError, ValueError, AttributeError, Exception):
        result = 0
    
    current_context = ctx.get()
    if current_context == "JIT_ON":
        print(f"JIT active: Calculated {result} at {datetime.datetime.now()}")  # Added timestamp
    else:
        print(f"No JIT: Calculated {result} at {datetime.datetime.now()}")  # Added timestamp
    return result

def main():
    ctx = contextvars.ContextVar("execution_context")
    ctx.set("No JIT")

    threads = []
    for i in range(10):  # Increased number of threads
        thread = threading.Thread(target=threaded_function, args=(i, ctx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with ctx.set("JIT_ON"):
        print("Context set to JIT_ON")
        for i in range(-10, 10): #wider range
          try:
              result = threaded_function(i, ctx)
          except Exception as e:
              print(f"Error in threaded_function: {e}")

    # ... (rest of the code remains largely unchanged)
    
    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __copy__(self):
            return copy.copy(self)  # Use copy.copy
        def __replace__(self, a=None, b=None):
          return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    # ... (rest of the code remains largely unchanged)


if __name__ == "__main__":
    main()

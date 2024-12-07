
import threading
import copy
import os
import ssl
import time
import typing

def complex_function(data: typing.List[int], verbose: bool = False) -> typing.List[int]:
    """
    A function demonstrating free-threading and JIT compiler potential issues.
    """
    if verbose:
        print("Starting complex_function")

    result = []
    for i in data:
        # This is a hot loop that may be JIT-compiled.
        if i > 10:
            result.append(i * 2)

    if verbose:
        print("Finished complex_function")

    return result


def test_free_threading():
    data = [1, 2, 3, 4, 5, 12, 15, 20]
    
    #Testing threading with and without the GIL
    threads = []
    for i in range(5):
      threads.append(threading.Thread(target = complex_function, args=([data],)))  
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()
  
    print("threading with GIL")

    threads = []
    for i in range(5):
      threads.append(threading.Thread(target = complex_function, args=([data], False)))  
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()

    print("threading without GIL")
    return True

def fuzz_replace(obj):
    if hasattr(obj, '__replace__'):
        try:
            replaced_obj = copy.replace(obj, some_attribute=42)
            return replaced_obj
        except Exception as e:
            print(f"Exception during replace: {e}")


if __name__ == "__main__":
    try:
        test_free_threading()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    #Fuzzing copy.replace
    class ReplaceableObject:
        def __init__(self, value):
            self.value = value
        
        def __replace__(self, **changes):
          self.value = changes.get('some_attribute', self.value)
          return self
          

    obj = ReplaceableObject(10)
    fuzz_replace(obj)
    print(f"Object after replacement: {obj.value}")
    try:
      # Fuzzing os.timer
      t = time.perf_counter()
      result = os.times()
      t = time.perf_counter() - t
      print(result)
      print(f"Time taken for os.times(): {t}")
    except Exception as e:
        print(f"Error in os.times(): {e}")



    # Simple ssl example (very basic - more extensive fuzzing would be needed)
    context = ssl.create_default_context()
    print("SSL context created.")

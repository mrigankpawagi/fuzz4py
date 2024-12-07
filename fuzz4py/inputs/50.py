
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def test_free_threading(arg1: int, arg2: str) -> None:
    """
    This function demonstrates free-threading, possibly using a C extension.
    """
    
    # Simulate a long-running task in a separate thread
    def worker(arg):
        
        # Potential race condition if not properly synchronized.
        global shared_resource 
        shared_resource = arg * 2 
        time.sleep(0.1)

    # Using threading.Thread directly, potentially problematic
    t1 = threading.Thread(target=worker, args=(arg1,))
    t2 = threading.Thread(target=worker, args=(arg2,))  # Notice the different argument!
    threads = [t1, t2]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Additional checks, ensuring the threads are actually operating
    if shared_resource != arg1 * 2:
        raise Exception("Incorrect result shared_resource")
    if shared_resource != arg2 * 2:
        raise Exception("Incorrect result shared_resource")
    # ... additional checks ...
    
    return None


#Example usage (fuzzing would vary inputs)

shared_resource = 0  # Initial shared resource

try:
    test_free_threading(10, "fuzz")
except Exception as e:
    print(f"Error in test_free_threading: {e}")


# Fuzzing dbm.sqlite3
try:
  db = dbm.open('test.db', 'c')
  db['key1'] = 'value1'
  db['key2'] = 'very-long-value-to-test-storage-capacity'  # Fuzzing with a long value
  value = db['key1']
  db.close()
except Exception as e:
  print(f"Error in dbm.sqlite3 fuzzing: {e}")


# Fuzzing os.times()
try:
    start_time = time.time()
    os.times()
    end_time = time.time()
    diff_time = end_time - start_time
    print(f"Time taken by os.times(): {diff_time}")

except Exception as e:
  print(f"Error in os.times() fuzzing: {e}")



# Example using typing annotations with lambdas (fuzzed by varying the input and lambda)
def complex_function(arg: typing.Union[int, typing.Callable[[int], int]]) -> int:
  if callable(arg):
    result = arg(10)
  elif isinstance(arg, int):
    result = arg + 10
  else:
    raise TypeError("Invalid argument type")
  return result
try:
    result = complex_function(lambda x: x * 2)  # Example using a lambda
    print(result) 
except Exception as e:
    print(f"Error in typing annotation fuzzing: {e}")


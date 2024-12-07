
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
    
    shared_resource = 0  # Initialize shared resource

    def worker(arg):
        nonlocal shared_resource # Use nonlocal keyword
        # Introduce potential race condition by not using a lock.
        shared_resource = arg * 2
        time.sleep(0.1 * arg1) # Vary the sleep time

    t1 = threading.Thread(target=worker, args=(arg1,))
    t2 = threading.Thread(target=worker, args=(int(arg2),)) # Convert arg2 to int. Critical for robustness

    threads = [t1, t2]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    try:  # Wrap in a try/except to handle potential errors. Crucial for robustness.
        if shared_resource != arg1 * 2:
            raise ValueError("Incorrect result for arg1")
        if shared_resource != int(arg2) * 2:
            raise ValueError("Incorrect result for arg2")
    except ValueError as e:
        print(f"Error in test_free_threading: {e}")
    return None


#Example usage (fuzzing would vary inputs)

shared_resource = 0  # Initial shared resource

try:
    test_free_threading(10, "20")
    test_free_threading(0, "abc") # Test with invalid input
    test_free_threading(-5, "10")  # Negative values
    test_free_threading(10, "-10") # Negative argument 
except Exception as e:
    print(f"Error in test_free_threading: {e}")


# Fuzzing dbm.sqlite3 (Robustness enhanced)
try:
  db = dbm.open('test.db', 'c')
  db['key1'] = 'value1'
  db['key2'] = 'a' * 10000  # Fuzzing with a long value (limit)
  db['key3'] = b'\x00\x01\xff' #Fuzz with binary data
  value = db['key1']
  db.close()
except (dbm.error, OSError) as e:
  print(f"Error in dbm.sqlite3 fuzzing: {e}")


# Fuzzing os.times() (with potential errors and varying inputs)
try:
    start_time = time.time()
    os.times()
    end_time = time.time()
    diff_time = end_time - start_time
    print(f"Time taken by os.times(): {diff_time:.6f}")
except Exception as e:
  print(f"Error in os.times() fuzzing: {e}")


# Example using typing annotations with lambdas (fuzzed by varying the input and lambda)
def complex_function(arg: typing.Union[int, typing.Callable[[int], int]]) -> int:
  if callable(arg):
    try:
      result = arg(10)
    except Exception as e:
        print(f"Error in lambda: {e}")
        return -1 # Return a specific value to indicate error
  elif isinstance(arg, int):
    result = arg + 10
  else:
    raise TypeError("Invalid argument type")
  return result


try:
  result = complex_function(lambda x: x * 2)  # Example using a lambda
  result = complex_function(10)
  result = complex_function("not a callable")  # Test with non-callable input
  result = complex_function(lambda x: x / 0) # Test for exceptions
  print(result)
except Exception as e:
    print(f"Error in typing annotation fuzzing: {e}")

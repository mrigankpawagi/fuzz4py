
import threading
import time
import copy
import os
import ssl
import dbm
import typing
import random

def complex_function(arg1: typing.List[int], arg2: typing.Dict[str, str]) -> str:
    """
    This function demonstrates a complex computation.
    """
    try:
        result = ""
        for i in arg1:
          # Introduce potential TypeError by trying to add different types
          try:
            result += str(i)
          except TypeError as e:
            return str(e)
        if arg2:
          try:
            result += arg2["key"]
          except KeyError as e:
            return str(e)
        return result
    except (KeyError, TypeError) as e:
        return str(e)
  

def multithreaded_example(data: list[int]) -> None:
  """
  A multi-threaded example demonstrating potential race conditions.  This is intended to stress the free-threading implementation.
  """
  lock = threading.Lock()
  results = []
  
  threads = []
  for i in data:
      t = threading.Thread(target=process_data, args=(i, lock, results))
      threads.append(t)
      # Introduce random delays in thread start
      time.sleep(random.uniform(0, 0.05))
      t.start()
  
  for t in threads:
      t.join()

  print(f"Final results: {results}")


def process_data(data_point: int, lock: threading.Lock, results: list) -> None:
  """
  Simulates a process that may take significant time."""
  
  #Simulate some work
  time.sleep(random.uniform(0.05, 0.15))  # More varied sleep times
  
  lock.acquire()
  try:
    # Introduce potential errors by making arg2 a different type
    results.append(complex_function([data_point], {"key": "Value", "another_key": random.randint(0, 10)}))  
  except Exception as e:
    results.append(str(e)) #Handle exceptions
  finally:
    lock.release()


if __name__ == "__main__":
  #Example Usage - Fuzzing these values is important
  # Fuzz with different data types and sizes
  data_list = [random.randint(-100, 100) for _ in range(random.randint(2,10))]

  multithreaded_example(data_list)
  
  #Demonstrating dbm.sqlite3 interaction (highly simplified) - Fuzz different input types
  try:
      # Fuzz different file names and modes
      db_name = f"test{random.randint(1,100)}.db"
      db = dbm.open(db_name, "c")
      # Fuzz input with non-string data
      db["key"] = random.randint(0, 100)
      db.close()
      print(f"Database operation successful for {db_name}.")
  except Exception as e:
      print(f"Error in database operation: {e}")
  
  try:
    # Example with ssl and potentially malformed certificate
    # Fuzz with different certificate paths
    certificate_path = f"/tmp/fuzzcert{random.randint(1,100)}.pem"
    try:
        with open(certificate_path, 'w') as f:  
            f.write("Test certificate")
    except IOError:
        print("Error creating test certificate")
    context = ssl.create_default_context()
    print("SSL context creation successful")
  except Exception as e:
      print(f"Error in SSL context creation: {e}")


  # Example illustrating annotation scope.  Fuzzing this with different types and expressions is crucial
  # Fuzz with different types and values
  some_var: typing.List[int] = [random.randint(0, 10) for _ in range(random.randint(2, 5))]
  print(some_var)


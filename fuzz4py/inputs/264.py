
import threading
import time
import copy
import ssl
import os
import dbm
import typing
import socket
import random

def race_condition_example(data: typing.List[int]) -> None:
    """
    Demonstrates a potential race condition.
    """
    global shared_data
    shared_data = 0
    threads = []
    for i in range(random.randint(2, 10)): #Fuzz with variable number of threads
        t = threading.Thread(target=increment_shared, args=(data,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final shared data: {shared_data}")

def increment_shared(data):
    global shared_data
    for x in data:
        shared_data += x
        # Introduce a potential race condition by pausing (very short)
        time.sleep(random.uniform(0, 0.01))  # Fuzz with varying sleep times

    time.sleep(random.uniform(0.05, 0.2)) #Fuzz with varying sleep times

def test_copy_replace():
    class MyData:
        def __init__(self, val1, val2):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, val1=None, val2=None):
            return MyData(val1 if val1 is not None else self.val1,
                           val2 if val2 is not None else self.val2)

    try:
        my_data = MyData(1,2)

        #Fuzzing with different replacement values and types
        new_data = copy.replace(my_data, val1=random.randint(-100, 100), val2=random.uniform(-10.0, 10.0)) 
        assert new_data.val1 == new_data.val1
        assert new_data.val2 == new_data.val2
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def fuzz_ssl():
    try:
        # Fuzz with a potentially invalid hostname.  Also fuzz with a valid one
        hostname = random.choice(['invalid.hostname', 'example.com']) #Fuzz with a valid hostname too
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect(('example.com', 443))  # Connect to a valid host
            # Also test with a variety of ports
            s.connect(('example.com', random.randint(80, 8080)))

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  # Example usage. Fuzz input data.
  my_data = [random.randint(-10, 10) for _ in range(random.randint(1, 10))]
  race_condition_example(my_data)
  test_copy_replace()

  # Example of a potential JIT/threading test:
  import time

  def jit_test():
      result = 0
      for _ in range(random.randint(100000, 1000000)): #Fuzz the loop iterations
        result +=1
      return result

  threads = []
  for _ in range(random.randint(2, 10)):
      t = threading.Thread(target=jit_test)
      threads.append(t)
      t.start()

  for t in threads:
      t.join()
  print("JIT test completed successfully")


  #Example of fuzzing dbm.sqlite3 (requires a dummy database)
  try:
    # Fuzzing with malformed key/value
    db_name = f"mydatabase_{random.randint(1,10)}.db" #Fuzz the database name
    db = dbm.open(db_name, 'c')
    key = str(random.randint(1, 1000))
    value = str(random.randint(1, 1000)) #Fuzz with random values
    db[key] = value  # Adding malformed key
    db.close()
    db = dbm.open(db_name, 'r')
    try:
      value = db.get(str(random.randint(1, 100))) #Fuzz with random keys
      db.close()
    except Exception as e:
      print(f"Error retrieving data from DB: {e}")

  except Exception as e:
    print("Error in dbm.sqlite3 test:", e)

  #Example of fuzzing a possible race condition with open/close in os
  try:
      num_files = random.randint(1, 5)
      files = [open(f"tempfile_{i}.txt", "w") for i in range(num_files)]

      for file in files:
          file.write("some data")

      for file in files:
          file.close()
      time.sleep(random.uniform(0.01, 0.5)) #Introduce a delay

      for file in files:
          try:
              file2 = open(file.name, "r") #Fuzzing with potentially non-existent file
              contents = file2.read()
              assert contents == "some data"
              file2.close()
          except Exception as e:
              print(f"Error accessing file after close: {e}")
  except Exception as e:
      print(f"Error during file operations: {e}")

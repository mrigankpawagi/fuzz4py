
import threading
import time
import copy
import ssl
import os
import dbm
import typing
import socket

def race_condition_example(data: typing.List[int]) -> None:
    """
    Demonstrates a potential race condition.
    """
    global shared_data
    shared_data = 0
    threads = []
    for i in range(5):
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
        time.sleep(0.001)  

    time.sleep(0.1)

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
        new_data = copy.replace(my_data, val1=10, val2=20)  # Attempt replacement of both values
        assert new_data.val1 == 10
        assert new_data.val2 == 20
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def fuzz_ssl():
    try:
        # Fuzz with a potentially invalid hostname.
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='invalid.hostname') as s:
            s.connect(('example.com', 443))  # Connect to a valid host
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  # Example usage.
  my_data = [1, 2, 3, 4, 5]
  race_condition_example(my_data)
  test_copy_replace()

  # Example of a potential JIT/threading test:
  import time

  def jit_test():
      result = 0
      for _ in range(1000000):
        result +=1
      return result

  threads = []
  for _ in range(5):
      t = threading.Thread(target=jit_test)
      threads.append(t)
      t.start()

  for t in threads:
      t.join()
  print("JIT test completed successfully")


  #Example of fuzzing dbm.sqlite3 (requires a dummy database)
  try:
    # Fuzzing with malformed key
    db = dbm.open('mydatabase', 'c')  # Create or open the database
    db['key1'] = 'value1'
    db['key with space'] = 'value2'  # Malformed key
    db.close()
    db = dbm.open('mydatabase', 'r')
    value = db.get('key with space') # Attempt to retrieve malformed key
    db.close()
  except Exception as e:
    print("Error in dbm.sqlite3 test:", e)

  #Example of fuzzing a possible race condition with open/close in os
  try:
      files = [open(f"tempfile_{i}.txt", "w") for i in range(3)]

      for file in files:
          file.write("some data")

      for file in files:
          file.close()
      time.sleep(0.1) #Introduce a delay

      for file in files:
          try:
            file2 = open(file.name, "r")  # Attempt to open a potentially deleted file
            contents = file2.read()
            assert contents == "some data"
            file2.close()
          except Exception as e:
            print(f"Error accessing file after close: {e}")
  except Exception as e:
      print(f"Error during file operations: {e}")

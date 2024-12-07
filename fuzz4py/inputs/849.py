
import threading
import copy
import os
import time
import ssl
import typing
import dbm
import sys

# Fuzzing complex type annotations
def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
          try:
            result.append(int(item))
          except ValueError:
            result.append(0)

    return result


# Fuzzing free-threading and GIL
def worker(data):
    try:
        time.sleep(1)  #Simulate work
        result = process_data(data)
        print(f"Thread {threading.current_thread().name}: {result}")
    except Exception as e:
        print(f"Error in thread {threading.current_thread().name}: {e}")

if __name__ == "__main__":
    # Using os.getpid() for testing differences in GIL behavior
    data_for_threads = [1, 2, '3', 'abc', 5,6] * 100

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data_for_threads,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()



    # Fuzzing dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(f"Retrieved value: {value}")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")

    # Fuzzing os.times()
    try:
        start_time = time.time()
        os.times()
        end_time = time.time()
        print(f"Time taken by os.times(): {end_time - start_time}")
    except Exception as e:
        print(f"Error with os.times(): {e}")


    # Fuzzing SSL with certificates
    try:
        context = ssl.create_default_context()
        # In a real application, this would be a certificate from a file.
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE # Crucial for fuzzing, skip verification
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error with SSL: {e}")


    #Example of copy.replace()
    try:
      class ReplaceableObject:
          def __init__(self, value):
              self.value = value
          def __replace__(self, value):
              return ReplaceableObject(value)
      obj1 = ReplaceableObject(5)
      obj2 = copy.copy(obj1)

      obj1.value = 10
      print(obj1.value)
      print(obj2.value)
    except Exception as e:
      print(f"Error with copy.replace(): {e}")


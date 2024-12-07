
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys

def worker(arg: int, lock: threading.Lock, extra_data=None):
    lock.acquire()
    try:
        time.sleep(arg)  # Potential race condition
        if extra_data is not None:
          print(f"Thread {threading.current_thread().name} finished with arg: {arg}, Extra Data: {extra_data}")
        else:
          print(f"Thread {threading.current_thread().name} finished with arg: {arg}")
    except Exception as e:
        print(f"Worker Error: {e}")
    finally:
        lock.release()


def main():
    lock = threading.Lock()
    threads = []
    for i in range(5):
        extra_data = random.randint(10, 100)  # Introduce extra data
        t = threading.Thread(target=worker, args=(i, lock, extra_data))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    # Example with copy.replace()
    class MyObject:
        def __init__(self, value):
            self.value = value

        def __replace__(self, value=None):
            return MyObject(value or self.value)

        # Add a potentially problematic method
        def modify_value(self, multiplier):
            self.value *= multiplier

    obj = MyObject(5)
    new_obj = copy.replace(obj)  # Testing replace protocol
    print(new_obj.value)
    try:
        new_obj.modify_value(2)
        print(new_obj.value)
    except Exception as e:
      print(f"Error modifying value: {e}")


    # Example with dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        value = db['key']
        print(value)
        db.close()
    except Exception as e:
        print(f"Error with dbm: {e}")


    try:
        # Example with os.times() - Introduce potential error
        t = os.times()
        print(f"CPU times: {t}")
        os.times()
    except Exception as e:
        print(f"Error with os.times(): {e}")
    
    # Fuzzing ssl.create_default_context()
    try:
      context = ssl.create_default_context()
      print("SSL context created successfully.")
      # Test with invalid certificate (simplified)
      context.load_verify_locations(cafile=None)
      context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
      print(context)
    except Exception as e:
        print(f"Error with ssl.create_default_context(): {e}")

    # Complex type annotation example
    def annotated_function(arg: typing.List[typing.Tuple[int, str]]) -> typing.Dict[str, int]:
        try:
          return {x[0]: x[1] for x in arg}  # Accessing the incorrect index
        except IndexError as e:
          print(f"Index error in function: {e}")
          return {}

    result = annotated_function([(1, 'a'), (2, 'b')])
    print(result)

    # Second program's functions (with added error handling)
    def worker(data, lock):
        try:
            db = dbm.open("mydatabase", 'c')  # 'c' for creation
            # Introduce potential errors here. 
            db[str(data)] = str(data * 2)  
            db.close()
        except (dbm.error,TypeError,KeyError, OSError) as e:  # More specific errors
            lock.acquire()
            print(f"Worker Error: {e}")
            lock.release()
            return  # Avoid continuing if there's an error

    def main2():
      data_list = [1, 2, 3, 4, 5, "abc", 6.7]  # More diverse data
      lock = threading.Lock()

      threads = []
      for data in data_list:
          thread = threading.Thread(target=worker, args=(data, lock))
          threads.append(thread)
          thread.start()

      for thread in threads:
          thread.join()


      try:
          with dbm.open("mydatabase", 'r') as db:
              for key in db:
                  value = db[key]
                  print(f"Key: {key}, Value: {value}")
      except (dbm.error,FileNotFoundError) as e:
          print(f"Error accessing database: {e}")
      finally:
          try:
              os.remove("mydatabase")  # Remove the database file
          except OSError:
              pass


    if __name__ == "__main__":
        main2()


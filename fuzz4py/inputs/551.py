
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def my_function(arg1: int, arg2: str) -> str:
    """
    A function that does something.

    Args:
        arg1: An integer.
        arg2: A string.
    
    Returns:
        A string.
    """
    # Simulate a long computation
    time.sleep(0.01)
    if arg1 < 0:
        raise ValueError("arg1 cannot be negative")  # Introduce error handling
    return f"Result for arg1: {arg1}, arg2: {arg2}"


def worker(arg1, arg2):
    try:
        result = my_function(arg1, arg2)
        print(f"Thread {threading.current_thread().name}: {result}")
    except ValueError as e:
      print(f"Error in worker thread {threading.current_thread().name}: {e}")



def test_free_threading():
    
    # Demonstrate free-threading
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i, "Thread input "+str(i)))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def test_copy_replace():
  class MyClass:
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __replace__(self, **kwargs):
        # Introduce a potential error
        if kwargs.get('a') is None:
            raise ValueError("a cannot be None")
        return MyClass(kwargs.get('a', self.a), kwargs.get('b', self.b))

  obj = MyClass(1, 2)
  try:
    replaced_obj = copy.replace(obj, a=3)
    print(f"Original: {obj.a}, {obj.b}")
    print(f"Replaced: {replaced_obj.a}, {replaced_obj.b}")
  except ValueError as e:
      print(f"Error in test_copy_replace: {e}")

def test_dbm():
  try:
    db = dbm.sqlite3.open("mydatabase", 'c')
    db['key1'] = "value1"
    db['key2'] = b'\x00\x01\x02'  # Test with bytes
    db.close()
  except Exception as e:
    print(f"Error in test_dbm: {e}")
    try:
        os.remove("mydatabase")
    except:
        pass # Ignore errors if the file doesn't exist


def test_os_timer():
    try:
        start = time.perf_counter()
        result = os.times()
        end = time.perf_counter()
        print(f"OS Times: {result}, Time taken: {end-start}")
    except Exception as e:
      print(f"Error in test_os_timer: {e}")



def main():
  test_free_threading()
  test_copy_replace()
  test_dbm()
  test_os_timer()

if __name__ == "__main__":
  main()

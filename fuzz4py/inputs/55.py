
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket

def worker(arg: int):
    # Simulate a long-running task
    time.sleep(0.1)
    return arg * 2

def multithreaded_test(data: typing.List[int]):
    threads = []
    results = []

    for item in data:
        t = threading.Thread(target=worker, args=(item,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    for item in data:
      results.append(worker(item))

    return results

def test_free_threading(arg1: int, arg2: str) -> None:
    """
    This function demonstrates free-threading, possibly using a C extension.
    """
    
    shared_resource = 0  # Initialize shared resource

    def worker(arg):
        nonlocal shared_resource
        # Introduce potential race condition by not using a lock.
        shared_resource = arg * 2
        time.sleep(0.1 * arg1)

    t1 = threading.Thread(target=worker, args=(arg1,))
    t2 = threading.Thread(target=worker, args=(int(arg2),))

    threads = [t1, t2]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    try:
        if shared_resource != arg1 * 2:
            raise ValueError("Incorrect result for arg1")
        if shared_resource != int(arg2) * 2:
            raise ValueError("Incorrect result for arg2")
    except ValueError as e:
        print(f"Error in test_free_threading: {e}")
    return None


def complex_function(arg: typing.Union[int, typing.Callable[[int], int]]) -> int:
  if callable(arg):
    try:
      result = arg(10)
    except Exception as e:
        print(f"Error in lambda: {e}")
        return -1
  elif isinstance(arg, int):
    result = arg + 10
  else:
    raise TypeError("Invalid argument type")
  return result


def add_annotations(l: typing.List[int], fn: typing.Callable[[int], int]) -> typing.List[int]:
    return [fn(item) for item in l]



# Combined Fuzzing Tests

try:
  test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # Fuzzing with a malformed key
  malformed_dbm = dbm.open('malformed', 'c')
  malformed_dbm['key'] = b'\x00\xff'
  malformed_dbm.close()

  #Fuzzing different threading scenarios, with sleep
  multithreaded_test(test_data)
  test_free_threading(10, "20")
  test_free_threading(0, "abc")
  test_free_threading(-5, "10")
  test_free_threading(10, "-10")
  test_free_threading("abc", "def")

  #Testing copy.replace() (very basic)
  my_class = copy.copy(test_data)
  try:
    my_class = copy.replace(my_class, 2)
  except Exception as e:
    print(f"Exception raised in copy.replace(): {e}")

    
  # Fuzzing dbm.sqlite3
  db = dbm.open('test.db', 'c')
  db['key1'] = 'value1'
  db['key2'] = 'a' * 10000
  db['key3'] = b'\x00\x01\xff'
  db['key4'] = b'\x00' * 100000
  value = db['key1']
  db.close()
  
  # Fuzzing os.times()
  start_time = time.time()
  os.times()
  end_time = time.time()
  diff_time = end_time - start_time
  print(f"Time taken by os.times(): {diff_time:.6f}")

  # Fuzzing with SSL context
  context = ssl.create_default_context()
  try:
    with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
        s.connect(('example.com', 443))
  except Exception as e:
      print(f"Exception during SSL connection: {e}")
    

  annotations_result = add_annotations(test_data, lambda x: x*2)

  result = complex_function(lambda x: x * 2)
  result = complex_function(10)
  result = complex_function("not a callable")
  result = complex_function(lambda x: x / 0)


except (dbm.error, ssl.SSLError, OSError, ValueError, TypeError, Exception) as e:
  print(f"An error occurred: {type(e).__name__} - {e}")

print("Testing complete.")

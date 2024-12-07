
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket


def worker(arg: int):
    # Simulate a potentially JIT-compiled hot loop
    for i in range(1000000):
        if arg % 2 == 0:
            pass
        else:
            time.sleep(0.001)

    return arg


def jit_sensitive_function(data: list[int]) -> int:
    """
    A function designed to be JIT-compiled.
    """
    result = 0
    for i in range(len(data)):
        result += data[i] * i
    return result


def test_free_threading(data: list[int]) -> None:
    """Test free-threading with GIL."""
    threads = []
    for i in range(5):
        thread = threading.Thread(target=lambda x: jit_sensitive_function(x), args=(data,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def test_copy_replace(data: typing.List[int]) -> typing.List[int]:
  """Test the copy.replace protocol."""
  try:
    new_data = copy.copy(data)
    new_data.replace(3, 42)  #Trying to replace element.  (Unlikely to work but worth testing)
    return new_data
  except Exception as e:
    print(f"Error in replace: {e}")
    return data


def test_dbm_sqlite3() -> None:
  """Test dbm.sqlite3"""
  try:
    db = dbm.open('test.db', 'c')
    db['key'] = 'value'
    retrieved_value = db['key']
    db.close()
  except Exception as e:
    print(f"Error in dbm.sqlite3: {e}")


def test_os_timer():
  """Test os.times()."""
  try:
     t = os.times()
  except Exception as e:
    print(f"Error in test_os_timer: {e}")


def test_ssl_default_context() -> None:
  """Test ssl.create_default_context()."""
  try:
      context = ssl.create_default_context()
      print("Successfully created default context.")
  except Exception as e:
    print(f"Error in test_ssl_default_context: {e}")

def main():
    try:
        # Test free threading and GIL
        data = [1, 2, 3, 4, 5]
        test_free_threading(data)

        #Test os module timer functions.  Potentially race-condition prone.
        start = time.perf_counter()
        result = os.times()
        end = time.perf_counter()
        print("os.times() took:", end - start)

        #Test dbm.sqlite3
        test_dbm_sqlite3()

        #Test copy module with replace protocol
        data = [1, 2, 3, 4, 5]
        new_data = test_copy_replace(data)
        print("Copy replace result:", new_data)

        #Test SSL connections
        try:
            test_ssl_default_context()
            
        except Exception as e:
            print(f"SSL error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Cleanup
    try:
        os.remove('test.db')
    except OSError:
        pass


if __name__ == "__main__":
    main()

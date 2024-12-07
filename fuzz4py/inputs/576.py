
import threading
import copy
import os
import time
import ssl
import dbm
import typing
import random
import functools


def complex_function(arg1: typing.List[int], arg2: str) -> int:
    """
    This function demonstrates the use of complex types and annotations.  It does not handle exceptions well for testing purposes.
    """
    try:
        result = sum(arg1) * len(arg2)
        return result
    except (TypeError, ValueError):
        return -1  # Indicates an error


def test_free_threading(num_threads: int = 5):
    """
    Example of a free-threading function.
    """
    shared_list = []
    
    def worker(i):
        # Potential race condition.
        shared_list.append(i)
        time.sleep(0.1) # Introduces some timing variation


    threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return shared_list


def test_jit_and_locals():
    """
    Example of a function potentially JIT-compiled, with locals semantics.
    """
    a = 10
    b = [1,2,3,4]
    locals_dict = locals()
    return (a, locals_dict["b"])


def test_complex_annotations():
    """
    Fuzzing with complex type annotations.
    """
    complicated_annotation: typing.List[typing.Union[int, str]] = [1, 2, "3", 4]


#Fuzzing with new dbm backend
def test_dbm_sqlite3(db_name="test.db"):
  """
  Fuzzer for dbm.sqlite3
  """
  try:
    db = dbm.open(db_name, 'c')
    db['key1'] = 'value1'
    db['key2'] = 123
    
    # Attempt to write malformed data.
    db['key3'] = 'malformed\x00data'
    db.close()
    
    db = dbm.open(db_name, 'r')
    try:
        key_found = db.get('key1')
    finally:
      db.close()
  except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")
  finally:
    try:
        os.remove(db_name)
    except OSError:
        pass

def test_threading_jit(n: int) -> None:
    """Tests free-threading and JIT compiler with a hot loop."""
    data = [0] * n  # Initialize to 0
    lock = threading.Lock()
    
    def worker(i: int) -> None:
        with lock:
            for _ in range(1000):
                try:
                    data[i] += 1
                except TypeError:
                  print("Data corruption!")
                  return
                if random.random() < 0.1:
                    try:
                      lock = None
                    except Exception as e:
                      print(f"Error in lock mutation: {e}")
                      
    threads = []
    for i in range(n):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    
    # check for incorrect data due to potential race conditions
    for val in data:
      if not isinstance(val, int):
        print("Data corrupted!")
        break


def test_complex_annotations(data: typing.List[typing.Union[int, str]]) -> None:
    """Tests complex type annotations."""
    for i, item in enumerate(data):
        if isinstance(item, str):
          try:
              data[i] = item.upper()
          except AttributeError:
              print("Error: Invalid string operation!")
              data[i] = None
        elif isinstance(item, int):
          try:
              data[i] *= 2
          except TypeError:
              print("Error: Invalid arithmetic operation!")
              data[i] = None
        else:
          print("Unexpected type!")
    return data


def test_dbm_sqlite3_malformed():
  """Tests dbm.sqlite3 with malformed data."""
  try:
    db_name = "test.db"
    db = dbm.open(db_name, 'c')
    
    #Fuzzing malformed data: Varying key and value lengths
    key_length = random.randint(1, 10000)
    value_length = random.randint(1, 10000)
    
    key = b'\x00' * key_length
    value = b'\xff' * value_length
    
    db[key] = value
    db.close()
    
    db = dbm.open(db_name, 'r')
    try:
        db[key]
    except KeyError:
        print("Key not found.")
        return
    db.close()
  except Exception as e:
      print(f"Error accessing dbm: {e}")
  finally:
    try:
      os.remove(db_name)
    except OSError:
      pass

def test_os_timer():
  """Tests os.times() with different time values"""
  try:
      start_time = time.time()
      result = os.times()
      end_time = time.time()
      print(f"Time elapsed: {end_time - start_time}, Results: {result}")

  except Exception as e:
      print(f"Error in os.times(): {e}")


def test_ssl_connection(cert_path: str = "path/to/custom.pem") -> None:
  """Tests SSL connections with custom certificates."""
  try:
      context = ssl.create_default_context()
      
      # Fuzz with invalid certificate paths
      if random.random() < 0.5:
          cert_path = "/path/to/nonexistent/cert.pem"
      
      try:
        with open(cert_path, 'rb') as f:
          context.load_verify_locations(cafile=f.read())
          print("SSL connection attempt with custom certificate")
      except (FileNotFoundError, OSError) as e:
          print(f"Error: Certificate file not found or other error: {e}")
      except Exception as e:
          print(f"Error loading certificate: {e}")

  except Exception as e:
    print(f"General error: {e}")


def main():
    """
    Entry point to run the various fuzzing tests.
    """
    test_threading_jit(5)
    test_complex_annotations([1, "hello", 3, "world", "bad string", 2.7])  # Add a float
    test_dbm_sqlite3_malformed()
    test_os_timer()
    test_ssl_connection()
    test_free_threading()
    test_jit_and_locals()
    test_complex_annotations()
    test_dbm_sqlite3()


    print("Fuzzing tests complete.")


if __name__ == "__main__":
    main()

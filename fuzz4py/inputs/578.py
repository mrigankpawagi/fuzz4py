
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
        # Potential race condition.  Added more varied inputs.
        if random.random() < 0.5:
            shared_list.append(i)
        else:
            try:
                shared_list.append(i * random.uniform(0.1, 10)) # More varied inputs
            except TypeError:
                print("Worker failed due to TypeError")
                shared_list.append("Error")
            except Exception as e:
                print(f"Unexpected error: {e}")
                shared_list.append("Error") # catch and handle other exceptions
        time.sleep(random.uniform(0.05, 0.15))


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
    
    try:
        b_copy = locals_dict['b'][:]
        random.shuffle(b_copy)  # Mutate a copy, not original
        return (a, b_copy)
    except Exception as e:
      print(f"Error in locals test: {e}")
      return (a, b)


def test_complex_annotations():
    """
    Fuzzing with complex type annotations.
    """
    complicated_annotation: typing.List[typing.Union[int, str]] = [1, 2, "3", 4]
    
    try:
        index1 = random.randint(0, 3)
        index2 = random.randint(0, 3)
        complicated_annotation[index1] = complicated_annotation[index2] * 2
    except Exception as e:
        print(f"Annotation error: {e}")

    return complicated_annotation


#Fuzzing with new dbm backend
def test_dbm_sqlite3(db_name="test.db"):
  """
  Fuzzer for dbm.sqlite3
  """
  try:
    db = dbm.open(db_name, 'c')
    db['key1'] = 'value1'
    db['key2'] = 123
    
    # Attempt to write malformed data.  More complex cases
    db['key3'] = b'malformed\x00data'
    db['key4'] = b'\x00' * 1000
    db['key5'] =  123.45  #test a float
    db['key6'] = None
    db['key7'] = True
    db['key8'] =  [1,2,3]
    
    db.close()
    
    db = dbm.open(db_name, 'r')
    try:
        key_found = db.get('key1')
        key_found2 = db.get('key9', None)
    except (KeyError, TypeError) as e:
      print(f"Error accessing key: {e}")
    finally:
      db.close()
  except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")
  finally:
    try:
        os.remove(db_name)
    except OSError:
        pass


def test_os_timer():
  try:
      result = os.times()
      print(f"Time results (fuzzing): {result}")
  except Exception as e:
    print(f"Error in os.times(): {e}")


def test_ssl_connection():
  try:
      # Using a placeholder cert path, adjust to your environment
      context = ssl.create_default_context()
      context.check_hostname = False  # Disable hostname verification (for fuzzing)
      context.verify_mode = ssl.CERT_NONE  # Disable certificate verification
      # Placeholder for actual connection logic.
      print("SSL connection attempted (fuzzing)")
  except Exception as e:
    print(f"Error in SSL connection test: {e}")


def main():
    test_free_threading()
    test_jit_and_locals()
    test_complex_annotations()
    test_dbm_sqlite3()
    test_os_timer()
    test_ssl_connection()

if __name__ == "__main__":
    main()

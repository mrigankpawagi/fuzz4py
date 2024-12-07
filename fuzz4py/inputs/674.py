
import threading
import time
import copy
import os
import ssl
import sqlite3
import dbm
import socket
import typing
import random

# Fuzzing example targeting free-threading and dbm.sqlite3
def worker(id, db_conn, data):
    try:
        cursor = db_conn.cursor()
        # Inject potential error inducing data (more complex)
        injected_data = data * 1000 if isinstance(data, (str, bytes)) else str(data) #check types
        injected_data = random.choice([injected_data, None, b'\x00' * 1024, b'\x80' * 1024, b'\xff' * 1024, data,  # Bad bytes
                                       b'\x00' * random.randint(1, 1024),  #Variable length bad bytes
                                       str(random.random()),  #random floats
                                       int(random.random() * 1000),  #random integers
                                       bytearray(random.randint(1,100))])  #Random bytearray
        cursor.execute("INSERT INTO mytable VALUES (?, ?)", (id, injected_data))
        db_conn.commit()
    except Exception as e:
        print(f"Thread {id}: Error: {e}")
        raise


def fuzz_dbm_sqlite3():
    try:
        # Create a database connection (with different filenames)
        db_filename = 'mydatabase' + str(random.randint(1, 100)) + '.db'
        db_conn = sqlite3.connect(db_filename)

        # Create a table (with error-prone query)
        cursor = db_conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS mytable (id INTEGER, data TEXT)"
        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error in query: {e}")
            return  # Important: Exit if table creation fails
        db_conn.commit()


        # Fuzz with different data types and sizes, including larger data
        data_list = [b"hello", 123, None, b"\x00\x01\x02", "", "a" * 1024, 123.456, b"\x00"*2048, bytearray(random.randint(1,100)),
                     (1, 2, 3), {1: 2}, [1, 2, 3], 
                     {"key": b"value"},
                     b"a" * 4096,  #Longer strings
                     12345678901234567890, #Large integers
                     {i: i * 2 for i in range(100)},
                     {i: str(i) for i in range(10)},  # Dict with strings as values
                     [1, 2, [1,2,3,4], {"inner": 5}],  # Nested data structures
                     {"key": None},
                     {}, [], (), b"", 
                     b'this is a very long string' * 100]
        

        threads = []
        for i in range(5):
            t = threading.Thread(target=worker, args=(i, db_conn, random.choice(data_list))) #Random selection
            threads.append(t)
            t.start()
        
        for t in threads:
          t.join()

        db_conn.close()
        print("Database operations completed.")

    except Exception as e:
        print(f"Error during fuzzing: {e}")



def fuzz_os_timer():
    try:
        time_value = random.uniform(-10, 10)  # Random time values
        flags = random.choice([os.O_RDONLY, os.O_WRONLY, os.O_RDWR, 0, -1, 0o777])  # Fuzz more flags
        try:
            os.times()  #Call os.times to ensure it does not cause an error
            # os.utime(random.choice([None, "/tmp/a_file"]), (time_value, time_value)) #Use more possible error-prone calls
        except Exception as e:
            print(f"Error during os.times(): {e}")
    except Exception as e:
        print(f"Error during fuzzing: {e}")


def fuzz_ssl_connections():
  try:
    context = ssl.create_default_context()  
    certificate_paths = [None, "bad_certificate.crt", "does_not_exist.crt",
                         os.path.join(os.getcwd(), "a", "b", "c", "certificate.crt"), "/dev/null", 
                         os.path.join(os.path.dirname(__file__), "fake_cert.crt")] #More paths
    certificate_path = random.choice(certificate_paths)
    
    try:
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="example.com") as s:
            s.connect(("localhost", 443))
            print("SSL connection established.")
    except Exception as e:
        print(f"Error during SSL connection attempt: {e}")
  except Exception as e:
      print(f"Error during SSL Fuzzing: {e}")


def complex_function(data: typing.List[int], replace_flag: bool = False) -> typing.Optional[int]:
  if not data:
      return None
  num_threads = random.randint(1, 100)
  try:
      result = sum(data)  # Replace with more complex logic.
      return result
  except Exception as e:
      print(f"Error in complex_function: {e}")
      return None



def race_condition_example(data: typing.List[int]) -> typing.List[int]:
    lock = threading.Lock()
    results = []

    def worker(item):
        with lock:
            results.append(item * 2)

    threads = []
    for item in data:
        thread = threading.Thread(target=worker, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def jit_test():
  count = 0
  for i in range(10000000):
    count += i
  return count


def test_replace_protocol(obj):
    try:
        return copy.replace(obj, new_attr=42)
    except AttributeError:
        return obj


def test_dbm():
    db_name = 'test.db'
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute("INSERT INTO test_table VALUES(?)", (b'invalid data',))
        conn.commit()
    except Exception as e:
        print(f"Error in dbm test: {e}")
    finally:
        try:
            conn.close()
        except:
            pass


def main():
    fuzz_dbm_sqlite3()
    fuzz_os_timer()
    fuzz_ssl_connections()
    test_data = [1, 2, 3, 4, 5]
    print(f"Race Condition Output: {race_condition_example(test_data)}")
    jit_result = jit_test()
    print(f"JIT Result: {jit_result}")
    class TestClass:
        def __init__(self, attr):
            self.attr = attr
        def __replace__(self, attr=None):
            return type(self)(attr or self.attr)
    try:
        test_class_replace = TestClass(10)
        replaced_obj = test_replace_protocol(test_class_replace)
        print(f"Replaced Object: {replaced_obj}")
    except Exception as e:
        print(f"Error in replacing object: {e}")
    try:
        test_dbm()
    except Exception as e:
        print(f"Error in DBM test: {e}")

if __name__ == "__main__":
    main()


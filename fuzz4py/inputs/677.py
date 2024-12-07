
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


# ... (rest of the functions from the second code block) ...


def multithreaded_fuzz(data_list):
    threads = []
    for data in data_list:
        thread = threading.Thread(target=worker, args=(data,)) #using worker from first code block.
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()  # Crucial for correctness and avoiding data races.



# Fuzzing complex type annotations
def annotated_function(data: typing.Union[str, int, list[int]]) -> typing.Union[str, int]:
    # ... (rest of the function) ...


# Fuzzing os.times() with different values
def test_os_times():
    try:
        t = os.times()
        print(f"CPU times: {t}")
    except (OSError, ValueError) as e:
        print(f"Error getting CPU times: {e}")


# Fuzzing SSL connections (simplified for demonstration)
def ssl_fuzz():
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


# Example usage (Fuzzing)
data_list = ["hello", "world", "python", 123, [1, 2, 3]]  # Diverse inputs


# Testing Free-threading with different input types
multithreaded_fuzz(data_list)



# ... (rest of the functions from the second code block) ...

if __name__ == "__main__":
    # ... (rest of the main function, including calls to the fuzzing functions) ...

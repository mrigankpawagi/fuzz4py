
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
        injected_data = data * 1000 if isinstance(data, (str, bytes)) else str(data)
        injected_data = random.choice([injected_data, None, b'\x00' * 1024, b'\x80' * 1024, b'\xff' * 1024, data,
                                       b'\x00' * random.randint(1, 1024),
                                       str(random.random()),
                                       int(random.random() * 1000),
                                       bytearray(random.randint(1, 100))])  #Simplified choice
        cursor.execute("INSERT INTO mytable VALUES (?, ?)", (id, injected_data))
        db_conn.commit()
    except Exception as e:
        print(f"Thread {id}: Error: {e}")


def fuzz_dbm_sqlite3():
    try:
        # Create a database connection (with different filenames)
        db_filename = 'mydatabase' + str(random.randint(1, 100)) + '.db'
        db_conn = sqlite3.connect(db_filename)

        # Create a table (with error-prone query)
        cursor = db_conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS mytable (id INTEGER, data TEXT)"
        cursor.execute(query)  # Removed try-except for table creation
        db_conn.commit()


        # Fuzz with different data types and sizes
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
            t = threading.Thread(target=worker, args=(i, db_conn, random.choice(data_list)))
            threads.append(t)
            t.start()
        
        for t in threads:
          t.join()

        db_conn.close()
        print("Database operations completed.")

    except Exception as e:
        print(f"Error during fuzzing: {e}")


def multithreaded_fuzz(data_list):
    threads = []
    for i, data in enumerate(data_list):
        thread = threading.Thread(target=worker, args=(i, sqlite3.connect("fuzz_db.db"), data)) # Corrected connection
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def annotated_function(data: typing.Union[str, int, list[int]]) -> typing.Union[str, int]:
    return str(data) if isinstance(data, str) else data


# Fuzzing os.times() with different values (Example, minimal changes)
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
    # ... (rest of the function)  # Placeholder for SSL connection fuzzing
    certificate_paths = [None, "bad_certificate.crt", "does_not_exist.crt"]
    certificate_path = random.choice(certificate_paths)
    try:
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="example.com") as s:
            s.connect(("localhost", 443))  # Attempt to connect to a server
            print("SSL connection established.")
    except Exception as e:
        print(f"Error during SSL connection attempt: {e}")
  except Exception as e:
      print(f"Error during SSL Fuzzing: {e}")



if __name__ == "__main__":
    data_list = ["hello", "world", "python", 123, [1, 2, 3]]
    multithreaded_fuzz(data_list)
    fuzz_dbm_sqlite3()
    test_os_times()
    ssl_fuzz()

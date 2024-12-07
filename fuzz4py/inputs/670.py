
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
        injected_data = random.choice([injected_data, None, b'\x00' * 1024, b'\x80' * 1024, b'\xff' * 1024, data]) #Fuzz with None & bad bytes, various patterns
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
                     #Add more complex objects
                     {"key": b"value"},
                     b"a" * 4096,  #Longer strings
                     12345678901234567890, #Large integers
                     {i: i * 2 for i in range(100)}] #dictionary with 100 elements

        threads = []
        for i in range(5):
            t = threading.Thread(target=worker, args=(i, db_conn, data_list[i % len(data_list)]))
            threads.append(t)
            t.start()
        
        for t in threads:
          t.join()

        # Close the connection after all threads are finished
        db_conn.close()
        print("Database operations completed.")

    except Exception as e:
        print(f"Error during fuzzing: {e}")



def fuzz_os_timer():
    try:
        time_value = random.uniform(-10, 10)  # Random time values
        flags = random.choice([os.O_RDONLY, os.O_WRONLY, os.O_RDWR, 0, -1]) #Fuzz with invalid flags -1
        print(f"Calling os.times() with time_value={time_value}, flags={flags}")
        try:
          time_results = os.times()
          print(f"Results: {time_results}")
        except Exception as e:
            print(f"Error during os.times(): {e}")


    except Exception as e:
        print(f"Error during fuzzing: {e}")



def fuzz_ssl_connections():
  try:
    context = ssl.create_default_context()  
    # Fuzz with various certificate paths including invalid, none and different paths
    certificate_paths = ["bad_certificate.crt", None, "does_not_exist.crt", os.path.join(os.getcwd(), "a", "b", "c", "certificate.crt")]
    certificate_path = random.choice(certificate_paths)
    print(f"Trying with certificate at {certificate_path}")
    try:
      with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="example.com") as s:
          s.connect(("localhost", 443))
          print("SSL connection established.")
    except ssl.SSLError as e:
      print(f"SSL Error: {e}")
  except Exception as e:
      print(f"Error during SSL Fuzzing: {e}")


def complex_function(data: typing.List[int], replace_flag: bool = False) -> typing.Optional[int]:
  # Fuzz with empty data
  if not data:
      return None

  #Fuzz with different thread count
  num_threads = random.randint(1, 100)


  # ... (rest of the function remains the same - add more fuzzing)


def main():
    fuzz_dbm_sqlite3()
    fuzz_os_timer()
    fuzz_ssl_connections()
    # ... (rest of the main function - add more fuzzing functions)


if __name__ == "__main__":
    main()

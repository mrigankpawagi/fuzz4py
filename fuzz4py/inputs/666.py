
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing
import socket

# Fuzzing example targeting free-threading and dbm.sqlite3
def worker(id, db_conn, data):
    try:
        cursor = db_conn.cursor()
        # Inject potential error inducing data
        injected_data = data * 1000 if data else ""
        cursor.execute("INSERT INTO mytable VALUES (?, ?)", (id, injected_data))
        db_conn.commit()
    except Exception as e:
        print(f"Thread {id}: Error: {e}")
        raise


def fuzz_dbm_sqlite3():
    try:
        # Create a database connection
        db_conn = sqlite3.connect('mydatabase.db')

        # Create a table
        cursor = db_conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER, data TEXT)")
        db_conn.commit()


        # Fuzz with different data types and sizes
        data_list = [b"hello", 123, None, b"\x00\x01\x02", "", "a" * 1024]  

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
      time_value = -1.2345  # Negative time value
      flags = os.O_RDONLY | os.O_WRONLY # Example flags with different combinations
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
    # Replace with your certificate if you have one
    #  or a potentially problematic certificate
    certificate_path = "bad_certificate.crt" # Or a bad certificate
    print(f"Trying with certificate at {certificate_path}")
    
    try:
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="example.com") as s:
            s.connect(("localhost", 443)) #443 for standard port
            print("SSL connection established.")
    except ssl.SSLError as e:
      print(f"SSL Error: {e}")
  except Exception as e:
      print(f"Error during SSL Fuzzing: {e}")


if __name__ == "__main__":
    fuzz_dbm_sqlite3()
    fuzz_os_timer()
    fuzz_ssl_connections()

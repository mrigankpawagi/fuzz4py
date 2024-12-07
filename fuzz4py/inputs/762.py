
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing
import socket

def worker(arg: int, context: ssl.SSLContext) -> None:
    # Simulate some work that might be JIT-compiled
    for _ in range(10000):
        try:
            time.sleep(0.0001 * (arg % 10))  # Vary sleep time based on arg
        except Exception as e:
            print(f"Thread {threading.current_thread().name} time.sleep error: {e}")
        
    # Use replace protocol - introduce potential errors
    try:
        if arg > 0:
          arg = copy.copy(arg)  #Avoid potential mutation issues
          arg = arg * 2
        else:
          arg = 0
    except Exception as e:
        print(f"Thread {threading.current_thread().name} copy operation error: {e}")
    
    print(f"Thread {threading.current_thread().name} processed {arg}")

    # Interact with ssl context
    try:
        with context.wrap_socket(
            socket.socket(), server_hostname="localhost"
        ) as s:
            s.connect(("127.0.0.1", 4433 + arg))  # Vary port based on arg
    except Exception as e:
        print(f"Thread {threading.current_thread().name} SSL error: {e}")

def main():
    # Create an SSL context.  Fuzzing should include various certificate types
    try:
        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        context.load_verify_locations(cafile="invalid_ca.crt")  # Invalid Certificate
    except Exception as e:
        print(f"SSL context creation error: {e}")

    # Example use of new timer functions (assuming you have a suitable timer)
    start_time = time.perf_counter()  # Use perf_counter for better accuracy

    threads = []
    for i in range(5):
        x = threading.Thread(target=worker, args=(i, context))
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print("Elapsed time:", end_time - start_time)

    # Example using dbm.sqlite3 (with error handling)
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")
        cursor.execute("INSERT INTO data (value) VALUES (?)", ('fuzzed_data' * 100,))  # Large data
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:  # General exception handler
      print(f"Unexpected error: {e}")

    try:  # Added try/except to catch any exceptions
        with open("test_file.txt", "w") as f:
            f.write("some data")
    except Exception as e:
        print(f"File error: {e}")


if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import sqlite3
import socket

# Fuzzing focus on free-threading and JIT compiler (PEP 703, 744)
def worker(i):
    try:
        # Simulate some work
        time.sleep(0.1)
        # Potential race condition if accessed by multiple threads
        global shared_data
        shared_data[i] += 1
    except Exception as e:
        print(f"Error in worker {i}: {e}")


def multithreaded_test():
    global shared_data
    shared_data = [0] * 10
    threads = []

    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Shared data:", shared_data)


# Fuzzing focus on docstring whitespace stripping
def my_function():
    """This is a docstring with varying
    whitespace"""
    pass


# Fuzzing focus on annotation scopes
def complex_annotation(data: list[str] | dict[str, int]) -> int:
    return len(data)


# Fuzzing focus on dbm.sqlite3
def dbm_fuzzer():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    try:
        #  Fuzz with malformed data
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER, name TEXT)")
        cursor.execute("INSERT INTO test VALUES (1, 'fuzzed_data')")

        # Attempting to insert malformed data (example of a potential fuzz case)
        cursor.execute("INSERT INTO test VALUES (2, 'this is a malformed string')")
        
        conn.commit()
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()
        print("Database results:", results)

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()

#Fuzzing focus on copy.replace()
class Replaceable:
    def __init__(self, value):
        self.value = value
    def __replace__(self,value=None):
        if value:
            self.value = value
        return self

def replace_fuzz():
  obj = Replaceable(10)
  replaced_obj = copy.replace(obj, value=20)
  print(f"Original: {obj.value}, Replaced: {replaced_obj.value}")


# Fuzzing focus on ssl.create_default_context()
def ssl_fuzz():
    context = ssl.create_default_context()
    try:
        # Replace with a proper invalid certificate for better fuzzing
        # (e.g., a self-signed certificate)
        #  This is a placeholder for a more robust test that checks a potentially invalid certificate
        with context.wrap_socket(socket.socket(), server_hostname="127.0.0.1") as s:
          s.connect(('127.0.0.1', 8443)) # Replace with a test server if available.
          s.sendall(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
          response = s.recv(1024)
          print("SSL Response:", response)
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
        

if __name__ == "__main__":
  try:
      multithreaded_test()
      dbm_fuzzer()
      replace_fuzz()
      ssl_fuzz() # Added ssl_fuzz
  except Exception as e:
      print(f"Error: {e}")


import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket
import random

def jit_sensitive_function(input_list):
    """
    A function likely to be JIT-compiled.
    """
    total = 0
    for i in range(len(input_list)):
        try:
            total += input_list[i]
        except IndexError:
          return "IndexError in jit_sensitive_function"
    return total


def test_free_threading(data: list) -> None:
    """
    Test free-threading functionality.
    """
    results = []
    def worker(data_part):
        try:
          result = jit_sensitive_function(data_part)
          if result == "IndexError in jit_sensitive_function":
            raise IndexError("Error in worker thread")
          results.append(result)
        except Exception as e:
            results.append(f"Worker thread error: {e}")

    threads = []
    for i in range(4):
        thread = threading.Thread(target=worker, args=(data[i*len(data)//4 : (i+1)*len(data)//4],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    return results


def test_dbm_sqlite3(key, value):
    """
    Test dbm.sqlite3 module.
    """
    try:
        db = dbm.open("test.db", "c")
        db[key] = value
        retrieved_value = db.get(key)  # Use get to handle potential errors gracefully
        db.close()
        if retrieved_value is None:
          return "Key not found"
        return retrieved_value
    except Exception as e:
        return f"Error: {e}"


def test_ssl_context(certificate_path):
    """Test SSL connections with potentially invalid certificates."""
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(
                socket.socket(socket.AF_INET), server_hostname="example.com"
        ) as ssock:
          ssock.settimeout(5.0)  # Add timeout to prevent indefinite hangs
          ssock.connect(("localhost", 4433))
          return "SSL connection established"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
  data = list(range(1000))
  try:
      results = test_free_threading(data)
      print("Free threading results:", results)
  except Exception as e:
      print(f"Free threading error: {e}")
  

  key = "testkey"
  value = "testvalue"
  result = test_dbm_sqlite3(key, value)
  print(result)

  #  Crucially, create a dummy invalid certificate file
  try:
    with open("invalid.pem", "w") as f:
        f.write("This is not a valid certificate")
  except Exception as e:
      print(f"Error creating invalid certificate: {e}")

  certificate_path = "invalid.pem"
  ssl_result = test_ssl_context(certificate_path)
  print(ssl_result)


import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(data: typing.List[int]) -> None:
    """
    Demonstrates multi-threading issues and docstring whitespace.

    Args:
        data: A list of integers to process.
    """
    time.sleep(0.1) # Introduce delay for potential race conditions
    try:
        db = dbm.sqlite3.open("test.db", "c")  # Use dbm.sqlite3
        for i in data:
          db[str(i)] = str(i * 2)
        db.close()
    except Exception as e:
      print(f"Error in worker: {e}")

def main():
    """Main function for testing."""
    data = [i for i in range(10)]
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=([x for x in data if x %2 == i],)) # pass a copy of the list to prevent race conditions
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
    print("All threads finished.")

    try:
      db = dbm.sqlite3.open("test.db", "r")
      for key in db:
          print(f"Key: {key}, Value: {db[key]}")
      db.close()
    except Exception as e:
      print(f"Error opening or reading database: {e}")

    os.remove("test.db") # Clean up

if __name__ == "__main__":
  main()



import threading
import time
import copy
import dbm.sqlite3
import os
import ssl
import typing
import random
import sys

def worker(data: typing.List[int]) -> None:
    """
    Demonstrates multi-threading issues and docstring whitespace.

    Args:
        data: A list of integers to process.
    """
    time.sleep(random.uniform(0.05, 0.15))  # Vary delay for fuzzing
    try:
        db_mode = random.choice(["c", "w"])  # Fuzz db open mode
        db = dbm.sqlite3.open("test.db", db_mode)
        for i in data:
            db[str(i)] = str(i * random.randint(1, 10))  # Fuzz value for db
        db.close()
    except Exception as e:
        print(f"Error in worker ({threading.current_thread().name}): {e}", file=sys.stderr)


def main():
    """Main function for testing."""
    data = list(range(10))
    threads = []
    for i in range(random.randint(3, 7)):  # Vary the number of threads for fuzzing
        sub_list = [x for x in data if x % (i + 1) == 0]  # Fuzz mod operator for list slicing
        if not sub_list:
          continue  # Prevent empty lists
        # Create a copy, but with potential for error (fuzzing).
        try:
          t = threading.Thread(target=worker, args=(sub_list.copy(),))
        except Exception as e:
          print(f"Error creating thread: {e}", file=sys.stderr)
          continue
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
    print("All threads finished.")

    try:
        db = dbm.sqlite3.open("test.db", "r")
        for key in db:
            try:
                value = db[key]
                if not isinstance(value, str):  # Check data type
                   print("Unexpected value type!", file=sys.stderr)
                   continue

                print(f"Key: {key}, Value: {value}")
            except Exception as e:
                print(f"Error reading key {key}: {e}", file=sys.stderr)
        db.close()
    except Exception as e:
        print(f"Error opening or reading database: {e}", file=sys.stderr)
    
    #Fuzz the file removal.  Adding exception handling to prevent program termination
    try:
        os.remove("test.db")  # Clean up
    except OSError as e:
        print(f"Error removing database: {e}", file=sys.stderr)

    except Exception as e:
      print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
  main()

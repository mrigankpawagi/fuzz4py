
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
    sleep_time = random.uniform(0.05, 0.15)
    time.sleep(sleep_time)  # Vary delay for fuzzing
    try:
        db_mode = random.choice(["c", "w", "n", "a", "r"]) # Added 'r'
        # Fuzz db_mode with invalid values
        if random.random() < 0.1:
          db_mode = "xyz"  
        db = dbm.sqlite3.open("test.db", db_mode)
        for i in data:
            try:
              value = i * random.randint(-100, 100) # Wider range for fuzzing, including 0
              # Fuzzing with None
              if random.random() < 0.1:
                value = None
              if value is None:
                continue
              # Fuzzing with different data types
              if random.random() < 0.1:
                db[str(i)] = b"some bytes" # Attempting to write bytes
              elif random.random() < 0.1:
                db[str(i)] = True
              elif random.random() < 0.1:
                  db[str(i)] = 3.14159
              else:
                db[str(i)] = str(value)  # Fuzz value for db
            except Exception as e:
                print(f"Error writing to database: {e}", file=sys.stderr)

        db.close()
    except Exception as e:
        print(f"Error in worker ({threading.current_thread().name}): {e}", file=sys.stderr)


def main():
    """Main function for testing."""
    data = list(range(10))
    threads = []
    num_threads = random.randint(3, 7)

    for i in range(num_threads):
        sub_list = [x for x in data if x % (i + 1) == 0]
        if not sub_list:
            continue

        # Robust thread creation - critical for fuzzing
        t = threading.Thread(target=worker, args=(sub_list.copy(),))
        threads.append(t)
        try:
          t.start()
        except Exception as e:
            print(f"Error creating thread {i}: {e}", file=sys.stderr)

    for t in threads:
        t.join()

    print("All threads finished.")

    #Robust database handling
    try:
      db = dbm.sqlite3.open("test.db", "r")
    except dbm.error as e:
      print(f"Error opening database: {e}", file=sys.stderr)
      # Crucial: avoid trying to read if the database is unavailable
      sys.exit(1)  
    for key in db:
        try:
            value = db[key]
            if not isinstance(value, (str, bytes)):
                print("Unexpected value type!", file=sys.stderr)
                continue  # Crucial! Prevents crashes.
            print(f"Key: {key}, Value: {value}")
        except Exception as e:
            print(f"Error reading key {key}: {e}", file=sys.stderr)
    db.close()


    try:
        if os.path.exists("test.db"):
            os.remove("test.db")
    except (OSError, Exception) as e:
        print(f"Error removing database: {e}", file=sys.stderr)


if __name__ == "__main__":
  main()

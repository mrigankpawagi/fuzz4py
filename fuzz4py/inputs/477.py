
import threading
import time
import copy
import dbm.sqlite3
import os
import ssl
import typing

def worker(data: typing.List[int]) -> None:
    """
    Demonstrates multi-threading issues and docstring whitespace.

    Args:
        data: A list of integers to process.
    """
    time.sleep(0.1)  # Introduce delay for potential race conditions
    try:
        # Use dbm.sqlite3
        db = dbm.sqlite3.open("test.db", "c")
        for i in data:
            db[str(i)] = str(i * 2)
        db.close()
    except Exception as e:
        print(f"Error in worker: {e}")


def main():
    """Main function for testing."""
    data = list(range(10))
    threads = []
    for i in range(5):
        # Crucial copy of the slice to avoid race conditions.
        sub_list = [x for x in data if x % 2 == i]
        # Create a copy to avoid race conditions.
        t = threading.Thread(target=worker, args=(sub_list.copy(),))  
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
    print("All threads finished.")

    try:
        db = dbm.sqlite3.open("test.db", "r")
        for key in db:
            try:
                print(f"Key: {key}, Value: {db[key]}")
            except Exception as e:
                print(f"Error reading key {key}: {e}")
        db.close()
    except Exception as e:
        print(f"Error opening or reading database: {e}")

    try:
        os.remove("test.db")  # Clean up
    except OSError as e:
        print(f"Error removing database: {e}")


if __name__ == "__main__":
  main()


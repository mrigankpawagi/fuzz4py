
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

def my_function(arg1: int, arg2: str, arg3: typing.List[int]) -> int:
    """
    This function does something complex.

    Args:
        arg1: An integer.
        arg2: A string.
        arg3: A list of integers.

    Returns:
        An integer.
    """

    try:
      result = arg1 + sum(arg3)
      if arg2 == "error":
        raise ValueError("Error condition triggered.")
      return result
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        return -1  # Or some other error handling


def worker_thread(data: typing.Tuple[int, str, list[int]]):
    try:
      arg1, arg2, arg3 = data
      result = my_function(arg1, arg2, arg3)
      print(f"Thread {threading.current_thread().name}: Result: {result}")
    except Exception as e:
        print(f"Thread {threading.current_thread().name}: Error: {e}")
    time.sleep(0.1) # Simulate work


if __name__ == "__main__":
    # Fuzzing with various inputs and thread usage
    data_list = [
        (10, "hello", [1, 2, 3]),
        (20, "error", [4, 5, 6]),
        (-1, "test", [7, 8, 9]),
        (100, "a" * 1000, [100]),
        (0, "", []),
        (20, "another test", [5000000000, 5000000000, 5000000000])

    ]


    threads = []
    for data in data_list:
      thread = threading.Thread(target=worker_thread, args=(data,))
      threads.append(thread)
      thread.start()
    
    for thread in threads:
      thread.join()

    # Example interaction with the dbm module (sqlite3)
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")
        cursor.execute("INSERT INTO data (value) VALUES (?)", ('fuzzing data',))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")


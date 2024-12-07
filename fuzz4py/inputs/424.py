
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

def race_condition_example(data: int, lock: threading.Lock) -> None:
    """
    This function demonstrates a potential race condition.
    """
    lock.acquire()
    try:
        global_data = data * 2
        time.sleep(0.1)  # Introduce a delay for potential race
        print(f"Thread {threading.get_ident()} calculated: {global_data}")
    finally:
        lock.release()

def main():
    global_data = 10
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=race_condition_example, args=(global_data, lock))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    # Demonstrate copy.replace()
    try:
      class MyData:
          def __init__(self, value:int):
              self.value = value
          def __replace__(self, **kwargs):
              new_value = kwargs.get('value')
              if new_value is not None:
                  return type(self)(new_value)
              return self


      data = MyData(10)
      replaced_data = copy.replace(data, value=20)
      assert replaced_data.value == 20
      print("copy.replace() successful")


    except Exception as e:
        print(f"copy.replace() error: {e}")

    #  Simple database interaction (using dbm.sqlite3)
    try:
        db = sqlite3.connect(":memory:")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, value TEXT)")
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", ("Initial Data",))

        result = cursor.execute("SELECT value FROM mytable").fetchone()
        if result:
            print(f"Database data: {result[0]}")
        db.close()

    except Exception as e:
        print(f"Database interaction error: {e}")


    try:
      start_time = time.time()
      time_taken = os.times()[0]
      print(f"Time taken: {time_taken}")
      end_time = time.time()
      print(f"Time taken (alternative method): {end_time - start_time}")
    except Exception as e:
        print(f"Time measurement error: {e}")

if __name__ == "__main__":
    main()

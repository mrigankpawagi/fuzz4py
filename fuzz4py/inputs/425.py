
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
        # Introduce a potentially problematic delay.
        time.sleep(0.1 + data * 0.01)  #Varying delay
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


    try:
        class MyData:
            def __init__(self, value: int = 0):
                self.value = value

            def __replace__(self, **kwargs):
                if "value" in kwargs and kwargs["value"] is not None:
                    try:
                        new_value = int(kwargs["value"]) #adding potential error injection
                        return type(self)(new_value)
                    except ValueError as e:
                        print(f"Error in __replace__: {e}")
                        return self  # Return original if value cannot be converted

        data = MyData(10)
        replaced_data = copy.replace(data, value="20") #invalid input
        assert replaced_data.value == 20
        print("copy.replace() successful")


    except Exception as e:
        print(f"copy.replace() error: {e}")



    #  Simple database interaction (using dbm.sqlite3)
    try:
        db = sqlite3.connect(":memory:")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, value TEXT)")
        # Malformed data insertion
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", (None,))  # Try inserting None

        result = cursor.execute("SELECT value FROM mytable").fetchone()
        if result:
            print(f"Database data: {result[0]}")
        db.close()

    except Exception as e:
        print(f"Database interaction error: {e}")




    try:
        # Fuzzing the os module timer function
        time_taken = os.times()[0]  # Introduce potential error in this line
        print(f"Time taken: {time_taken}")

        start_time = time.time()
        time.sleep(5) #sleep for a few seconds to introduce potential delays
        end_time = time.time()
        print(f"Time taken (alternative method): {end_time - start_time}")
    except Exception as e:
        print(f"Time measurement error: {e}")

if __name__ == "__main__":
    main()


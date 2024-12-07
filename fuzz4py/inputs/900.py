
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def my_function(data: typing.List[int], sleep_time: float) -> None:
    """
    This function demonstrates threading and database operations.
    """

    # Accessing the GIL (in this case, a simulated GIL)
    # Simulate a database operation
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        for i in data:
            db[str(i)] = str(i * 2)
        db.close()

    except Exception as e:
        print(f"Database error: {e}")


    # Simulate a function that takes a variable amount of time
    time.sleep(sleep_time)

    # Testing local variables
    local_var = 10
    local_var2 = [1, 2, 3]
    print("Local var in thread:", local_var, local_var2)

def main():
    data = list(range(1000))

    # Create threads
    threads = []
    for i in range(5):
        sleep_time = float(i) / 2  # Vary sleep time
        t = threading.Thread(target=my_function, args=(copy.deepcopy(data), sleep_time))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    main()

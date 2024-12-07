
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def worker(data: typing.List[int], id: int) -> None:
    try:
        for i in range(len(data)):
            # Simulate work
            result = data[i] * id
            time.sleep(0.1)
            if result > 1000:
                raise ValueError("Result too large")
    except ValueError as e:
        print(f"Thread {id}: Error: {e}")
        # Attempting to raise exceptions that would terminate threads
        raise
    except Exception as e:
        print(f"Thread {id}: Unhandled exception: {e}")
    finally:
        pass

def main():
    data = list(range(100))
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), i))  # Deepcopy to avoid shared memory issues.
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Simulate database interaction, using the new dbm.sqlite3 backend
    try:
      db = dbm.open('mydatabase', 'c') # 'c' for create
      db['key'] = 'value'
      value = db['key']
      db.close()

    except Exception as e:
        print(f"Error during database operation: {e}")


    # Testing os module timer functions
    try:
        start_time = time.perf_counter()
        result = os.times()  # Use the timer function from os
        end_time = time.perf_counter()
        print("OS Timer results (real, user, sys, cuser, csys):", result)
        print("Time taken:", end_time - start_time)
    except Exception as e:
        print(f"Error during timer function: {e}")


    # Testing ssl
    try:
        context = ssl.create_default_context()
        # Add further SSL testing here, but this example is illustrative
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

    try:
        # Testing replace protocol
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __replace__(self, **changes):
                return type(self)(**changes)


        point = Point(x=1, y=2)
        new_point = point.__replace__(x=3) # Use the new replace protocol for object manipulation
        print(new_point.x, new_point.y)

    except Exception as e:
        print("Error during replace protocol test:", e)


if __name__ == "__main__":
    main()

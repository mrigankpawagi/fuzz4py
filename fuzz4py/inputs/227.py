
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
            result = data[i] * id
            time.sleep(0.1)
            if result > 1000:
                raise ValueError("Result too large")
    except ValueError as e:
        print(f"Thread {id}: Error: {e}")
        raise
    except Exception as e:
        print(f"Thread {id}: Unhandled exception: {e}")

def main():
    data = list(range(100))
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        value = db['key']
        db.close()
    except Exception as e:
        print(f"Error during database operation: {e}")


    try:
        start_time = time.perf_counter()
        result = os.times()
        end_time = time.perf_counter()
        print("OS Timer results (real, user, sys, cuser, csys):", result)
        print("Time taken:", end_time - start_time)
    except Exception as e:
        print(f"Error during timer function: {e}")


    try:
        context = ssl.create_default_context()
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


    try:
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __replace__(self, **changes):
                return type(self)(**changes)

        point = Point(x=1, y=2)
        new_point = point.__replace__(x=3)
        print(new_point.x, new_point.y)

    except Exception as e:
        print("Error during replace protocol test:", e)


if __name__ == "__main__":
    main()


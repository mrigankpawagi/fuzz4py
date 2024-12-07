
import threading
import time
import copy
import os
import ssl
import dbm.sqlite3
import typing

def worker(data: typing.List[int], lock):
    for i in data:
        # Simulate some work that can be JIT-compiled.
        time.sleep(0.001)
        lock.acquire()
        try:
            # Potential race condition.
            # Notice this thread is not using the GIL.
            # This code now can be executed by multi-threading.
            # Note: This is a simplified example, real-world cases
            # are usually much more complicated and require careful design.
            temp = i * 2
        finally:
            lock.release()


def main():
    data = list(range(1000))
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")

    # Example using dbm.sqlite3
    try:
        db = dbm.sqlite3.open("mydatabase.db", 'c')  # 'c' mode creates the DB
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Database error: {e}")



if __name__ == "__main__":
    main()




import threading
import copy
import os
import ssl
import time
import dbm.sqlite3
import typing


def worker(data, lock, db):
    # Simulate work with potential race condition
    lock.acquire()
    try:
        db[str(data)] = data * 2
    finally:
        lock.release()
    time.sleep(0.01)  # Simulate some work


def main():
    db = dbm.sqlite3.open("mydatabase", 'c')
    lock = threading.Lock()
    threads = []
    data_list = [i for i in range(100)]

    try:
        for data in data_list:
            thread = threading.Thread(target=worker, args=(data, lock, db))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        result = {}
        for key in db:
            result[int(key)] = int(db[key])

        # Example of a potential error
        try:
            bad_data =  'string' * 2500
            db[bad_data] = 'test'
        except Exception as e:
          print(f"Exception caught in db write: {e}")
    except Exception as e:
      print(f"Exception in main loop: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()

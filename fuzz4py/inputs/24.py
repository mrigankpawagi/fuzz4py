
import threading
import time
import copy
import os
import ssl
import typing
import dbm

def worker(id: int, data: str, lock):
    # Simulate work that takes some time.
    time.sleep(0.1)
    lock.acquire()
    try:
        # Simulate database interaction (using dbm.sqlite3)
        db = dbm.open('mydatabase', 'c')
        db[str(id)] = data
        db.close()
    except Exception as e:
        print(f"Error in worker {id}: {e}")
    finally:
        lock.release()


def main():
    lock = threading.Lock()
    num_threads = 5
    data_items = ["data" + str(i) for i in range(10)]

    threads = []
    for i, item in enumerate(data_items):
        thread = threading.Thread(target=worker, args=(i, item, lock))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Example of using replace
    my_object = {'a': 1, 'b': 2, 'c': 3}
    new_object = copy.replace(my_object, a=4)  # Example of a replace call
    print(f"Original object: {my_object}")
    print(f"New object: {new_object}")


    # Example of testing ssl
    try:
        context = ssl.create_default_context()
        # Replace with your real certificate/connection
        with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
            s.connect(('localhost', 443))
            print('Connected to server using SSL.')
    except ssl.SSLError as e:
      print(f"SSL Error: {e}")
    


if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import dbm.sqlite3
import typing
import random

def worker(data: typing.List[int], lock, thread_id):
    for i in data:
        # Simulate some work that can be JIT-compiled.
        time.sleep(0.001 + random.random() * 0.001)  # Introduce randomness
        lock.acquire()
        try:
            # Potential race condition.
            # Notice this thread is not using the GIL.
            # This code now can be executed by multi-threading.
            temp = i * 2
            
            # Introduce potential corruption by overwriting with a string.
            # if i % 2 == 0:
            #     data[i] = "hello"  # Potentially corrupting the data list


            #Error induction
            if random.random() < 0.1:
              raise ValueError(f"Error from thread {thread_id}")

        finally:
            lock.release()


def main():
    data = list(range(1000))
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data, lock, i)) #Added thread id
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")

    # Example using dbm.sqlite3
    try:
        db = dbm.sqlite3.open("mydatabase.db", 'c')  # 'c' mode creates the DB
        db['key1'] = 'value1'
        
        # Fuzzing the dbm module with malformed key
        try:
           db[str(123) * 1000] = 'value2'
        except Exception as e:
           print(f"Error writing to database: {e}")
        
        db.close()
    except Exception as e:
        print(f"Database error: {e}")

    # Introducing a potential copy issue.  This might be problematic.
    copied_data = copy.copy(data)
    print("Copied data:", copied_data)



if __name__ == "__main__":
    main()

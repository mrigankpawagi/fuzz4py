
import threading
import time
import copy
import ssl
import os
import dbm
import random

def threaded_function(i, data, lock):
    # Simulate a potentially slow operation
    time.sleep(random.uniform(0.05, 0.15))  # Introduce randomness
    with lock:
        try:
            data[i] += 1
            return data[i]
        except IndexError as e:
            print(f"Caught IndexError in thread {threading.current_thread().name}: {e}")
            return None

def main():
    data = [0] * 100  # Shared data
    lock = threading.Lock() # Added lock for thread safety
    threads = []

    for i in range(10):
        thread = threading.Thread(target=threaded_function, args=(i, data, lock))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print("Final data:", data)

    # Testing copy.replace() - replace values in list (with potential for errors)
    try:
      new_data = copy.deepcopy(data)
      new_data[random.randint(0, 99)] = new_data[random.randint(0, 99)] + random.randint(1, 1000)
      print("Modified data:", new_data)
    except Exception as e:
        print(f"Error with copy.replace(): {e}")


    # Testing dbm.sqlite3 - example usage (with potential for errors)
    try:
        db = dbm.open('mydatabase', 'c')
        key = "key" + str(random.randint(1, 1000))
        db[key] = str(random.randint(1000, 20000)) # Adding random data
        value = db.get(key)
        if value:
            print("Database value:", value)
        else:
            print("Database key not found")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Testing os.times() - timing (introduce a potential race condition probe)
    start_time = os.times()[0]
    try:
      other_thread = threading.Thread(target=lambda: time.sleep(random.uniform(0.05, 0.15)))  # Introduce a second thread
      other_thread.start()
      time.sleep(random.uniform(0.05, 0.15))  # Introduce a slight sleep
      other_thread.join()
    except Exception as e:
        print(f"Error during os.times(): {e}")

    end_time = os.times()[0]
    print("Time elapsed:", end_time - start_time)


    # Attempting ssl.create_default_context() - more robust example
    try:
        context = ssl.create_default_context()
        # Probe with a different protocol version
        context.options |= ssl.OP_NO_SSLv3
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    main()

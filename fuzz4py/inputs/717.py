
import threading
import time
import copy
import ssl
import os
import dbm

def threaded_function(i, data):
    # Simulate a potentially slow operation
    time.sleep(0.1)
    # Access shared data in a race condition-prone way
    data[i] += 1
    try:
        return data[i]
    except IndexError as e:
        print(f"Caught IndexError in thread {threading.current_thread().name}: {e}")
        return None

def main():
    data = [0] * 100  # Shared data
    threads = []

    for i in range(10):
        thread = threading.Thread(target=threaded_function, args=(i, data))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print("Final data:", data)

    # Testing copy.replace() - replace values in list
    new_data = copy.deepcopy(data)
    new_data[5] = new_data[5] + 100

    # Testing dbm.sqlite3 - example usage
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print("Database value:", value)
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Testing os.times() - timing
    start_time = os.times()[0]
    time.sleep(0.2)
    end_time = os.times()[0]
    print("Time elapsed:", end_time - start_time)



    # Attempting ssl.create_default_context() - example use (should work, but is just a probe)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully")
    except Exception as e:
        print(f"Error creating SSL context: {e}")


if __name__ == "__main__":
    main()

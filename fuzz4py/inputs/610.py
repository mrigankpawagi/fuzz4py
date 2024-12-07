
import threading
import time
import copy
import os
import ssl
import typing
import socket

def worker(data: int, lock):
    # Simulate a potentially long operation
    time.sleep(0.1)
    with lock:
        print(f"Thread {threading.current_thread().name} processed {data}")


def main():
    # Example usage of free threading
    lock = threading.Lock()
    threads = []
    data_list: list[int] = [i for i in range(5)]

    for data in data_list:
        thread = threading.Thread(target=worker, args=(data, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # Example with dbm.sqlite3 (simulated, no actual database)
    try:
        dbm_data = {'key1': 'value1'}
        # Simulate database operation, potentially vulnerable to SQL injection if real dbm
        # Replace with actual dbm operation if possible
        with open("dbm_temp", "w") as file:
            file.write(str(dbm_data))  # Store data temporarily for demo
        print("Simulated dbm operation completed.")

        # Retrieve data
        with open("dbm_temp", "r") as file:
            dbm_result = file.read()
        print(f"Retrieved dbm data: {dbm_result}")
        os.remove("dbm_temp")

    except Exception as e:
        print(f"Error in dbm operation: {e}")

    # Example of copy.replace()
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __replace__(self, **kwargs):
            result = copy.copy(self)
            for key, value in kwargs.items():
                setattr(result, key, value)
            return result

    point = Point(1, 2)
    replaced_point = copy.replace(point, x=3)
    print(f"Replaced point: x={replaced_point.x}, y={replaced_point.y}")


    # Example of ssl connection (using a dummy certificate, avoid real certificates)
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(
            socket.socket(), server_hostname="localhost"
        ) as s:
            print("Successfully created SSL context.")

    except Exception as e:
        print(f"Error in SSL operation: {e}")

if __name__ == "__main__":
  main()

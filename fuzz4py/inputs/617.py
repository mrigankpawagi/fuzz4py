
import threading
import time
import copy
import os
import ssl
import socket
import dbm
import typing

def worker(data: int, lock):
    # Simulate a potentially long operation
    time.sleep(0.1)
    with lock:
        print(f"Thread {threading.current_thread().name} processed {data}")


def main():
    # Example usage of free threading
    lock = threading.Lock()
    threads = []
    data_list: list[int] = list(range(5))

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
        with open("dbm_temp.txt", "w") as file:
            import json
            file.write(json.dumps(dbm_data))  # Store data temporarily for demo
        print("Simulated dbm operation completed.")

        # Retrieve data
        with open("dbm_temp.txt", "r") as file:
            dbm_result = file.read()
        print(f"Retrieved dbm data: {dbm_result}")
        os.remove("dbm_temp.txt")

    except Exception as e:
        print(f"Error in dbm operation: {e}")

    # Example of copy.replace()
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __copy__(self):
            return Point(self.x, self.y)
        
        def __replace__(self, x=None, y=None):
            new_point = copy.copy(self)
            if x is not None:
                new_point.x = x
            if y is not None:
                new_point.y = y
            return new_point

    point = Point(1, 2)
    replaced_point = point.__replace__(x=3)
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


def worker2(data, lock):
    try:
        lock.acquire()
        # Simulate a potentially long operation
        time.sleep(0.1)  # Simulate work
        # Simulate data modification - Using deepcopy is crucial
        new_data = copy.deepcopy(data)
        new_data.append(new_data[-1] + 1)
        
        #Attempt to use dbm.sqlite3
        try:
            db = dbm.open('mydatabase', 'c')
            db[str(new_data[-1])] = str(new_data[-1])
            db.close()
        except Exception as e:
            print(f"Error interacting with dbm: {e}")
        
        # Important - modify the shared data structure outside the critical section
        data[:] = new_data[:] #modifies the original shared list
    
    except Exception as e:
        print(f"Error in worker thread: {e}")
    finally:
        lock.release()


def main2():
    data = [1]
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker2, args=(copy.deepcopy(data), lock)) #crucial for each thread getting a fresh copy
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data: {data}")


    #Testing SSL - Likely would be a part of a larger program
    try:
        context = ssl.create_default_context()
        #replace with certificate handling - simplified example
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))
            print('Connection established with example.com')
    except Exception as e:
        print("Error during SSL connection:", e)
    

    #Test the new replace protocol for copy module 
    class MyData(typing.NamedTuple):
        x: int
        y: str
    d = MyData(1, 'hello')
    d2 = copy.replace(d._replace(x=2))
    print(d)
    print(d2)

if __name__ == "__main__":
    main()
    main2()

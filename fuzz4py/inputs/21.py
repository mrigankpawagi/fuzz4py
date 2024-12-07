
import threading
import time
import copy
import dbm.sqlite3
import ssl
import socket
import typing

def worker(data: typing.List[int], lock):
    try:
        # Simulate some work
        for i in data:
            time.sleep(0.01)
        with lock:
            # Potentially problematic access/modification
            data.append(1000)  # Critical section
    except Exception as e:
        print(f"Worker thread {threading.get_ident()} caught exception: {e}")


def main():
    data = list(range(100))
    lock = threading.Lock()
    threads = []

    # Create multiple threads
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), lock))  # Deep copy is crucial
        threads.append(thread)
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

    # Check for integrity of data
    if len(data) != 105:
        raise Exception("Incorrect data length after threading")

    # Using new dbm.sqlite3 module
    try:
      db = dbm.sqlite3.open('test.db', 'c')
      db['key'] = 'value'
      db.close()
    except Exception as e:
      print(f"Error with dbm.sqlite3: {e}")

    # Test ssl with a simplified context
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname="example.com") as s:
            s.connect(('example.com', 443))
    except Exception as e:
      print(f"Error with ssl: {e}")


if __name__ == "__main__":
    main()

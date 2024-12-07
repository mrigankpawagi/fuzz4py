
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(data, lock):
    # Simulate some work that could be JIT-compiled
    result = sum(data)
    with lock:
        print(f"Thread {threading.get_ident()} result: {result}")
    time.sleep(0.1)

def main():
    data = list(range(10000))
    lock = threading.Lock()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Example using dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()

        db = dbm.open('mydatabase', 'r')
        print(f"Retrieved key: {db['key1']}")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Example using ssl
    try:
        context = ssl.create_default_context()
        # Replace with a valid certificate path for testing purposes
        with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
            s.connect(('localhost', 443))  # Replace with appropriate port
            print("SSL connection successful.")
    except ssl.SSLError as e:
        print(f"SSL connection error: {e}")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()


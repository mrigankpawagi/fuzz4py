
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing

def race_condition_example(data: int, lock: threading.Lock):
    lock.acquire()
    try:
        time.sleep(0.01)  # Introduce a delay for potential race
        data += 1
    finally:
        lock.release()
    return data

def fuzz_dbm(db_name: str, data: dict):
    try:
        with dbm.open(db_name, 'c') as db:
            for key, value in data.items():
                db[key] = value
            result = db.get('test_key', 'key not found')  #Handle missing key gracefully
            return result
    except Exception as e:
        return str(e)
    
def fuzz_copy_replace(obj: copy.MutableMapping):
    try:
        new_obj = copy.copy(obj)  # create a copy, essential for proper replace
        new_obj['x'] = 10
        return new_obj
    except Exception as e:
        return str(e)

def fuzz_ssl():
    try:
        context = ssl.create_default_context()
        # Simulate a connection attempt with potential invalid certs
        # Use a dummy socket
        dummy_socket = socket.socket()
        with context.wrap_socket(dummy_socket, server_hostname='invalid_hostname'):
          # Simulate reading from the socket. Replace with actual read if needed.
          dummy_socket.recv(1024)  
          return "SSL connection established"
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    lock = threading.Lock()
    data = 0
    threads = []
    for _ in range(5):
        t = threading.Thread(target=race_condition_example, args=(data, lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final data: {data}")  #Potential race condition output

    db_data = {'test_key': 'value', 'another_key': 'another_value'}
    db_result = fuzz_dbm('test_db', db_data)
    print(f"DBM Result: {db_result}")

    example_obj = {'x': 5, 'y': 10}
    replace_result = fuzz_copy_replace(example_obj)
    print(f"Copy Replace Result: {replace_result}")

    ssl_result = fuzz_ssl()
    print(f"SSL Result: {ssl_result}")


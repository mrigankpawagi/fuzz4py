
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing
import random
import sys

def race_condition_example(data: int, lock: threading.Lock, seed: int):
    lock.acquire()
    try:
        time.sleep(random.uniform(0.001, 0.05))  # Variable delay
        data += 1
        if seed % 2 == 0:  # Introduce potential corruption
            data = -1
    finally:
        lock.release()
    return data

def fuzz_dbm(db_name: str, data: dict, seed: int):
    try:
        with dbm.open(db_name, 'c') as db:
            for key, value in data.items():
                db[key] = str(value)  # Handle non-string values
                
                if seed % 3 == 0:
                    db[key] = None  # Introduce a None value for testing
                elif seed % 5 == 0:
                    db[key] = b"invalidbytes"  # Test with binary data
            
            if seed % 7 == 0:
                key_to_find = 'nonexistent_key'
            else:
                key_to_find = 'test_key'  # Test with different key names

            result = db.get(key_to_find, 'key not found') 
            return result
    except Exception as e:
        return str(e)

def fuzz_copy_replace(obj: copy.MutableMapping, seed: int):
    try:
        new_obj = copy.copy(obj)
        if seed % 2 == 0:
          new_obj = copy.deepcopy(obj)  #Introduce a deepcopy for potential issues.

        if seed % 3 == 0:
          new_obj['x'] = 12345678901234567890
        else:
          new_obj['x'] = 10
        return new_obj
    except Exception as e:
        return str(e)


def fuzz_ssl():
    try:
      context = ssl.create_default_context()
      
      #Simulate different hostnames. More comprehensive testing
      hostnames = ['invalid_hostname', 'another_hostname', 'localhost']
      hostname = random.choice(hostnames)
      
      dummy_socket = socket.socket()
      with context.wrap_socket(dummy_socket, server_hostname=hostname):
        dummy_socket.recv(1024)
        return "SSL connection established"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    seed = int(time.time()) #Seed using current time
    random.seed(seed) #seed random
    lock = threading.Lock()
    data = 0
    threads = []
    for i in range(5):
        t = threading.Thread(target=race_condition_example, args=(data, lock, i))  # Pass seed to each thread
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final data: {data}")

    db_data = {'test_key': 'value', 'another_key': 'another_value'}
    db_result = fuzz_dbm('test_db', db_data, seed)
    print(f"DBM Result: {db_result}")

    example_obj = {'x': 5, 'y': 10}
    replace_result = fuzz_copy_replace(example_obj, seed)
    print(f"Copy Replace Result: {replace_result}")

    ssl_result = fuzz_ssl()
    print(f"SSL Result: {ssl_result}")

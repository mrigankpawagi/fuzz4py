
import threading
import copy
import os
import ssl
import typing
import dbm
import time
import socket

# Fuzzing example using free-threading (PEP 703)
def worker(data: list, lock: threading.Lock):
    try:
        with lock:
            data.append(data[0] * 2)
    except Exception as e:
        # Critical race condition example
        data.append("Error: " + str(e))
    return

def main_part1():
    data = [10]
    lock = threading.Lock()
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=worker, args=(copy.copy(data), lock))  # Fuzzing copy
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(data)
    
    # Example using dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')  # Fuzz opening
        db['key'] = 'value'
        value = db['key']
        print(f"Value retrieved: {value}")
        db.close()
    except Exception as e:
        print(f"DB Error: {e}")
    

    # Example using os timer
    start_time = time.perf_counter_ns()
    # ... some operation (replace with a meaningful operation)
    time.sleep(1)  # Simulate operation
    end_time = time.perf_counter_ns()
    print(f"Operation took {end_time - start_time} ns")

    # Example of ssl
    try:
        context = ssl.create_default_context()
        # Add certificate fuzzing here - this is a placeholder
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))
            s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            response = s.recv(1024)
            print(response)

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

    # Example of typing annotations
    def my_func(arg: typing.List[int]) -> typing.List[int]:
        return [x * 2 for x in arg]

    result = my_func([1, 2, 3])
    print(result)

def worker_part2(data, lock):
    try:
        # Simulate work, potentially using a C extension
        intermediate_result = data * 2
        # Simulate database interaction
        with dbm.open('mydatabase', 'c') as db:
            db[str(intermediate_result)] = str(time.time())
            
    except Exception as e:
        lock.acquire()
        print(f"Error in worker: {e}")
        lock.release()
    finally:
      lock.release()


def main_part2():
    data = 10
    lock = threading.Lock()
    threads = []
    
    for i in range(5):
        t = threading.Thread(target=worker_part2, args=(data, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    try:
      with dbm.open('mydatabase','r') as db:
        for key in db:
          print(f"Key: {key}, Value: {db[key]}")
    except Exception as e:
      print(f"Error accessing database: {e}")
    finally:
      try:
        os.remove('mydatabase')
      except:
        pass

if __name__ == "__main__":
    main_part1()
    main_part2()


import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket
import random

def worker(data: typing.List[int], lock):
    with lock:
        for i in range(len(data)):
            try:
              time.sleep(data[i] / 1000.0)
              data[i] += 1
              time.sleep(0.001 * (data[i] % 3))
              if data[i] % 2 == 0:
                try:
                  del data[data.index(data[i])]
                except IndexError:
                  pass
              try:
                # Fuzzing: Introduce potential for IndexError
                # Add a possibility of appending None, a string, or a large integer
                data.append(data[i] + random.randint(-5, 5) if random.random() < 0.8 else None if random.random() < 0.1 else "fuzz" if random.random() < 0.1 else 10**100)
              except IndexError:
                print(f"Error in worker (appending): {i}, {data[i]}")
              except TypeError as e:
                print(f"Error in worker: {e}")
            except IndexError as e:
              print(f"Error in worker (index): {e}")
            except Exception as e:
              print(f"Unexpected error in worker: {e}")
                
                


def main():
    # Fuzzing: Varying data sizes
    data_size = random.randint(50, 200)
    data = list(range(data_size))
    lock = threading.Lock()
    threads = []

    # Fuzzing: Varying number of threads
    num_threads = random.randint(10, 30)

    for i in range(num_threads):
        threads.append(threading.Thread(target=worker, args=(copy.deepcopy(data), lock)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    try:
        # Fuzzing: Check for unexpected data types in list
        for i in range(len(data)):
            if not isinstance(data[i], int):
                print(f"Error: Data element {i} is not an integer. It is: {type(data[i])}")
            elif data[i] != i + 1:
                print(f"Error: Data element {i} should be {i+1}, but it is {data[i]}")
    except IndexError:
        print("Error: Index out of bounds")

    # Fuzzing: Using a potentially invalid host
    try:
        fuzz_hostname = "not_a_real_host"  # Introduce a fuzzed value.
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=fuzz_hostname) as s:
            s.connect(('example.com', 443)) # Use 'example.com' as a correct target
            print("SSL connection established successfully.")
            s.sendall(b"Fuzzing test string")
            response = s.recv(1024)
            print(f"Received: {response.decode()}")
    except ssl.SSLError as e:
        print(f"SSL connection failed: {e}")


    try:
        # Fuzzing: Using malformed database key.
        db = dbm.open('test.db', 'c')
        # Fuzzing: Varying key size and data types
        fuzz_key = b'\x00' * random.randint(100, 500)
        db['key'] = fuzz_key
        db.close()
        print('Database operation successful.')
    except dbm.error as e:
        print(f"Error opening/accessing database: {e}")

if __name__ == "__main__":
    main()

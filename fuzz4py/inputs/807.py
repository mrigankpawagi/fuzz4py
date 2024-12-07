
import threading
import time
import copy
import ssl
import dbm
import os
import typing
import socket
import random

# Fuzzing example targeting free-threading, JIT, and copy.replace()
def my_function(data, iterations):
    result = 0
    for i in range(iterations):
        try:
            multiplier = random.randint(-10, 10)
            if multiplier == 0:
                multiplier = 1
            result += data[i] * multiplier
        except IndexError:
            return -1
    
    try:
        new_data = copy.copy(data)
        new_data = new_data._replace(field1=random.randint(0, 100))
    except AttributeError:
        pass
    
    if iterations % 2 == 0:
        result *= 2
    elif iterations % 3 == 0:
        result += 1
    return result

# Example class implementing the replace protocol
class MyData(typing.NamedTuple):
    field1: int
    field2: str

# Example with the new dbm.sqlite3 module

result = 0
try:
    db_file = "mydatabase"
    db = dbm.open(db_file, 'c')
    for i in range(10):
        key = str(i)
        value = str(random.randint(0, 1000))
        db[key] = value
    db.close()

    db = dbm.open(db_file, 'r')
    for i in range(10):
        key = str(i)
        try:
            value = db[key]
            print(f"Key: {key}, Value: {value}")
        except KeyError:
            print(f"KeyError for key {key}")
    db.close()
    os.remove(db_file)

except Exception as e:
    print(f"Database error: {e}")


def worker(data, iterations):
    global result
    try:
        result += my_function(data, random.randint(1, iterations))
    except (TypeError, IndexError):
        pass  # Catch specific errors

data = [random.randint(0, 1000) for _ in range(1000)]
iterations = 10000

threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(data, iterations))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Result: {result}")



try:
  context = ssl.create_default_context()
  context.verify_mode = ssl.CERT_REQUIRED
  for i in range(5):
    hostname = f"fuzz-hostname-{i}.com"
    port = random.randint(1, 65535)
    try:
      with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        try:
          s.connect((hostname, port))
          print(f"Connected to {hostname}:{port}")
          request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
          s.sendall(request.encode())
          response = s.recv(4096)
          print(response.decode())
        except (OSError, ssl.SSLError) as e:
          print(f"Error connecting to {hostname}:{port}: {e}")
    except Exception as e:
      print(f"Error in SSL connection test: {e}")

except ssl.SSLError as e:
    print("SSL Error:", e)


# Fuzzing timer functions (with more variations)
try:
    for i in range(5):
        start_time = time.perf_counter()
        cpu_times = os.times()
        elapsed_time = time.perf_counter() - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        print(f"CPU times: {cpu_times}")
        time.sleep(random.uniform(0.1, 1))
except Exception as e:
    print(f"Error with timer: {e}")

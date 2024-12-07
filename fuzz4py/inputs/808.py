
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
    try:
        for i in range(iterations):
            multiplier = random.randint(-100, 100)  # Wider range
            if multiplier == 0:
                multiplier = 1
            result += data[i] * multiplier
            if i > len(data):
                raise IndexError
        
        #Fuzzing with different types
        if iterations % 2 == 0:
            new_data = copy.deepcopy(data)
        elif iterations % 3 == 0:
            try:
                new_data = copy.deepcopy(data)
                new_data[0] = "bad input"
            except TypeError:
                pass
            
        try:
          new_data = copy.copy(data)
          new_data = new_data._replace(field1=random.randint(0, 1000000)) #Fuzzing large numbers
        except AttributeError:
          pass
        except TypeError:
          pass

        if iterations % 2 == 0:
            result *= 2
        elif iterations % 3 == 0:
            result += 1

        return result
    except (IndexError, TypeError, AttributeError):
        return -1

# Example class implementing the replace protocol
class MyData(typing.NamedTuple):
    field1: int
    field2: str = "default"  # Add a default value

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
        key = str(i) + "a"  #Fuzzing with additional characters
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
    except (TypeError, IndexError, AttributeError):
        result = -2 # Indicate error case

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
  context.verify_mode = ssl.CERT_REQUIRED  # Critical for security
  context.check_hostname = True  # Essential for hostname validation
  for i in range(5):
    hostname = f"fuzz-hostname-{i}.com"
    port = random.randint(1, 65535)
    try:
      with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.settimeout(5)  # Add timeout to avoid indefinite hangs
        try:
          s.connect((hostname, port))
          print(f"Connected to {hostname}:{port}")
          #Fuzzing with various headers and methods
          request = f"POST / HTTP/1.1\r\nHost: {hostname}\r\nContent-Length: 10\r\n\r\nfuzzdata"
          s.sendall(request.encode())
          response = s.recv(4096)
          print(response.decode())
        except (OSError, ssl.SSLError, socket.timeout) as e:
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
        time.sleep(random.uniform(0.1, 1))  #Fuzz different sleep times
except Exception as e:
    print(f"Error with timer: {e}")

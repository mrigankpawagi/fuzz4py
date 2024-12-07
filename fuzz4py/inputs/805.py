
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
    # This loop is designed to be JIT compiled.  Fuzzing addition with data
    result = 0
    for i in range(iterations):
        try:
            #Fuzzing by multiplying by random values
            multiplier = random.randint(-10, 10)
            if multiplier == 0:
                multiplier = 1
            result += data[i] * multiplier  
        except IndexError as e:
            print(f"IndexError in my_function: {e}")
            return -1  # Indicate error
    
    # Use copy.replace() to modify a copy of the data.
    # This illustrates a possible interaction with free-threading
    try:
        new_data = copy.copy(data)  
        #Fuzzing by replacing with random values
        new_data = new_data._replace(field1=random.randint(0, 100))
    except AttributeError:
        pass #Handle cases where data doesn't support replace
    
    #Fuzz with different operations
    if iterations % 2 == 0:
        result = result * 2
    elif iterations % 3 == 0:
        result = result + 1

    return result

# Example class implementing the replace protocol
class MyData(typing.NamedTuple):
    field1: int
    field2: str

# Example with the new dbm.sqlite3 module

result = 0 # Initialize the global result
try:
    db_file = "mydatabase"
    db = dbm.open(db_file, 'c')  # Fuzzing with different modes
    for i in range(10):
      key = str(i)
      value = str(random.randint(0, 1000))
      db[key] = value  # Fuzzing with different types of data
    db.close()

    db = dbm.open(db_file, 'r')
    for i in range(10):
        key = str(i)
        try:
            value = db[key]
            print(f"Key: {key}, Value: {value}")
        except KeyError as e:
            print(f"KeyError: {e}")
    db.close()

    os.remove(db_file) # Clean up the database file.

except Exception as e:
    print(f"Database error: {e}")


# Demonstrate free-threading,  possibly causing race condition
def worker(data,iterations):
    global result
    try:
        result += my_function(data, random.randint(1, iterations)) # Fuzz iteration count
    except TypeError as e:
        print(f"TypeError in worker: {e}")
    except Exception as e:
      print(f"Error in worker: {e}")
    
    
data = [random.randint(0, 1000) for _ in range(1000)]  #Random Data
iterations = 10000


threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(data, iterations))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Result: {result}")



# Fuzzing with custom data objects and ssl
try:
  context = ssl.create_default_context()
  context.verify_mode = ssl.CERT_REQUIRED # Example of stricter SSL check

  # Fuzzing with random hostnames and ports
  for i in range(5):  # More iterations for better fuzzing coverage
    hostname = f"fuzz-hostname-{i}.com"  # More diverse hostnames
    port = random.randint(1, 65535)
    try:
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            try:
              s.connect((hostname, port))
              print(f"Connected to {hostname}:{port}")
              # Fuzzing with random HTTP requests
              request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
              s.sendall(request.encode())
              response = s.recv(4096)
              print(response.decode())
            except OSError as e:
              print(f"Connection error to {hostname}:{port}: {e}")
            except ssl.SSLError as e:
              print(f"SSL error during connection to {hostname}:{port}: {e}")

    except Exception as e:
        print(f"Error in SSL connection test: {e}")

except ssl.SSLError as e:
    print("SSL Error:",e)


# Fuzzing timer functions (with more variations)
try:
    for i in range(5):
        start_time = time.perf_counter()
        cpu_times = os.times()
        elapsed_time = time.perf_counter() - start_time
        print(f"Elapsed time (perf_counter): {elapsed_time:.6f} seconds")
        print(f"CPU times (os.times()): {cpu_times}")
        time.sleep(random.uniform(0.1, 1))  # Introduce random delays

except Exception as e:
    print("Error with Timer:", e)



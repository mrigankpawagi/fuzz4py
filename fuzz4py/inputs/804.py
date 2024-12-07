
import threading
import time
import copy
import ssl
import dbm
import os
import typing
import socket

# Fuzzing example targeting free-threading, JIT, and copy.replace()
def my_function(data, iterations):
    # This loop is designed to be JIT compiled.  Fuzzing addition with data
    result = 0
    for i in range(iterations):
        try:
            result += data[i] * 2  # Fuzzing by multiplying by 2
        except IndexError as e:
            print(f"IndexError in my_function: {e}")
            return -1  # Indicate error
    
    # Use copy.replace() to modify a copy of the data.
    # This illustrates a possible interaction with free-threading
    try:
        new_data = copy.copy(data)  
        new_data = new_data._replace(field1=42) # Replace only if data supports it.
    except AttributeError:
        pass #Handle cases where data doesn't support replace
    
    #Fuzz with different operations
    if iterations % 2 == 0:
        result = result * 2
    
    return result

# Example class implementing the replace protocol
class MyData(typing.NamedTuple):
    field1: int
    field2: str

# Example with the new dbm.sqlite3 module

result = 0 # Initialize the global result
try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'
    db['key2'] = b'binary_value'  # Adding a binary key
    db.close()

    db = dbm.open('mydatabase', 'r')
    value = db['key1']
    binary_value = db['key2']  # Accessing the binary key
    db.close()
    os.remove("mydatabase")  # Clean up the database file.

except Exception as e:
    print(f"Database error: {e}")


# Demonstrate free-threading,  possibly causing race condition
def worker(data,iterations):
    global result
    try:
        result += my_function(data, iterations)
    except TypeError as e:
        print(f"TypeError in worker: {e}")
        
    
data = [1] * 1000
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
  
  # Fuzzing with different hostnames, invalid hostnames, and invalid ports
  for hostname in ["example.com", "invalid-hostname", "127.0.0.1"]:
    for port in [443, 80, 1]:
      
        try:
            with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
                try:
                    s.connect((hostname, port))
                    print(f"Connected to {hostname}:{port}")
                    s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")  #Example HTTP request
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


# Fuzzing timer functions
try:
    start_time = time.perf_counter()
    cpu_times = os.times()
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time (perf_counter): {elapsed_time:.6f} seconds")
    print(f"CPU times (os.times()): {cpu_times}")

except Exception as e:
    print("Error with Timer:", e)


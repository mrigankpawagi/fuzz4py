
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
    # This loop is designed to be JIT compiled.
    result = 0
    for i in range(iterations):
        result += data[i]

    # Use copy.replace() to modify a copy of the data.
    # This illustrates a possible interaction with free-threading
    try:
        new_data = copy.copy(data)  
        new_data = new_data._replace(field1=42) # Replace only if data supports it.
    except AttributeError:
        pass #Handle cases where data doesn't support replace

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
    db.close()

    db = dbm.open('mydatabase', 'r')
    value = db['key1']
    db.close()
    os.remove("mydatabase")  # Clean up the database file.

except Exception as e:
    print(f"Database error: {e}")


# Demonstrate free-threading,  possibly causing race condition
def worker(data,iterations):
    global result
    result += my_function(data, iterations)

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
  
  # Example of using the context (replace with your test code)
  # Using a dummy socket and hostname to avoid needing a real server
  with context.wrap_socket(socket.socket(), server_hostname="example.com") as s:
      try:
        s.connect(("example.com", 443))  # Replace with your desired test, using a dummy server or testing a known good cert.
        s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")  #Example HTTP request
        response = s.recv(4096)
        print(response.decode()) # print the response
      except OSError as e:
        print(f"Connection error: {e}")
      except ssl.SSLError as e: # Handle SSL errors separately
          print(f"SSL error during connection: {e}")

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


import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket

def worker(data, context):
    try:
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as sock:
            #Simulate work with potentially problematic data
            # Introducing fuzzing input variations
            try:
              result = int(data) * 100  #  Potential for overflow.  Try different data types
            except ValueError:
              result = data
            #Introduce a potential error to create fuzzing condition
            if len(str(data)) > 100:  # Check string length to catch various types
                raise ValueError("Data too long!")

            db = dbm.open('mydatabase', 'c') # Use sqlite3 backend
            try:
              db[str(result)] = time.time()  #Store as string to handle different data types
            except Exception as e:
              print(f"Error writing to db: {e}")
            db.close()

            sock.sendall(b'some data')
            #Fuzzing: send malformed data or data with different types
            try:
              sock.sendall(data.encode())  # Encode to bytes to handle different data types
            except Exception as e:
                print(f"Error sending data: {e}")

    except ValueError as e:
        print(f"ValueError in worker: {e}")
    except Exception as e:
        print(f"Error in worker: {e}")

def main():
  # Test with and without GIL
  context = ssl.create_default_context()  # Create a context object
  context.check_hostname = False  # Add this to simplify the test case

  #Fuzzing: using different data types
  data_types = [123, "someData", b"binaryData", None, True, [1,2,3], bytearray(10), object(), 1234567890, -10, 3.14, "", "   ", b"", bytearray(0)]
  for data in data_types:
      threads = []
      for i in range(5):
        try:
          t = threading.Thread(target=worker, args=(str(data), context)) # Convert to string for consistency
          threads.append(t)
          t.start()
        except Exception as e:
            print(f"Error creating thread for {data}: {e}")
      for t in threads:
        try:
          t.join()
        except Exception as e:
          print(f"Error joining thread: {e}")

  # Fuzzing with different data types and annotations.  More complex data
  data = [1, 2, 3, "hello", True, "longer string", object(), [], {}, None, 1234567890, 3.14159,  [1,2,3, 10000], {"a":1, "b":[1,2,3]}, (1,2,3), {1:2, 3:4},  {"a": 1, "b": [1, 2, 3, [1, 2]]}, lambda x: x * 2,  {"a": lambda x: x * 2},  {"a": [1,2,3, lambda x: x * 2]}]
  try:
    for item in data:
      threads = []
      for i in range(5):
        try:
          thread = threading.Thread(target=worker, args=(str(item), context))
          threads.append(thread)
          thread.start()
        except Exception as e:
          print(f"Error creating thread for {item}: {e}")
      for thread in threads:
        try:
          thread.join()
        except Exception as e:
          print(f"Error joining thread: {e}")
  except Exception as e:
      print(f"Error in main loop for more complex data: {e}")


  # Fuzzing with invalid data and data that trigger exception (Expanded)
  malformed_data = [123, "someData", b"binaryData", None, True, [1,2,3], bytearray(10), None, object(),  b"\x00\xff", b"\x00", b"\xff", "", "   ", b"", bytearray(0), b"\x00\x01\x02\x03", b"\xff\x01", b'\x00\x00\x00', b'\xff\xff'] # Added more types and edge cases


  try:
    for item in malformed_data:
      threads = []
      for i in range(5):
        try:
          thread = threading.Thread(target=worker, args=(str(item), context))
          threads.append(thread)
          thread.start()
        except Exception as e:
          print(f"Error creating thread for {item}: {e}")
      for thread in threads:
        try:
          thread.join()
        except Exception as e:
          print(f"Error joining thread: {e}")
  except Exception as e:
    print(f"Error in main loop for malformed data: {e}")


  # Cleanup - This is crucial for fuzzing testing.  Ensuring the file is closed
  try:
    import shutil
    shutil.rmtree('mydatabase', ignore_errors=True)
  except Exception as e:
    print(f"Error cleaning up database: {e}")

if __name__ == "__main__":
  import socket
  main()

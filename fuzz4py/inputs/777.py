
import threading
import copy
import os
import ssl
import sqlite3
import typing

def complex_function(data: typing.List[int],  key: int) -> typing.List[int]:
    """
    A complex function demonstrating free-threading and annotation usage.
    """
    results = []
    for item in data:
        results.append(item * key)
    return results


def multithreaded_test(data: typing.List[int], num_threads: int, key):
    """
    A multi-threaded function demonstrating potential race conditions.
    """

    threads = []
    results = []
  
    for i in range(num_threads):
        thread = threading.Thread(target=lambda x=i: results.append(complex_function(data[x*len(data)//num_threads:(x+1)*len(data)//num_threads],key))) 
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results



#Fuzzing the os.stat() function with varying time values
try:
  stat_result = os.stat("/tmp/testfile")
  print(stat_result.st_mtime) #Demonstrates using result of os.stat.
except FileNotFoundError:
  print("Test file not found. Creating a dummy file")
  with open("/tmp/testfile", "w") as f:
    f.write("dummy data")
  stat_result = os.stat("/tmp/testfile")
  print(stat_result.st_mtime)


# Fuzzing dbm.sqlite3
try:
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT)")
  cursor.execute("INSERT INTO test (data) VALUES (?)", ('malformed data' , ))
  conn.commit()  # Important to commit changes

  cursor.execute("SELECT * FROM test")
  results = cursor.fetchall()
  print(results)
except sqlite3.Error as e:
  print(f"Error interacting with dbm.sqlite3: {e}")

# Demonstrate replacing protocol functionality
class ReplaceableClass:
    def __init__(self, value: int):
        self.value = value

    def __replace__(self, value: int = None):
        if value is not None:
          self.value = value
        return self

    def __str__(self) -> str:
        return f"Value: {self.value}"

    def some_other_method(self):
        return "Some other functionality"
# Test the ReplaceableClass


new_object = ReplaceableClass(10)
print(new_object)  # Output: Value: 10
replaced_object = new_object.__replace__(20)
print(replaced_object)  # Output: Value: 20


# Basic SSL example, but more complex fuzzing would be needed in a real fuzzer.
context = ssl.create_default_context()
context.verify_mode = ssl.CERT_REQUIRED


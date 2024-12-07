
import threading
import time
import os
import copy
import dbm
import ssl
import typing

def jit_sensitive_function(input_list):
    """
    A function designed to be JIT-compiled, with a tight loop.
    """
    result = 0
    for item in input_list:
        result += item
    return result

def multithreaded_example(data):
    """
    A multi-threaded function to demonstrate free-threading and potential race conditions.
    """
    threads = []
    lock = threading.Lock()
    shared_data = 0

    for i in range(10):
        thread = threading.Thread(target=worker, args=(data,lock, shared_data,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    return shared_data
    
def worker(data, lock, shared_data):
        # Accessing shared resources without the GIL is the focus of this test.

        time.sleep(0.1)
        with lock:
             shared_data += data


def test_annotation_scope():
  """
  A test case demonstrating annotation scopes, including lambdas.
  """
  annotation_dict: typing.Dict[str, typing.Callable[[int], int]] = {
      "add1": lambda x: x + 1
  }

  # Using a complex type annotation in the function itself.
  def complex_function(data: typing.List[int]) -> typing.List[int]:
      return [annotation_dict["add1"](item) for item in data]


def test_replace_protocol():
  """
    Tests the replace protocol with a custom class.
  """
  class MyData:
    def __init__(self, val):
        self.val = val

    def __replace__(self, **kargs):
        return MyData(kargs.get("val", self.val))

  original_data = MyData(5)
  replaced_data = copy.replace(original_data, val=10)
  return replaced_data.val
  

#Example usage demonstrating fuzzing different aspects

# JIT compilation test
jit_result = jit_sensitive_function([1, 2, 3, 4,5])


# Free-threading test with varying data.
data_set = [1, 2, 3, 4]
multithreaded_result = multithreaded_example(data_set)



# Docstring whitespace stripping test (indirect)
# ... (code that uses docstrings with varying whitespace)



# Annotation scopes test
test_annotation_scope()

# Replace protocol test
result_replace = test_replace_protocol()


# DBM test (using sqlite3)
try:
    db = dbm.open('mydatabase', 'c')
    db['key'] = 'value'
    db.close()
except Exception as e:
  print(f"DBM error: {e}")


# SSL test (indirectly, by trying connections)
try:
    context = ssl.create_default_context()
    # Simulate connection attempts
    with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
      s.connect(('example.com', 443))
except Exception as e:
  print(f"SSL error: {e}")

print(f"JIT result: {jit_result}")
print(f"Multithreaded result: {multithreaded_result}")
print(f"Replace protocol result: {result_replace}")


import socket


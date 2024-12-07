
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def jit_sensitive_function(input_list: list[int]) -> int:
    """A function likely to be JIT-compiled due to its loop."""
    total = 0
    for i in input_list:
        total += i
    return total

def test_free_threading(data: int) -> int:
    """Illustrates a potential race condition with free threading."""
    lock = threading.Lock()
    total = 0
    threads = []
    for i in range(data):
        t = threading.Thread(target=lambda x=i: add_to_total(x, lock, total))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return total

def add_to_total(i, lock, total):
    lock.acquire()
    try:
        total += i
    finally:
        lock.release()

def test_copy_replace(data):
  class MyReplaceable:
      def __init__(self, value: int):
          self.value = value

      def __replace__(self, value: int):
          return MyReplaceable(value)


  original = MyReplaceable(data)
  replaced = copy.replace(original, value=data + 10)

  return replaced.value


def test_dbm_sqlite3():
  db = dbm.open('test.db', 'c')
  db['key'] = str(123)
  data = db['key']
  db.close()

def test_os_timer():
  t = os.times()
  return t

def test_ssl_connection():
  try:
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
        s.connect(('example.com', 443))
        return True
  except Exception as e:
    return False


import socket  # Needed for SSL


# Example usage (demonstrating different fuzz targets)
try:
  test_free_threading(10)
  jit_sensitive_function([1, 2, 3, 4, 5])
  test_copy_replace(5)
  test_dbm_sqlite3()
  test_os_timer()
  test_ssl_connection()
except Exception as e:
    print(f"An error occurred: {e}")


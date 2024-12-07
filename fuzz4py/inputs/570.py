
import threading
import copy
import os
import time
import ssl
import dbm
import typing

def test_threading_jit(n: int) -> None:
    """Tests free-threading and JIT compiler with a hot loop."""
    data = [i for i in range(n)]
    lock = threading.Lock()
    
    def worker(i: int) -> None:
        with lock:
            # Potentially JIT-compiled loop
            for _ in range(1000):
                data[i] += 1
                
    threads = []
    for i in range(n):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()


def test_complex_annotations(data: typing.List[typing.Union[int, str]]) -> None:
    """Tests complex type annotations."""
    for item in data:
        if isinstance(item, str):
            item = item.upper()
        else:
            item *= 2
    return data

def test_dbm_sqlite3():
  """Tests dbm.sqlite3 with malformed data."""
  try:
      db = dbm.open('test.db', 'c')
      db['key'] = b'\x00' * 10000  # Large key with null bytes
      db.close()
      db = dbm.open('test.db', 'r')
      value = db['key']
      db.close()
  except Exception as e:
      print(f"Error accessing dbm: {e}")
      
  os.remove('test.db')

def test_os_timer():
  """Tests os.times() with different time values"""
  start_time = time.time()
  result = os.times()
  end_time = time.time()
  print(f"Time elapsed: {end_time - start_time}, Results: {result}")


def test_ssl_connection(cert_path: str) -> None:
  """Tests SSL connections with custom certificates."""
  context = ssl.create_default_context()
  try:
    with open(cert_path, 'rb') as f:
      context.load_verify_locations(cafile=f.read())
    
    # Simulate connection (replace with actual connection logic)
    print("SSL connection attempt with custom certificate")
  except ssl.SSLError as e:
      print(f"SSL Error: {e}")

if __name__ == "__main__":

  test_threading_jit(5)
  test_complex_annotations([1, "hello", 3, "world"])
  test_dbm_sqlite3()
  test_os_timer()
  test_ssl_connection("path/to/custom.pem")  # Replace with a valid path

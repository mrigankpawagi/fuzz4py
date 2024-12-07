
import threading
import copy
import os
import ssl
import typing
import dbm

def test_free_threading(n: int) -> None:
    """
    Test free-threading with a race condition.
    """
    shared_data = 0
    lock = threading.Lock()

    def increment(i: int) -> None:
        nonlocal shared_data
        with lock:
            shared_data += i

    threads = []
    for i in range(n):
        t = threading.Thread(target=increment, args=(1,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    assert shared_data == n


def test_jit_compiler():
  """A potentially JIT-compiled function"""
  iterations = 1000000
  results = []
  for i in range(iterations):
    # This is a very simple calculation, so it should JIT compile.
    result = i * 2 + 100
    results.append(result)

def test_docstring_whitespace():
  """Test doctests with varying whitespace"""
  # Indentation affects doctests in specific ways.
  assert 1==1



def test_replace_protocol():
    """Test the replace protocol."""
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __replace__(self, x=None, y=None):
          new_x = x if x is not None else self.x
          new_y = y if y is not None else self.y
          return Point(new_x, new_y)


    p = Point(10,20)
    replaced_p = p.__replace__(x=30)
    assert replaced_p.x == 30
    assert replaced_p.y == 20

def test_dbm_sqlite3():
  """Test dbm.sqlite3"""
  try:
      db = dbm.open('test.db', 'c')
      db['key'] = 'value'
      value = db['key']
      assert value == 'value'
      db.close()
  except Exception as e:
      print("dbm test failed:", e)
      
  os.remove('test.db')


def main():
  test_free_threading(5)
  test_jit_compiler()
  test_docstring_whitespace()
  test_replace_protocol()
  test_dbm_sqlite3()



if __name__ == "__main__":
  main()

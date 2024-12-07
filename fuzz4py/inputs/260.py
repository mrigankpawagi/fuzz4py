
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def test_free_threading(n: int):
    data = [0] * n
    lock = threading.Lock()

    def worker(i):
        with lock:
            # Introduce race condition vulnerability
            data[i] = data[i] + random.randint(-10, 10) # adding random values to make it more complex

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(n)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return data

def test_jit_compiler():
    iterations = random.randint(100000, 2000000)
    a = 0
    for _ in range(iterations):
        a += 1
        # Introduce more complex control flow for JIT compilation
        if _ % 10000 == 0 and iterations > 500000 and random.random() > 0.5:
            a = a * 2  # Potentially affect JIT compilation

    if iterations > 500000:
        b = 10
    else:
        b = 20
    
    # Introduce a potentially JIT-compiled calculation
    c = 0
    for i in range(100):
      c = c + i * 2
      
    return a + b + c

def test_complex_annotations():
    Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
    MyDict = typing.Dict[Point, str]
    my_point = Point(1, 2)
    my_dict: MyDict = {my_point: "some data"}

    try:
      # Fuzzing complex type annotations - error cases.  This could fail
      my_dict[Point(3, 4)] = "error" 
      return my_dict
    except Exception as e:
      print(f"Error in complex annotations: {e}")
      return "Error"


def test_docstring_whitespace():
    """This is a docstring with inconsistent whitespace.
       With various formats to test parsing.
    """
    a = 1
    
    # Introduce varied docstrings for different testing purposes
    try:
      eval('a = 2\n\n# test\n\n')
      return a *2
    except Exception as e:
      print(f"Error in docstring eval: {e}")
      return "Error"

def test_dbm_sqlite():
  try:
    # Introduce a potential failure condition
    filename = 'test.dbm' + str(random.randint(0, 10000))

    db = dbm.open(filename, 'c')
    db['key'] = 'value'
    data = db['key']
    db.close()
    os.remove(filename) #Crucially, remove the created file.
  except Exception as e:
    print(f"Error in DBM operation: {e}")
    return "error"
  return data



if __name__ == "__main__":
    n = 10
    result = test_free_threading(n)
    print(f"Free-threading result: {result}")
    jit_result = test_jit_compiler()
    print(f"JIT compiler result: {jit_result}")
    annotations_result = test_complex_annotations()
    print(f"Complex annotations result: {annotations_result}")
    docstring_result = test_docstring_whitespace()
    print(f"Docstring whitespace result: {docstring_result}")
    dbm_result = test_dbm_sqlite()
    print(f"DBM sqlite3 result: {dbm_result}")

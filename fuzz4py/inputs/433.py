
import threading
import time
import os
import copy
import ssl
import sqlite3
import typing

def worker(i):
    # Simulate work with race condition vulnerability
    global counter
    with lock:
        counter += i
        time.sleep(0.01)  # Introduce delay for potential race conditions


def test_race_condition():
    global counter
    counter = 0
    threads = []
    lock = threading.Lock()
    
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final Counter: {counter}")
    
# Test with JIT (Note: JIT is not guaranteed to be enabled)
def jit_test():
    result = 0
    for i in range(1000000):
        result += i
    print(f"Result from JIT test: {result}")


def test_copy_replace():
    class MyReplaceable(object):
        def __init__(self, x):
            self.x = x

        def __replace__(self, **changes):
            return MyReplaceable(changes.get("x", self.x))

    original = MyReplaceable(5)
    copied = copy.replace(original, x=10)
    print(f"Original: {original.x}, Copied: {copied.x}")

def test_dbm_sqlite3():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, data TEXT)")
        cursor.execute("INSERT INTO mytable (data) VALUES (?)", ('Hello',))
        conn.commit()

        cursor.execute("SELECT data FROM mytable")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        conn.close()
    except sqlite3.Error as e:
        print(f"Error in dbm.sqlite3 test: {e}")

def test_os_timer():
  #Example usage (not a complete test)
  start = time.perf_counter()
  time.sleep(1)
  end = time.perf_counter()
  print(f"Elapsed time: {end-start}")



# Test with annotations (complex annotation)
def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.List[str]:
  return [x[1] for x in data]



if __name__ == "__main__":
    test_race_condition()
    jit_test()
    test_copy_replace()
    test_dbm_sqlite3()
    test_os_timer()
    print(complex_annotation([(1, "a"), (2, "b")]))


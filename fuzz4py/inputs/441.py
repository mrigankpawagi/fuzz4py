
import threading
import time
import os
import copy
import sqlite3
import typing
import ssl
import unittest
import dbm
import random

# Global variable (for demonstration of race condition)
counter = 0


def worker(i):
    # Simulate work with race condition vulnerability
    global counter
    with threading.Lock():  # Explicit lock
        counter += i
        time.sleep(random.uniform(0.001, 0.01))  # Introduce random delay


def test_race_condition():
    global counter
    counter = 0
    threads = []
    lock = threading.Lock()  # Initialize lock here
    
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final Counter: {counter}")


def jit_target_function(input_list):
    """
    A function likely to be JIT compiled due to its repetitive nature.
    """
    total = 0
    for i in range(100000):
        try:
          total += input_list[i % len(input_list)]
        except IndexError as e:
          return f"IndexError occurred: {e}"  # Handle IndexError
    return total


def test_jit_compilation(input_list):
    """Test function to exercise JIT compiler."""
    return jit_target_function(input_list)

def test_copy_replace():
    class MyReplaceable:
        def __init__(self, x):
            self.x = x
            self.y = "initial"
        def __replace__(self, **changes):
            new_obj = copy.copy(self)
            for key, value in changes.items():
                setattr(new_obj, key, value)
            return new_obj

    original = MyReplaceable(5)
    copied = copy.replace(original, x=10,y="changed") #adding y attribute
    print(f"Original: {original.x}, Copied: {copied.x}, Copied y: {copied.y}")



def test_dbm_sqlite3():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # Insert varying data types
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, data TEXT, another_data INTEGER)")
        cursor.execute("INSERT INTO mytable (data, another_data) VALUES (?, ?)", ('Hello', 123))
        cursor.execute("INSERT INTO mytable (data, another_data) VALUES (?, ?)", ('World', 456))
        conn.commit()

        cursor.execute("SELECT * FROM mytable")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        conn.close()
    except sqlite3.Error as e:
        print(f"Error in dbm.sqlite3 test: {e}")


def test_os_timer():
    start = time.perf_counter()
    time.sleep(random.uniform(0.5, 1.5))  # Introduce random delay
    end = time.perf_counter()
    print(f"Elapsed time: {end-start}")



def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.List[str]:
  try:
    return [x[1] for x in data]
  except IndexError:
    return "IndexError"  # Handle potential index error

def my_complex_function(data: typing.List[int]) -> typing.List[int]:
    """
    A complex function demonstrating various features in Python 3.13.
    """
    if not data:
        return []

    threads = []
    lock = threading.Lock()
    global counter

    for i in data:
        t = threading.Thread(target=process_element, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    try:
      return data
    except Exception as e:
      print(f"Exception in my_complex_function: {e}")
      return None



def process_element(element):
    try:
        time.sleep(0.1)
    except Exception as e:
        print(f"Exception in process_element: {e}")
        return None
    return element



def fuzz_input():
    #Fuzz with different inputs, including empty lists and None
    choice = random.choice([list(range(10)), [], None])
    if choice is None:
      return None
    return choice


class ReplaceableClass:
    # ... (same as before)


class Meta(type):
    # ... (same as before)

class MyClass(metaclass=Meta):
    pass


class TestFreeThreading(unittest.TestCase):
    def test_thread_race(self):
        shared_data = [0]
        lock = threading.Lock()

        def worker():
            with lock:
                global shared_data
                shared_data[0] += 1

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(shared_data[0], 10)

if __name__ == '__main__':
    test_race_condition()
    input_list = list(range(random.randint(1000,150000)))  # Example list, larger range
    output = test_jit_compilation(input_list)
    print(output)
    test_copy_replace()
    test_dbm_sqlite3()
    test_os_timer()
    data = fuzz_input()
    if data:
      print(complex_annotation([(1, "a"), (2, "b")]))
      result = my_complex_function(data)
      if result:
          print("Complex function returned:", result)
    replaced = ReplaceableClass(10)
    replaced = replaced.__replace__(20)

    try:
        print("Value:", MyClass.__static_attributes__['value'])
    except Exception as e:
        print("Error accessing static attribute:", e)


    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"SSL error: {e}")

    try:
        db = dbm.open('test_db', 'c')
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Error accessing dbm: {e}")

    try:
      start_time = time.time()
      result = os.times()
      end_time = time.time()
      print(f"Time taken: {end_time - start_time}")
    except Exception as e:
      print(f"Error with os.times(): {e}")


    # Example using unittest (for testing free-threading)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

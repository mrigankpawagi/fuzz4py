
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
        if random.random() < 0.1: # Introduce occasional exception
          raise ValueError("Simulated exception")


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
        try:
          thread.join()
        except Exception as e:
            print(f"Thread {i} raised exception: {e}")
            
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
    if not input_list:
        return "Empty list"
    return jit_target_function(input_list)


def test_copy_replace():
    class MyReplaceable:
        def __init__(self, x, y="initial"): #added y
            self.x = x
            self.y = y
        def __replace__(self, **changes):
            new_obj = copy.copy(self)
            for key, value in changes.items():
                setattr(new_obj, key, value)
            return new_obj

    original = MyReplaceable(5)
    try:
      copied = copy.replace(original, x=10, y="changed") #adding y attribute
      print(f"Original: {original.x}, Copied: {copied.x}, Copied y: {copied.y}")
    except Exception as e:
        print(f"Error in test_copy_replace: {e}")


def test_dbm_sqlite3():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, data TEXT, another_data INTEGER)")
        for i in range(10):
          cursor.execute("INSERT INTO mytable (data, another_data) VALUES (?, ?)", (str(i), i*10))
        conn.commit()
        conn.close()
        print("dbm.sqlite3 test successful.")
    except sqlite3.Error as e:
        print(f"Error in dbm.sqlite3 test: {e}")



def test_os_timer():
    start = time.perf_counter()
    time.sleep(random.uniform(0.5, 1.5))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start}")



def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.List[str]:
  try:
    return [x[1] for x in data]
  except IndexError:
    return "IndexError"  # Handle potential index error
  except TypeError as e: #Catch invalid type
    return f"TypeError: {e}"


def my_complex_function(data: typing.List[int]) -> typing.List[int]:
    # ... (rest of the code is the same)



def fuzz_input():
    choice = random.choice([list(range(10)), [], None, [1, 2, 3, "a"], [1,2,None]])
    return choice


class ReplaceableClass:
  def __init__(self, x):
    self.x = x

  def __replace__(self, **changes):
    new_obj = copy.copy(self)
    for key, value in changes.items():
      setattr(new_obj, key, value)
    return new_obj


class Meta(type):
    __static_attributes__ = {"value": 42}

class MyClass(metaclass=Meta):
    pass


class TestFreeThreading(unittest.TestCase):
    # ... (rest of the code is the same)

if __name__ == '__main__':
    test_race_condition()
    input_list = list(range(random.randint(1000, 150000)))
    output = test_jit_compilation(input_list)
    print(output)
    test_copy_replace()
    test_dbm_sqlite3()
    test_os_timer()
    data = fuzz_input()

    #Added null checks
    if data is not None:
        print(complex_annotation([(1, "a"), (2, "b")]))
        result = my_complex_function(data)
        if result:
            print("Complex function returned:", result)
    # ... (rest of the code is the same)

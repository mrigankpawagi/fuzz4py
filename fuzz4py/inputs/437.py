
import threading
import time
import os
import copy
import sqlite3
import typing
import ssl
import unittest
import dbm

# Global variable (for demonstration of race condition)
counter = 0


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
    global lock
    lock = threading.Lock()
    
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
        total += input_list[i % len(input_list)]
    return total

def test_jit_compilation(input_list):
    """Test function to exercise JIT compiler."""
    try:
      result = jit_target_function(input_list)
      return result
    except IndexError as e:
      return "IndexError occurred: " + str(e)

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



def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.List[str]:
  return [x[1] for x in data]


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

    return data



def process_element(element):
    try:
        time.sleep(0.1)
    except Exception as e:
        print(f"Exception in process_element: {e}")
        return None

    return element



def fuzz_input():
    return [i for i in range(10)]


def docstring_test():
    """Example docstring with varying whitespace"""
    pass

class ReplaceableClass:
    def __init__(self, value):
        self.value = value

    def __replace__(self, value=None):
        if value is not None:
            return ReplaceableClass(value)
        else:
            return self

    def __str__(self):
       return str(self.value)


class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['__static_attributes__'] = {'value': 10}
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=Meta):
    pass


class MyCustomClass:
    def __init__(self, data):
        self.data = data

    def __replace__(self, data=None):
        return MyCustomClass(data or self.data)

    def __repr__(self):
        return f"MyCustomClass({self.data})"



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

    # Example usage of jit_target_function
    input_list = list(range(150000))
    output = test_jit_compilation(input_list)
    print(output)


    # Example of __replace__ usage
    custom_obj = MyCustomClass(42)
    replaced_obj = copy.replace(custom_obj, 10)
    print(f"Original: {custom_obj}")
    print(f"Replaced: {replaced_obj}")

    test_copy_replace()

    test_dbm_sqlite3()
    test_os_timer()
    print(complex_annotation([(1, "a"), (2, "b")]))
    data = fuzz_input()
    result = my_complex_function(data)
    if result:
        print("Complex function returned:", result)

    replaced = ReplaceableClass(10)
    replaced = replaced.__replace__(20)


    try:
        print("Value:", MyClass.__static_attributes__['value'])
    except Exception as e:
        print("Error accessing static attribute:", e)
    
    #Example for SSL connections (simplified, expand if needed)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"SSL error: {e}")

    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Error accessing dbm: {e}")

    # Example of os timer function (replace with a more complex test if needed)
    start_time = time.time()
    result = os.times()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")



    # Example using unittest (for testing free-threading)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



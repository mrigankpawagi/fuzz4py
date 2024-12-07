
import threading
import time
import os
import copy
import sqlite3
import typing
import ssl


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


if __name__ == "__main__":
    test_race_condition()
    jit_test()
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
    
    context = ssl.create_default_context()

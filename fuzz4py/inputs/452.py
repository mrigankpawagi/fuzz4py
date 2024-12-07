
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
    global counter
    lock = threading.Lock()
    with lock:  # Explicit lock
        try:
            counter += i
            time.sleep(random.uniform(0.001, 0.01))  # Introduce random delay
            if random.random() < 0.1:  # Introduce occasional exception
                raise ValueError("Simulated exception")
            if i % 5 == 0:
                raise ZeroDivisionError("Intentional Error")
            if i % 7 == 0:
                raise TypeError("Intentional TypeError")
            if i % 11 == 0:
                raise AttributeError("Intentional AttributeError")
        except Exception as e:
            print(f"Worker {i} raised exception: {e}")


def test_race_condition():
    global counter
    counter = 0
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Final Counter: {counter}")


def jit_target_function(input_list):
    if not input_list:
        return "Empty list"  # Handle empty list
    total = 0
    for i in range(100000):
        try:
            total += input_list[i % len(input_list)]
        except IndexError:
            return "IndexError: list index out of range"
        except Exception as e:
            return f"Exception in loop: {type(e).__name__}-{e}"
    return total


def test_jit_compilation(input_list):
    if not input_list:
        return "Empty list"
    try:
        return jit_target_function(input_list)
    except TypeError as e:
        return f"TypeError: {e}"
    except Exception as e:
        return f"Unexpected Exception: {type(e).__name__}-{e}"


def test_copy_replace():
    class MyReplaceable:
        def __init__(self, x, y="initial"):
            self.x = x
            self.y = y
        def __replace__(self, **changes):
            new_obj = copy.copy(self)
            for key, value in changes.items():
                try:
                    setattr(new_obj, key, value)
                except AttributeError as e:
                    print(f"AttributeError setting {key}: {e}")
                    return None
            return new_obj

    original = MyReplaceable(5)
    copied = original.__replace__(x=10, y="changed")
    if copied:
        print(f"Original: {original.x}, Copied: {copied.x}, Copied y: {copied.y}")
    else:
        print("Error replacing attribute.")


def test_dbm_sqlite3():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, data TEXT, another_data INTEGER)")
        for i in range(10):
            cursor.execute("INSERT INTO mytable (data, another_data) VALUES (?, ?)", (str(i), i * 10))
        conn.commit()
        conn.close()
        print("dbm.sqlite3 test successful.")
    except sqlite3.Error as e:
        print(f"Error in dbm.sqlite3 test: {e}")


def test_os_timer():
    start = time.perf_counter()
    time.sleep(random.uniform(0.5, 1.5))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.4f} seconds")


def complex_annotation(data: typing.List[typing.Tuple[int, str]]) -> typing.List[str]:
    if data is None:
        return "Input is None"
    try:
        return [x[1] for x in data]
    except (IndexError, TypeError) as e:
        return f"Error: {type(e).__name__} - {e}"


def my_complex_function(data: typing.List[int]) -> typing.List[int]:
    if data is None:
        return []
    return [x * 2 for x in data]


def fuzz_input():
    choices = [list(range(10)), [], None, [1, 2, 3, "a"], [1, 2, None], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, "a", 5.5]]
    return random.choice(choices)


if __name__ == '__main__':
    test_race_condition()
    input_list = list(range(random.randint(10, 150000)))
    output = test_jit_compilation(input_list)
    print(output)
    test_copy_replace()
    test_dbm_sqlite3()
    test_os_timer()
    data = fuzz_input()
    if data is not None:
        result = complex_annotation([(1, "a"), (2, "b")])
        print(result)
        if isinstance(data, list):
            processed_data = my_complex_function(data)
            if processed_data:
                print("Complex function returned:", processed_data)

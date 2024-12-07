
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing
import random

def worker(data: list[int], index: int, lock: threading.Lock):
    try:
        lock.acquire()
        if index + 1 < len(data):
            data[index + 1] += 1
        lock.release()
    except IndexError:
        print("IndexError caught in worker thread")
    except Exception as e:
        print(f"Worker thread {index} failed: {e}")

def main():
    data = [0] * 10
    lock = threading.Lock()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(data, i, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(data)


    class Point:
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y
        def __replace__(self,  x : int = None, y : int = None):
            return copy.copy(self) if x is None and y is None else copy.copy(self)

    p1 = Point(1, 2)
    p2 = Point(10,2)
    p1 = copy.copy(p1)
    p1 = copy.copy(p1)

    print(p1.x, p1.y)
    print(p2.x, p2.y)
    
    # Fuzzing replace protocol with various inputs
    p3 = Point(3, 4)
    p4 = fuzz_replace_protocol(p3)
    print(f"p4: {p4}")
    p5 = Point("a", "b")
    p6 = fuzz_replace_protocol(p5)
    print(f"p6: {p6}")
    p7 = fuzz_replace_protocol(None)
    print(f"p7: {p7}")
    p8 = fuzz_replace_protocol(123)
    print(f"p8: {p8}") # Fuzzing with integer


    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(value)
        db['key2'] = b'binary_value'
        value_binary = db['key2']
        print(value_binary)
        # Fuzzing with malformed data (added more variations)
        for i in range(10):
            try:
                db[f"key{i+3}"] = str(i)
            except Exception as e:
                print(f"Error setting key {i+3}: {e}")

        db['key10'] = b'\x00\x01' # Malformed binary data
        db['key11'] = [1, 2, 3]  # List as a value
        db['key12'] = {'a': 1}  # Dict as a value
        db['key13'] = 123.456  # Float
        db['key14'] = 10000000000  # Large integer
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    finally:
        if 'db' in locals() and isinstance(db, dbm.sqlite3.DB):
            db.close()


def worker(data: list[int], lock: threading.Lock, db: dbm.sqlite3):
    for i in data:
        lock.acquire()
        try:
            db[str(i)] = str(i * 2)
            result = os.times()
            print(f"Thread time result: {result}")
            db[str(i)] = str(i)
        finally:
            lock.release()
    return 1


def main_second():
    data = list(range(10))
    lock = threading.Lock()
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
    except Exception as e:
        print(f"Error opening database: {e}")
        return

    threads = []
    for i in range(5):
        thread_data = data[:]  # Correctly creates a copy
        thread_data.append("string")
        thread_data.append(12.34)
        thread_data.append(True)
        thread_data.append(None)
        thread_data.append(1j)
        thread_data.append(float('inf'))
        thread_data.append(float('-inf'))
        thread_data.append(b"bytes")
        thread_data.append(object())
        thread_data.append(lambda: print("Lambda function"))

        thread = threading.Thread(target=worker, args=(thread_data, lock, db))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    try:
        db.close()
    except Exception as e:
        print(f"Error closing database: {e}")

def fuzz_replace_protocol(data):
    try:
        return copy.copy(data)
    except Exception as e:
        print(f"Error replacing data: {e}")
        return None

if __name__ == "__main__":
    main()
    main_second()

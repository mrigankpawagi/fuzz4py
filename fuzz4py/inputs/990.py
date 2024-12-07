
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

        def __copy__(self):
            return Point(self.x, self.y)


    p1 = Point(1, 2)
    p2 = Point(10, 2)
    p1 = copy.copy(p1)
    p1 = copy.copy(p1)

    print(p1.x, p1.y)
    print(p2.x, p2.y)
    
    # Fuzzing replace protocol with various inputs
    def fuzz_replace_protocol(data):
        try:
            return copy.copy(data)
        except Exception as e:
            print(f"Error replacing data: {e}")
            return None

    p3 = Point(3, 4)
    p4 = fuzz_replace_protocol(p3)
    print(f"p4: {p4}")
    p5 = Point("a", "b")
    p6 = fuzz_replace_protocol(p5)
    print(f"p6: {p6}")
    p7 = fuzz_replace_protocol(None)
    print(f"p7: {p7}")
    p8 = fuzz_replace_protocol(123)
    print(f"p8: {p8}")  # Fuzzing with integer


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

        db['key10'] = b'\x00\x01'  # Malformed binary data
        db['key11'] = [1, 2, 3]  # List as a value
        db['key12'] = {'a': 1}  # Dict as a value
        db['key13'] = 123.456  # Float
        db['key14'] = 10000000000  # Large integer
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    finally:
        if 'db' in locals() and isinstance(db, dbm.sqlite3.DB):
            db.close()


def worker(data: list, lock: threading.Lock, db: dbm.sqlite3):
    for item in data:
        try:
            lock.acquire()
            db[str(item)] = str(item * 2)
            result = os.times()
            print(f"Thread time result: {result}")
            db[str(item)] = str(item)
            lock.release()
        except Exception as e:
            print(f"Error in worker thread: {e}")
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
        thread_data = data[:]
        # Adding various data types to the thread data
        thread_data.extend(["string", 12.34, True, None, 1j, float('inf'), float('-inf'), b"bytes", object(), lambda: print("Lambda function")])
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


if __name__ == "__main__":
    main()
    main_second()

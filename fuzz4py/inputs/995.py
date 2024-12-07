
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing
import random

def worker(data, index, lock):
    try:
        lock.acquire()
        if index + 1 < len(data):
            try:
                data[index + 1] += random.randint(-10, 10)
            except TypeError as te:
                print(f"TypeError in worker thread: {te}")

        lock.release()
    except IndexError:
        print("IndexError caught in worker thread")
    except Exception as e:
        print(f"Worker thread {index} failed: {e}")
        raise  # Re-raise to propagate the error

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
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __copy__(self):
            return Point(self.x, self.y)

        def __replace__(self, x=None, y=None):
            if x is not None:
                try:
                    self.x = int(x)  #Added type checking
                except ValueError as e:
                    print(f"Error converting x to int: {e}")
                    return self
            if y is not None:
                try:
                    self.y = int(y)
                except ValueError as e:
                    print(f"Error converting y to int: {e}")
                    return self
            return self

    p1 = Point(1, 2)
    p2 = Point(10, 2)
    p1 = copy.copy(p1)
    p1 = copy.copy(p1)
    p1 = copy.copy(p1)
    try:
        p1 = p1.__replace__(x=random.randint(1,100), y=random.randint(1,100))
    except TypeError as te:
        print(f"Error replacing p1: {te}")
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    
    def fuzz_replace_protocol(data):
        try:
            if isinstance(data, Point):
                return data.__replace__(x=random.randint(-100, 100), y=random.randint(-100, 100))
            elif isinstance(data, int) or isinstance(data, float):
                return data * 2  # Mutate numbers
            elif data is not None:
                return copy.copy(data)
            else:
                return None
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
    print(f"p8: {p8}")
    p9 = fuzz_replace_protocol("string")
    print(f"p9: {p9}")
    p10 = fuzz_replace_protocol(123.456)
    print(f"p10: {p10}")
    
    # Added error handling for non-dbm.sqlite3 type
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(value)
        db['key2'] = b'binary_value'
        value_binary = db['key2']
        print(value_binary)
        for i in range(10):
            try:
                db[f"key{i+3}"] = str(random.random())
            except Exception as e:
                print(f"Error setting key {i+3}: {e}")

        db['key10'] = b'\x00\x01'
        db['key11'] = [1, 2, 3]
        db['key12'] = {'a': 1}
        db['key13'] = 123.456
        db['key14'] = 10000000000
        db['key15'] = b"very long string that might be too long for the database"
        db['key16'] = b"\x00\x01" * 1000
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    finally:
        if 'db' in locals() and isinstance(db, dbm.sqlite3.DB):
            db.close()


def worker(data, lock, db):
    for item in data:
        try:
            lock.acquire()
            db[str(item)] = str(item * 2)
            result = os.times()  # Get time result
            print(f"Thread time result: {result}")
            db[str(item)] = str(item)
            lock.release()
        except Exception as e:
            print(f"Error in worker thread: {e}")
            raise  #Re-raise to propagate


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
        thread_data.extend(["string", 12.34, True, None, 1j, float('inf'), float('-inf'), b"bytes", object(), lambda: print("Lambda function"), "verylongstring", b'\x00'*1000, 123.4567])  #Added more diverse types
        thread = threading.Thread(target=worker, args=(thread_data, lock, db))
        threads.append(thread)
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

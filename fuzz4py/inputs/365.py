
import threading
import time
import copy
import dbm
import os
import ssl
import typing

# Fuzzing multi-threading with GIL
def worker(lock, data):
    with lock:
        try:
            data.append(1)
            time.sleep(0.001)  # Introduce some delay for potential race condition
            data.pop()
        except Exception as e:
            print(f"Error in worker thread: {e}")


def main():
    data = []
    lock = threading.Lock()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(lock, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data: {data}")

# Fuzzing copy.replace()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)


def copy_replace_fuzz():
    p1 = Point(10, 20)
    p2 = p1.__replace__(x=30)
    print(f"p1: {p1.x}, {p1.y}")
    print(f"p2: {p2.x}, {p2.y}")

#Fuzzing docstring whitespace
def indented_docstring():
    """
    This docstring
      has some
        indentation.
    """
    pass

# Fuzzing dbm.sqlite3
try:
    db = dbm.open('test.db', 'c')
    db['key1'] = 'value1'
    db.close()
    db = dbm.open('test.db', 'r')
    print(db['key1'])
    db.close()
    os.remove('test.db')
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")



if __name__ == "__main__":
    main()
    copy_replace_fuzz()
    indented_docstring()

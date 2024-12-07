
import threading
import time
import copy
import dbm
import os
import ssl
import socket
import typing
import random

def worker(data: typing.List[int], index: int, lock):
    try:
        lock.acquire()
        data[index] += 1
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
            return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)

    p1 = Point(1, 2)
    p2 = copy.replace(p1, x=10)
    print(p1.x, p1.y)
    print(p2.x, p2.y)


    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(value)
        db['key2'] = b'binary_value'
        value_binary = db['key2']
        print(value_binary)
    except Exception as e:
        print(f"Error interacting with dbm.sqlite3: {e}")
    finally:
        if 'db' in locals() and isinstance(db, dbm.sqlite3.DB):
            db.close()


def worker(data: typing.List[int], lock: threading.Lock, db: dbm.sqlite3):
    for i in data:
        lock.acquire()
        try:
            db[str(i)] = str(i * 2)
            os.times()
            db[str(i)] = i
        finally:
            lock.release()
    assert isinstance(data, typing.List[int])
    return 1


def main_second():
    data = list(range(10))
    try:
        db = dbm.sqlite3.open('mydatabase', 'c')
    except Exception as e:
        print(f"Error opening database: {e}")
        return

    threads = []
    for i in range(5):
        thread_data = copy.deepcopy(data)
        thread_data.append("string")
        thread_data.append(12.34)
        thread_data.append(True)
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


def jit_target_function(input_list):
    result = 0
    for i in input_list:
        result += i
    return result


def threaded_function(input_data, thread_id):
    result = jit_target_function(input_data)
    time.sleep(0.01)
    print(f"Thread {thread_id}: Result {result}")
    return result


def fuzz_replace_protocol(data):
    try:
        return copy.replace(data, x=None, y=None)
    except Exception as e:
        print(f"Error replacing data: {e}")
        return None


try:
    context = ssl.create_default_context()
    for hostname in [None, "", "invalid.hostname"]:
      with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
          try:
              s.connect(('example.com', 443))
              s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
              response = s.recv(4096)
              print(response.decode())
          except Exception as e:
              print(f"Error with ssl connection for hostname {hostname}:", e)
except Exception as e:
    print("Error with ssl connection:", e)


try:
    start_time = time.perf_counter()
    result = os.times()
    end_time = time.perf_counter()
    print(result)
    result = os.times("invalid_arg")  # Added invalid arg case
except Exception as e:
    print(f"Error with os timer: {e}")


def func(arg: typing.List[int]) -> int:
    return sum(arg)

def my_function(data: typing.List):
    try:
        db = dbm.open('mydatabase', 'c')
        result = 0
        for item in data:
            result += item
        return result
    except (TypeError, ValueError, dbm.error) as e:
        print(f"An error occurred: {e}")
        return -1


def my_function2(data: list):
    try:
        db = dbm.open('mydatabase', 'c')  # Open dbm
        result = 0
        for item in data:
            result += item
        return result
    except (TypeError, ValueError, dbm.error) as e:
        print(f"An error occurred: {e}")
        return -1



def main_third():
    data_types = [list(range(10)), [1, 2, 3, 'a'], [], [0]*100000 ,  [random.random()*100 for _ in range(100)], None, [1,2,3,4,None], [None]*10]
    for data in data_types:
        start_time = time.time()
        result = my_function(data)
        end_time = time.time()
        print(f"Result for input {data}: {result}, time taken: {end_time-start_time}")
        start_time = time.time()
        result = my_function2(data)
        end_time = time.time()
        print(f"Result for input {data}: {result}, time taken: {end_time-start_time}")


if __name__ == "__main__":
    main()
    main_second()
    main_third()

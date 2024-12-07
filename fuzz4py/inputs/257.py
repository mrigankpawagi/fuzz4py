
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket


def jit_target_function(input_list: typing.List[int]) -> int:
    """
    A function designed to be JIT compiled and targeted for fuzzing.
    """
    total = 0
    for i in input_list:
        total += i
    return total


def test_replace_protocol():
    """Testing copy.replace() and replace protocol."""
    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, a=None, b=None):
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    obj = MyClass(1, 2)
    new_obj = copy.replace(obj, a=3)
    return new_obj.a


def test_dbm_sqlite():
  """Testing dbm.sqlite3"""
  try:
    db = dbm.open('test.db', 'c')
    db['key1'] = b'value1'
    db['key2'] = b'value2'
    data = db['key1']
    db.close()
    os.remove('test.db')  # Clean up the temporary file
    return data
  except Exception as e:
    return str(e)


def test_os_timer():
    """Testing os module timer functions."""
    try:
      start_time = time.perf_counter()  # Use perf_counter for better accuracy
      result = os.times()
      end_time = time.perf_counter()  # Use perf_counter for better accuracy
      return (result, end_time - start_time)
    except Exception as e:
      return str(e)


def test_ssl_context():
    """Testing ssl.create_default_context() changes."""
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return "Connection success"
    except Exception as e:
        return str(e)


def worker(data, lock):
    # Simulate some work that could be JIT-compiled
    result = sum(data)
    with lock:
        print(f"Thread {threading.get_ident()} result: {result}")
    time.sleep(0.1)


def main():
    # Multi-threaded test (using worker function for better organization)
    data = list(range(10000))
    lock = threading.Lock()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Example using dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()

        db = dbm.open('mydatabase', 'r')
        print(f"Retrieved key: {db['key1']}")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


    # Example using ssl (with explicit port and error handling)
    try:
        context = ssl.create_default_context()
        # Replace with a valid certificate path for testing purposes
        with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
            s.connect(('localhost', 443))  # Replace with appropriate port
            print("SSL connection successful.")
    except ssl.SSLError as e:
        print(f"SSL connection error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    # Example usage of the other functions (now separated)
    results = jit_target_function([1, 2, 3, 4])
    new_obj_replace = test_replace_protocol()
    db_test = test_dbm_sqlite()
    os_timer_result = test_os_timer()
    ssl_test = test_ssl_context()

    print(f"JIT result: {results}")
    print(f"Replace protocol result: {new_obj_replace}")
    print(f"dbm.sqlite3 result: {db_test}")
    print(f"os timer result: {os_timer_result}")
    print(f"SSL context result: {ssl_test}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()


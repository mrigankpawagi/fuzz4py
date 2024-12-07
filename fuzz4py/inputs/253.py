
import threading
import time
import copy
import dbm
import os
import ssl
import typing

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
            
    obj = MyClass(1,2)
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
    return data
  except Exception as e:
    return str(e)

def test_os_timer():
    """Testing os module timer functions."""
    try:
      start_time = time.time()
      result = os.times()
      end_time = time.time()
      return (result, end_time-start_time)
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


def threaded_function(input_val):
  """Illustrative function for free-threading testing."""
  try:
    time.sleep(0.01)
    return input_val * 2
  except Exception as e:
    return str(e)



def main():
    # Multi-threaded test
    threads = []
    for i in range(5):
      x = threading.Thread(target=threaded_function, args=(i,))
      threads.append(x)
      x.start()

    for thread in threads:
        thread.join()



    # Example usage of the functions
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
    main()

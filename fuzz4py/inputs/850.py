
import threading
import time
import copy
import os
import ssl
import typing
import random
import dbm
import sys

def my_function(arg1: int, arg2: str, arg3: typing.List[int] = None) -> str:
    """
    This function demonstrates a complex type annotation and free-threading.
    """
    if arg3 is None:
        arg3 = []  # Initialize to avoid errors

    result = ""
    for i in range(len(arg3)):
        try:
            value = arg3[i] * arg1
            if abs(value) > 2**31:
              raise OverflowError("Integer overflow")
            result += str(value)
        except (Exception, OverflowError) as e:
            result += str(e)

    return result + arg2


def test_function():
    """Testing function with complex type annotations and threading."""

    my_list = [1, 2, 3]
    new_list = copy.copy(my_list)
    try:
        new_list.replace(random.randint(0, 10), random.randint(0, 100))
    except Exception as e:
        print(f"Error using replace: {e}")


    threads = []
    for i in range(random.randint(2, 10)):
        thread = threading.Thread(target=lambda: my_function(random.randint(-10, 10),
                                                        "hello" + str(random.randint(0, 100)),
                                                        [random.randint(-10, 10) for _ in range(random.randint(0, 5))]),
                                args=(random.randint(-10, 10), "hello" + str(random.randint(0, 100)), [random.randint(-10, 10) for _ in range(random.randint(0, 5))]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    try:
        for var_name in locals().keys():
          if var_name != 'threads':
            try:
              print(locals()[var_name])
            except Exception as e:
              print(f"Error accessing variable {var_name}: {e}")
    except KeyError as e:
        print(f"Error in the scope: {e}")


def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
          try:
            result.append(int(item))
          except ValueError:
            result.append(0)

    return result


def worker(data):
    try:
        time.sleep(1)
        result = process_data(data)
        print(f"Thread {threading.current_thread().name}: {result}")
    except Exception as e:
        print(f"Error in thread {threading.current_thread().name}: {e}")


if __name__ == "__main__":
    data_for_threads = [1, 2, '3', 'abc', 5,6] * 100

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data_for_threads,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        print(f"Retrieved value: {value}")
        db.close()
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")

    try:
        start_time = time.time()
        os.times()
        end_time = time.time()
        print(f"Time taken by os.times(): {end_time - start_time}")
    except Exception as e:
        print(f"Error with os.times(): {e}")


    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error with SSL: {e}")


    try:
      class ReplaceableObject:
          def __init__(self, value):
              self.value = value
          def __replace__(self, value):
              return ReplaceableObject(value)
      obj1 = ReplaceableObject(5)
      obj2 = copy.copy(obj1)

      obj1.value = 10
      print(obj1.value)
      print(obj2.value)
    except Exception as e:
      print(f"Error with copy.replace(): {e}")


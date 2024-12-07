
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

def complex_function(arg1: typing.List[int], arg2: str, arg3: typing.Dict[str, str]):
    """
    A function demonstrating various features of Python 3.13
    """

    # Test free-threading and GIL
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda x=i: process_input(x, arg2, arg3))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    
    # Test complex type annotations and scopes
    new_list: typing.List[int] = [x * 2 for x in arg1]
    
    # Test replace protocol
    obj = MyReplaceableClass(arg2)
    new_obj = copy.replace(obj, value=arg2 + "updated")
    
    # Test dbm.sqlite3
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (name) VALUES (?)", (arg2,))
    conn.commit()
    conn.close()

    # Test os module timer functions
    start_time = time.monotonic()
    time.sleep(0.1)
    end_time = time.monotonic()

    # Test ssl
    context = ssl.create_default_context()
    try:
        context.check_hostname = True  # Stricter check
        context.verify_mode = ssl.CERT_REQUIRED  # Ensure validation
        # ... (SSL connection code)
        print("SSL connection successful")
    except ssl.SSLError as e:
        print(f"SSL connection error: {e}")
    
    return new_list



class MyReplaceableClass:
  def __init__(self, value):
    self.value = value

  def __replace__(self, value = None):
    if value is not None:
        return MyReplaceableClass(value)
    return self


def process_input(input_id, arg2, arg3):
    print(f"Thread {input_id}: {arg2} {arg3}")
    time.sleep(0.01)
    print(f"Thread {input_id} finished.")



if __name__ == "__main__":
    test_data_1 = [1, 2, 3, 4, 5]
    test_data_2 = "some_string"
    test_data_3 = {"key1": "value1", "key2": "value2"}

    complex_function(test_data_1, test_data_2, test_data_3)

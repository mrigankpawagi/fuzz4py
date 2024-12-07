
import threading
import copy
import os
import ssl
import sqlite3
import typing

def race_condition_example(data: typing.List[int]) -> typing.List[int]:
    """
    Demonstrates a potential race condition if not thread-safe.
    """
    lock = threading.Lock()
    results = []

    def worker(item):
        with lock:
            results.append(item * 2)

    threads = []
    for item in data:
        thread = threading.Thread(target=worker, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def jit_test():
  """
  A simple function likely to be JIT compiled if run many times.
  """
  count = 0
  for i in range(10000000):
    count += i
  return count


def test_replace_protocol(obj):
    """
    Tests the copy.replace() protocol if implemented by an object.
    """
    try:
        return copy.replace(obj, new_attr=42)  # Try replacing an attribute if possible
    except AttributeError:
        return obj


def test_dbm():
    """Tests dbm.sqlite3 with various inputs."""
    db_name = 'test.db'

    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        # Attempt an operation with malformed input.
        cur.execute("INSERT INTO test_table VALUES(?)", (b'invalid data',))
        conn.commit()
    except Exception as e:
        print(f"Error in dbm test: {e}")
    finally:
        try:
            conn.close()
        except:
            pass



def main():
    # Test data for race condition
    test_data = [1, 2, 3, 4, 5]
    print(f"Race Condition Output: {race_condition_example(test_data)}")

    # Test JIT compilation
    jit_result = jit_test()
    print(f"JIT Result: {jit_result}")

    # Test replace protocol (replace needs to be added)
    class TestClass:
        def __init__(self, attr):
            self.attr = attr
        def __replace__(self, attr=None):
            return type(self)(attr or self.attr)
    try:
        test_class_replace = TestClass(10)
        replaced_obj = test_replace_protocol(test_class_replace)
        print(f"Replaced Object: {replaced_obj}")
    except Exception as e:
        print(f"Error in replacing object: {e}")


    try:
        test_dbm()
    except Exception as e:
        print(f"Error in DBM test: {e}")


if __name__ == "__main__":
    main()


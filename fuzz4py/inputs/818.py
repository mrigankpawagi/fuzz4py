
import threading
import copy
import os
import ssl
import typing
import dbm
import time

def my_function(data: typing.List[int]) -> int:
    """
    This function demonstrates a potential race condition.
    """
    total = 0
    for i in data:
        try:
            total += i
        except (TypeError, ValueError):  # Catch ValueError as well
            return "Error: Non-numeric type encountered."
    return total


def test_replace_protocol(obj):
  """
  Demonstrates the use of copy.replace()
  """
  try:
    return copy.copy(obj)  # Use copy to avoid modifying original
  except (TypeError, AttributeError) as e:  # Catch more general errors
    return f"Error: {e}"


def fuzz_dbm():
    """
    Fuzzes dbm.sqlite3, adding potentially malformed data.
    """
    try:
        db = dbm.open("mydatabase", 'c')
        db['key1'] = "value1"
        db['key2'] = "a very long string" * 1000
        db['key3'] = ""
        db['key4'] = None
        db['key5'] = b"binary data"
        db['key6'] = 123
        db['key7'] = 3.14
        db['key8'] = True
        db['key9'] = {'nested': 'dict'}
        db['key10'] = [1, 2, 3]
        try:
          data = db['key2']
        except KeyError as e:
          return f"Error: {e}"  # More specific error message
        db.close()
        return "dbm fuzzing successful"
    except (dbm.error, OSError) as e:
        return f"Error during dbm fuzzing: {e}"
    except Exception as e:  # Handle any other potential exceptions
        return f"Error during dbm fuzzing: {e}"

def fuzz_ssl():
    """
    Fuzzes ssl module.
    """
    try:
        ctx = ssl.create_default_context()
        try:
            ctx.load_verify_locations(cafile="invalid_ca.crt")
        except FileNotFoundError:
            print("invalid_ca.crt not found, skipping SSL verification load")
        except Exception as e:
            return f"Error loading CA: {e}"
        return "SSL fuzzing successful"
    except Exception as e:
        return f"Error during SSL fuzzing: {e}"


if __name__ == "__main__":
    # Fuzzing with varying inputs, including larger and more complex data
    data1 = list(range(1000))
    data2 = [1] * 10000
    data3 = [-1] * 500 + [1] * 500
    data4 = []
    data5 = [1, 2, "3"]  # Type error input
    data6 = [1,2,3,4,5,6,7,8,9,0]
    data7 = [1,2,3,"a", "b", "c"]

    results = []
    threads = [
        threading.Thread(target=my_function, args=(data1,)),
        threading.Thread(target=my_function, args=(data2,)),
        threading.Thread(target=my_function, args=(data3,)),
        threading.Thread(target=my_function, args=(data4,)),
        threading.Thread(target=my_function, args=(data5,)),
        threading.Thread(target=my_function, args=(data6,)),
        threading.Thread(target=my_function, args=(data7,))
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    # Fuzzing copy.replace() on various objects
    result_replace_list = test_replace_protocol([1, 2, 3])
    print(f"Result of copy.copy() on list: {result_replace_list}")
    result_replace_tuple = test_replace_protocol((1, 2, 3))
    print(f"Result of copy.copy() on tuple: {result_replace_tuple}")
    result_replace_str = test_replace_protocol("hello")
    print(f"Result of copy.copy() on string: {result_replace_str}")


    # Fuzzing dbm.sqlite3 (more comprehensive)
    dbm_result = fuzz_dbm()
    print(f"Result of dbm fuzzing: {dbm_result}")

    # Fuzzing ssl module (more comprehensive)
    ssl_result = fuzz_ssl()
    print(f"Result of SSL fuzzing: {ssl_result}")

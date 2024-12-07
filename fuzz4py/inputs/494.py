
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def my_function(arg1: typing.List[int], arg2: int = 10) -> typing.Tuple[int, str]:
    """
    This function demonstrates various Python 3.13 features.
    """
    result = 0
    for i in arg1:
        result += i
    
    # Using copy.replace() to modify a list.  This could cause unintended changes if not handled correctly.
    my_list = copy.copy(arg1)
    my_list.append(arg2)
    try:
        replaced_list = copy.replace(my_list, arg1)
    except Exception as e:
        return result, str(e)

    # Test dbm.sqlite3
    try:
        with dbm.open('test.dbm', 'c') as db:
            db['key1'] = str(result)
    except Exception as e:
        return result, str(e)


    # Example of a potentially JIT-compiled hot loop
    for i in range(1000000):
        if i % 10 == 0:
            result += i

    
    # Test new ssl context
    try:
      ctx = ssl.create_default_context()
      # Replace with your actual certificate and key handling
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE
    except Exception as e:
      return result, str(e)

    return result, "Success"



# Demonstrate free-threading, potentially encountering race conditions.
def threaded_function(data: typing.List[int], thread_id: int):
  global shared_result #This demonstrates shared resource potential conflicts
  try:
    shared_result = my_function(data)[0] + shared_result
  except Exception as e:
    pass

if __name__ == "__main__":
    shared_result = 0
    data = [1, 2, 3, 4, 5]
    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(data, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    print(f"Final Result: {shared_result}")


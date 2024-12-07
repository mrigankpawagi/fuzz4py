
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def jit_sensitive_function(input_list):
    """
    A function that potentially triggers JIT compilation.
    """
    result = 0
    for _ in range(10000):
        result += sum(input_list)
    return result


def multithreaded_function(data: typing.List[int]) -> typing.List[int]:
  """
  Illustrates free-threading and the GIL.
  """

  def worker(index: int, data: typing.List[int]) -> int:
      return data[index] * 2

  threads = []
  results = []

  for i in range(len(data)):
      thread = threading.Thread(target=worker, args=(i, data))
      threads.append(thread)
      thread.start()

  for thread in threads:
      thread.join()  

  return results

def test_replace():
  class MyClass:
    def __init__(self, val):
        self.val = val

    def __replace__(self, val):
        return MyClass(val)

  obj = MyClass(10)
  new_obj = copy.replace(obj, val=20)
  return new_obj.val


def test_dbm():
  try:
      db = dbm.open('test.db', 'c')
      db['key1'] = 'value1'
      db.close()
      db = dbm.open('test.db', 'r')
      value = db['key1']
      db.close()
      os.remove('test.db')
      return value
  except Exception as e:
      return str(e)

def test_ssl():
    context = ssl.create_default_context()
    try:
      context.check_hostname = False
      context.verify_mode = ssl.CERT_NONE

      # Simulate a connection
      return "SSL connection successful"
    except Exception as e:
      return str(e)



if __name__ == "__main__":
    try:
        # Example usage:
        data = list(range(10))
        result = multithreaded_function(data)
        print(result)


        jit_result = jit_sensitive_function([1,2,3,4,5])
        print(jit_result)

        replacement_result = test_replace()
        print(replacement_result)

        dbm_result = test_dbm()
        print(dbm_result)

        ssl_result = test_ssl()
        print(ssl_result)

    except Exception as e:
        print(f"An error occurred: {e}")

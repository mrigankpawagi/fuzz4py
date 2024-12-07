
import threading
import copy
import dbm
import os
import ssl
import typing
import time
import random

# Fuzzing with free-threading (PEP 703)
def worker(lock, data, delay, extra_arg):
    with lock:
        time.sleep(delay)
        try:
            data.append(random.randint(1, 100) + extra_arg)
        except TypeError:
            pass # Handle potential TypeError

def free_threading_test():
    data = []
    lock = threading.Lock()
    threads = []
    delays = [random.random() for _ in range(10)]
    extra_args = [i for i in range(10)] # Add extra argument
    for i, delay in enumerate(delays):
        try:
            thread = threading.Thread(target=worker, args=(lock, data, delay, extra_args[i]))
            threads.append(thread)
            thread.start()
        except Exception as e:
            print(f"Error creating thread: {e}")
    for thread in threads:
        thread.join()
    return data


# Fuzzing JIT compiler (PEP 744) -  simple hot loop
def jit_loop(n, multiplier, bad_input):
    result = 0
    for i in range(n):
        try:
            result += i * multiplier + bad_input
        except TypeError:
            pass
    return result


# Fuzzing docstring whitespace stripping (Language)
def my_function(param1, extra_whitespace):
    """This function does something.
        With some extra whitespace.
        """
    try:
        return param1 + 1 + extra_whitespace
    except TypeError:
        return None


# Fuzzing annotation scopes (Language)
def annotated_function(data: typing.List[int] | typing.Dict[str, float] | str | int | object) -> str:  # Added object
  if isinstance(data, list):
    return str(sum(data))
  elif isinstance(data, dict):
    return str(sum(data.values()))
  elif isinstance(data, str):
    return data
  elif isinstance(data, int):
    return str(data)
  else:
    try:
      return str(data)
    except Exception as e:
        return str(e)  # Handle exceptions


# Fuzzing copy.replace (Standard Library) - Custom class
class MyData:
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

  def __replace__(self, value1=None, value2=None):
      try:
          value1 = int(value1) if value1 is not None else self.value1
          value2 = int(value2) if value2 is not None else self.value2
          return MyData(value1, value2)
      except (ValueError, TypeError):
          return None


  def __str__(self):
      return f"MyData(value1={self.value1}, value2={self.value2})"


# Fuzzing dbm.sqlite3 (Standard Library)
def dbm_test():
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db['key2'] = 'value2'
        db[b'key3'] = b'\x00\x01\x02'  # Use bytes for key
        db.close()
        print("dbm test successful")
    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")


# Fuzzing os module timer functions (Standard Library)
def os_timer_test():
    try:
        start_time = time.perf_counter()
        time.sleep(random.uniform(-10, 10)) # wider range
        end_time = time.perf_counter()
        print(f"Elapsed time: {end_time - start_time}")
    except Exception as e:
        print(f"Error with os timer functions: {e}")


# Fuzzing ssl (Standard Library)
def ssl_test():
  # ... (previous code)


def process_element(element, context):
  try:
      key = str(element)
      context[key] = str(element * 2)
      time.sleep(random.uniform(0.05, 0.15))  # Vary sleep time
  except Exception as e:
      print(f"Error processing element: {e}")


def multithreaded_function(data, context):
    threads = []
    for i in data:
        try:
            t = threading.Thread(target=process_element, args=(i, context))
            threads.append(t)
            t.start()
        except Exception as e:
            print(f"Error starting thread: {e}")
    for t in threads:
        t.join()
    return 0


def jit_test_function(data):
    try:
        total = 0
        for i in data:
            total += i
        return total
    except TypeError:
        return None


def main():
    dbm_test()
    os_timer_test()
    ssl_test()

    try:
        # ... (other functions)
        context = dbm.sqlite3.open('test_db', 'c')
        data = [1, 2, 3, 4, "five", 6.7] # Added more types
        result = multithreaded_function(data, context)
        print(f"Result of multithreaded function: {result}")


        # ... (other parts)
    except Exception as e:
        print(f"Error during database or JIT operations: {e}")


    try:
        orig_obj = {"a": 1, "b": 2}
        new_obj = copy.replace(orig_obj, a=3) #Try replacing a with a string
        print(f"Original: {orig_obj}, New: {new_obj}")
    except Exception as e:
        print(f"Error in copy.replace: {e}")




    # ... (rest of the code)



if __name__ == "__main__":
    main()

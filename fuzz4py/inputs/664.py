
import threading
import copy
import os
import time
import ssl
import dbm
import typing

def complex_function(arg1: typing.List[int], arg2: typing.Dict[str, str]) -> str:
    """
    A complex function demonstrating different features
    """
    # Use of free-threading
    thread_local_var = 0

    def inner_function(arg: int):
        nonlocal thread_local_var
        thread_local_var += arg
        time.sleep(0.01)

    threads = []
    for i in arg1:
        t = threading.Thread(target=inner_function, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
      

    # Use of copy.replace()
    result_copy = copy.copy(arg2)
    result_copy = result_copy.replace(arg2['key1'], 'new_value')

    # Use of locals() in a complex scope
    local_var_1 = 10
    local_var_2 = 20
    local_dict = locals()

    # Use of dbm.sqlite3
    try:
        db = dbm.sqlite3.open('testdb', 'c')
        db['key'] = str(thread_local_var)
        db.close()
    except Exception as e:
        print(f"Error opening or closing database: {e}")

    # Use of os timer functions
    start_time = time.monotonic()
    result_time = time.monotonic() - start_time
    return f"Result: {thread_local_var}, {result_time}"


# Example usage (demonstrates potential issues)
list_arg = [1, 2, 3, 4, 5]
dict_arg = {'key1': 'old_value', 'key2': 'another_value'}

try:
    result = complex_function(list_arg, dict_arg)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")

#  Demonstrates a complex type annotation within an annotation scope
def annotated_function(arg: typing.List[typing.Callable[[int], int]]) -> typing.Union[int, str]:
    pass

try:
    print(annotated_function([lambda x: x * 2, lambda x: x + 5]))
except Exception as e:
    print(f"An error occurred: {e}")


try:
  # Testing SSL with a potentially invalid certificate (replace with actual problematic cert)
  context = ssl.create_default_context()
  with context.wrap_socket(
      socket.socket(), server_hostname='invalid_hostname.example.com'
  ) as s:
    pass #Simulate a connection
except ssl.SSLError as e:
  print(f"SSL Error: {e}")


import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(arg: int):
    # Simulate a long-running task
    time.sleep(arg / 10)
    # Accessing a shared resource (potentially problematic)
    #  This is a race condition vulnerability if no lock used
    global shared_counter
    shared_counter += 1
    return shared_counter


def multi_threaded_example():
    global shared_counter
    shared_counter = 0
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Final counter value: {shared_counter}")


# Example usage of copy.replace (assuming a custom class)
class MyData:
    def __init__(self, value: int):
        self.value = value

    def __replace__(self, **kwargs):
      return type(self)(value=kwargs.get('value', self.value))
    

    def __str__(self):
       return str(self.value)

def copy_example():
    data = MyData(10)
    replaced_data = copy.replace(data, value=20)
    print(f"Original data: {data}, Replaced data: {replaced_data}")


# Example usage of dbm.sqlite3
def dbm_example():
  try:
    d = dbm.sqlite3.open("mydatabase", 'c')
    d['key1'] = 'value1'
    d.close()
  except Exception as e:
    print(f"Error with dbm operation: {e}")


#Example usage of os timer functions (simulated)
def os_timer_example():
  try:
    start_time = time.time()
    # Replace with real os calls
    time.sleep(2)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time}")

  except Exception as e:
    print(f"Error with os timer example: {e}")



#Fuzzing docstring whitespace:
def indented_docstring():
    """
    This function has
        a docstring
        with
        multiple lines
    """

    return 123


if __name__ == "__main__":
    multi_threaded_example()
    copy_example()
    dbm_example()
    os_timer_example()
    print(indented_docstring()) # Test Docstring whitespace



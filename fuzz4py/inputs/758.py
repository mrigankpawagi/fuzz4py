
import threading
import time
import copy
import ssl
import os
import dbm
import typing

def jit_sensitive_function(input_list):
    """
    A function likely to be JIT compiled.  
    """
    output = []
    for i in input_list:
        output.append(i * 2)
    return output


def multithreaded_example(data: typing.List[int]) -> typing.List[int]:
    """
    A multithreaded function demonstrating the free-threading feature.
    """
    results = []
    threads = []
    for i in data:
        thread = threading.Thread(target=jit_sensitive_function, args=([i],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for thread in threads:
        try:
            result = thread.join()
            if result:
                results.extend(result)  # Extend for a list of results
        except Exception as e:
            print(f"Thread error: {e}")
            return []  # Return empty list on error


    return results




def test_docstring_whitespace():
  """
  This docstring has varying whitespace.
    
  """
  return "whitespace matters"


def jit_sensitive_function_int(input_val):
    """
    A function likely to be JIT compiled, taking an integer.  
    """
    output = []
    for i in range(input_val):
        output.append(i * 2)
    return output


def multithreaded_example_int(data: typing.List[int]) -> typing.List[int]:
    """
    A multithreaded function demonstrating the free-threading feature.
    """
    results = []
    threads = []
    for i in data:
        thread = threading.Thread(target=jit_sensitive_function_int, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for thread in threads:
        try:
            result = thread.join()
            if result:
                results.extend(result)  # Extend for list of results
        except Exception as e:
            print(f"Thread error: {e}")
            return []  # Return empty list on error

    return results




def main():
  # Fuzzing the new features
  try:
      
    data = [1,2,3,4,5]
    results = multithreaded_example(data)
    print(f"Multithreaded results (list of lists): {results}")
    
    results_int = multithreaded_example_int(data)
    print(f"Multithreaded results (integers): {results_int}")

    # Example of complex type annotation.
    custom_data: typing.Dict[str, typing.List[int]] = {'key': [1, 2, 3]}
    print(f"Custom data: {custom_data}")
    
    # Example using copy.replace() (if applicable to your Python version)
    #  (No copy.replace() example provided in the original)

    # Fuzzing dbm.sqlite3
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        db.close()
        print("dbm.sqlite3 test successful")
    except Exception as e:
        print(f"dbm.sqlite3 error: {e}")

    # Fuzzing the ssl module
    try:
        context = ssl.create_default_context()
        print("ssl test successful")
    except Exception as e:
        print(f"ssl test error: {e}")

    # Fuzzing os module timer functions
    start_time = time.perf_counter()
    time.sleep(2)  # Simulate a task
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Duration: {duration}")

    # Example of a doctest with whitespace issues
    print(test_docstring_whitespace())


  except Exception as e:
    print(f"Error encountered: {e}")

  

if __name__ == "__main__":
    main()

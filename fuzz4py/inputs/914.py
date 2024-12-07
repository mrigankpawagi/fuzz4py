
import threading
import time
import copy
import os
import ssl
import typing


def complex_function(data: typing.List[int], replace_val: int = 0) -> typing.List[int]:
    """
    A function with complex logic that demonstrates threading.
    Also uses copy.replace() and typing annotations.
    """
    
    if not isinstance(data, list):
        raise TypeError("Input data must be a list.")
        
    for i in range(len(data)):
        if isinstance(data[i], int):
            data[i] = data[i] + 1

    # Simulate a long-running task
    time.sleep(1)

    # Example use of copy.replace
    if hasattr(data[0], "__replace__"): # Check if replace is supported
        data_copy = copy.replace(data[0], newval = replace_val)
        data[0] = data_copy
    
    return data

def thread_test():
  
  test_data = [1,2,3,4,5]
  
  results = []

  for i in range(3):
    thread_result = threading.Thread(target=complex_function, args=(test_data, i))
    thread_result.start()
    results.append(thread_result)

  for thread in results:
    thread.join()

  # Simulate handling of results
  for thread_result in results:
    print("result:", complex_function(test_data))
    
  return results

if __name__ == "__main__":
  try:
    # Example usage to test threading.
    thread_test()
    print("Test completed without errors.")
  except Exception as e:
    print(f"Error during test: {e}")

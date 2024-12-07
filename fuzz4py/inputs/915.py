
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
    
    local_data = data[:]  # Create a copy to avoid modifying the original data in the thread
    for i in range(len(local_data)):
        if isinstance(local_data[i], int):
            local_data[i] = local_data[i] + 1

    time.sleep(1)

    if hasattr(local_data[0], "__replace__"):
        local_data_copy = copy.replace(local_data[0], newval=replace_val)
        local_data[0] = local_data_copy
    
    return local_data


def thread_test():
  
  test_data = [1,2,3,4,5]
  
  results = []

  for i in range(3):
    thread_result = threading.Thread(target=complex_function, args=(test_data.copy(), i)) # Crucial: copy the list
    thread_result.start()
    results.append(thread_result)

  for thread in results:
    thread.join()

  for i in range(3):
    # Correctly accessing the result of each thread
    print(f"result {i+1}:", complex_function(test_data.copy(), i))
    
  return results

if __name__ == "__main__":
  try:
    thread_test()
    print("Test completed without errors.")
  except Exception as e:
    print(f"Error during test: {e}")


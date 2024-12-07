
import threading
import copy
import os
import ssl
import typing

def worker(arg):
    try:
        # Simulate a CPU-bound task
        result = sum(range(1000000))
        
        # Use copy.replace to modify a mutable object
        my_list = copy.deepcopy([1, 2, 3])
        
        if isinstance(arg, str):
          my_list.append(arg)
        else:
          my_list.append(0) # handle non-string args

        my_list_modified = copy.replace(my_list, arg=arg)
        
        return result, my_list_modified, arg
    except Exception as e:
        return str(e), None, arg

def main():
    threads = []
    
    # Fuzzing with varying input types
    for i in range(5):
        if i % 2 == 0:
          thread_arg = "test_string" + str(i)
        else:
          thread_arg = i*2
        thread = threading.Thread(target=worker, args=(thread_arg,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
    results = []
    for thread in threads:
       # handle potential exceptions during join
        try:
          result_val, modified_list, arg = thread.result()
          results.append((result_val, modified_list, arg))
        except Exception as e:
            print(f"Error in thread: {e}")
    
    for result, modified_list, arg in results:
      print(f"Result: {result}, Modified List: {modified_list}, Input: {arg}")

if __name__ == "__main__":
    main()

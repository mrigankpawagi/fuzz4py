
import threading
import time
import copy
import os
import ssl
import dbm
import typing


def race_condition_test(data):
    # Simulate a shared resource
    shared_resource = 0

    def increment():
        nonlocal shared_resource
        shared_resource += data
        time.sleep(0.001)  # Introduce a delay for potential race conditions

    threads = []
    for _ in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return shared_resource



def jit_test():
    i = 0
    while i < 1000000:
        #Likely target for JIT compilation - hot loop
        result = 2 * i + 1
        i += 1
    return result


def complex_annotation_test(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    """A function with complex type annotations to test typing module."""
    results = []
    for item in data:
        if isinstance(item, int):
            results.append(item * 2)
        elif isinstance(item, str):
           # Handle strings in the way you want
           results.append(int(item)) #Example: convert to integer

    return results


def test_replace(data):
  #Test for copy.replace()
  class MyData:
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __replace__(self, *, a=None, b=None):
      return type(self)(a if a is not None else self.a, b if b is not None else self.b)
  
  original_data = MyData(1, 2)
  new_data = copy.replace(original_data, a=3)  
  return new_data.a



def main():
    # Test free-threading: race condition with varying inputs
    print(f"Race condition test (using a large integer): {race_condition_test(10000)}")

    # Test JIT compiler
    result = jit_test()
    print(f"JIT test result: {result}")


    #Test Complex Type Annotations
    complex_data = [1, 2, "3", 4, "5"]
    results = complex_annotation_test(complex_data)
    print(f"Complex type annotation test results: {results}")

    #Test for copy.replace()
    result = test_replace(1)
    print(f"Replace test result: {result}")


    #Test os module timer functions (Linux specific - uncomment to run)
    #try:
    #  timer_result = os.times()
    #  print(f"Timer result: {timer_result}")
    #except AttributeError as e:
    #  print(f"AttributeError: {e}") #Handle the AttributeError if os.times() is not available

if __name__ == "__main__":
    main()

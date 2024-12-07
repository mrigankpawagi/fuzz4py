
import threading
import copy
import time
import os
import ssl
import typing

def worker(i):
    # Simulate some work
    time.sleep(0.1)
    print(f"Thread {i}: working")

def test_free_threading():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    # Using copy.replace() on a custom class.
    class MyClass:
        def __init__(self, x):
            self.x = x
        def __replace__(self, x=None):
          if x is not None:
            return copy.copy(self)  # Important for proper immutability
          return self

    a = MyClass(10)
    b = copy.replace(a, x=20)

    print(f"a.x: {a.x}")
    print(f"b.x: {b.x}")


def test_os_timer():
  # Test the os module timer functions
  try:
    start_time = time.time()
    result = os.times()
    end_time = time.time()
    print(f"Time taken by os.times(): {end_time - start_time:.6f}")
    print(f"Returned values: {result}")

  except Exception as e:
    print(f"Error in os.times(): {e}")


def test_ssl():
    try:
      context = ssl.create_default_context()
      print("SSL context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

def main():
  test_free_threading()
  test_os_timer()
  test_ssl()

if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import typing
import random
import sys

def worker(arg: int, lock: threading.Lock, extra_arg: str = ""):
    lock.acquire()
    try:
        print(f"Thread {threading.get_ident()} received: {arg}, extra arg: {extra_arg}")
        time.sleep(arg % 5)  # Introduce varying sleep times
        if random.random() < 0.1:
          raise Exception("Simulated error in thread")
    except Exception as e:
        print(f"Exception in thread: {e}")
    finally:
        lock.release()

def main():
    lock = threading.Lock()
    threads = []
    for i in range(5):
        extra_arg = str(random.randint(1, 100))
        thread = threading.Thread(target=worker, args=(i, lock, extra_arg))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


    # Example using copy.replace() (Illustrative, more fuzzing)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y
        def __replace__(self, **kwargs):
          try:
            return copy.copy(self)
          except Exception as e:
              print(f"Error in __replace__: {e}")
              return None

    p1 = Point(1, 2)
    try:
        p2 = copy.replace(p1, x=3)
        p3 = copy.replace(p1, x=random.randint(1,100), y = random.randint(1,100))
    except Exception as e:
        print(f"Error in copy.replace(): {e}")

    # Testing os module timer functions (more fuzzing)
    for _ in range(5):
      try:
        start_time = time.perf_counter()
        result = os.times()
        end_time = time.perf_counter()
        print(f"Time taken to call os.times(): {end_time - start_time}, result: {result}")
        input_val = random.randint(1,100)  # Varying input
        os.times(input_val)
      except Exception as e:
          print(f"Error in os.times(): {e}")
    
    # Testing ssl.create_default_context() (fuzzing certificates)
    try:
        context = ssl.create_default_context()
        # ... (example of using the context to connect to a server)
        # More extensive testing with various SSL contexts.
        bad_cert = "some_bad_certificate.crt"
        context.load_verify_locations(bad_cert)  # Example of loading bad certificate
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    
    # Testing complex annotations (fuzzing with various types)
    def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
        try:
            result = []
            for item in data:
              if isinstance(item, int):
                result.append(item * 2)
              elif isinstance(item, str):
                try:
                  result.append(int(item) * 3)
                except ValueError:
                  result.append(-1) #Handle bad data gracefully
            return result
        except Exception as e:
            print(f"Error in process_data: {e}")
            return []


    annotated_data: typing.List[typing.Union[int, str]] = [1, 2, "3", "abc", 1000, "1234567", "xyz"]
    processed_data = process_data(annotated_data)
    print(f"Processed data: {processed_data}")

    # More testing with different input types
    annotated_data2 = [1, 2, 3.14, "4", "abc", None]
    processed_data2 = process_data(annotated_data2)
    print(f"Processed data 2: {processed_data2}")


if __name__ == "__main__":
    main()

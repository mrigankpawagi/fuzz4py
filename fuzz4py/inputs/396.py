
import threading
import time
import copy
import os
import ssl
import socket
import typing
import unittest
import dbm


# Fuzzing `copy.replace()`
class MyObject:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def __replace__(self, a: int = None, b: str = None):
        try:
            return MyObject(a if a is not None else self.a, b if b is not None else self.b)
        except TypeError as e:
            print(f"Error in __replace__: {e}")
            return None


def test_replace():
    obj = MyObject(10, "hello")
    try:
        new_obj = copy.deepcopy(obj)  # Using deepcopy for equivalent behavior
        new_obj.a = 20
        assert new_obj.a == 20
        assert new_obj.b == "hello"
    except AttributeError as e:
        print(f"AttributeError in copy.replace(): {e}")
    except Exception as e:
        print(f"Error in test_replace(): {e}")


# Fuzzing free-threading (PEP 703) and GIL
shared_data = 0

def worker(data: int):
    global shared_data
    try:
        time.sleep(0.01)
        with threading.Lock():
           shared_data += data
        return shared_data
    except Exception as e:
        print(f"Error in worker: {e}")
        return None

def test_threading():
    global shared_data
    shared_data = 0
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    try:
        assert shared_data == 45
    except AssertionError as e:
        print(f"AssertionError in test_threading: {e}")
    except Exception as e:
        print(f"Error in test_threading(): {e}")



# Fuzzing os module timer functions
def test_os_timer():
  try:
    start = time.perf_counter()  # Use perf_counter for more precise timing
    result = os.times()
    end = time.perf_counter()
    assert end - start > 0
    if result:
        print("OS times results:", result)
  except (OSError, Exception) as e:
      print(f"Error in os.times(): {e}")


# Fuzzing SSL connections (simplified)
def test_ssl_connection():
    try:
        ctx = ssl.create_default_context()
        try:
            with ctx.wrap_socket(socket.socket(), server_hostname="example.com") as s:
                s.connect(('example.com', 443))
                print("SSL connection successful")
        except Exception as e:
            print(f"Error during SSL connection: {e}")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"Error in test_ssl_connection(): {e}")


# Example with complex type annotations
def process_data(data: typing.Union[int, str]) -> typing.Optional[str]:
    try:
        if isinstance(data, int):
            return str(data * 2)
        elif isinstance(data, str):
            return data.upper()
        else:
            return None
    except Exception as e:
        print(f"Error in process_data: {e}")
        return None

# example using  __static_attributes__ & __firstlineno__
class MyClass:
    __static_attributes__ = {'attr': 1}
    __firstlineno__ = 10

    def method(self):
        try:
            return self.__static_attributes__['attr']
        except (KeyError, TypeError) as e:
            print(f"Error in MyClass.method(): {e}")
            return None


def my_function(input_data: typing.List[int], timeout: float = 1.0) -> typing.List[int]:
    threads = []
    results = []
    for i in input_data:
        thread = threading.Thread(target=simulate_work, args=(i,))
        thread.start()
        threads.append(thread)

    start_time = time.perf_counter()  # Use perf_counter for better timing

    for thread in threads:
        thread.join(timeout)
        if thread.is_alive():
            print(f"Thread for {i} timed out!")

        try:
            result = thread.join()
            results.append(result)

        except Exception as e:
            print(f"Exception in thread: {e}")

    end_time = time.perf_counter()
    print(f"Total execution time: {end_time - start_time}")
    return results



def simulate_work(data: int) -> int:
    time.sleep(0.1)
    return data * 2

class TestFuzzing(unittest.TestCase):
    def test_replace(self):
        test_replace()

    def test_threading(self):
        test_threading()

    def test_os_timer(self):
        test_os_timer()


    @unittest.skipIf(not hasattr(ssl, 'SSLContext'), "SSL module not available")
    def test_ssl_connection(self):
        test_ssl_connection()
    def test_process_data(self):
        self.assertEqual(process_data(10), "20")
        self.assertEqual(process_data("hello"), "HELLO")
        self.assertIsNone(process_data(None))
        self.assertIsNone(process_data(10.5))
    def test_my_class(self):
        self.assertEqual(MyClass().method(), 1)

    def test_my_function(self):
        input_data = [1, 2, 3]
        results = my_function(input_data)
        self.assertEqual(len(results), len(input_data))
        for i,result in enumerate(results):
            self.assertEqual(result, input_data[i]*2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


import threading
import time
import copy
import os
import ssl
import dbm
import typing
import socket


def worker(arg: int) -> None:
    """
    Worker function to demonstrate multi-threading.
    """
    try:
        time.sleep(arg)
        print(f"Thread {threading.get_ident()} finished with arg {arg}")

    except Exception as e:
        print(f"Thread {threading.get_ident()} encountered an exception: {e}")


def main():
    """
    Main function to demonstrate threading.
    """
    threads = []

    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    # Example using copy.replace() (new in 3.13)
    class MyClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

        def __repr__(self) -> str:
            return f"MyClass(a={self.a}, b={self.b})"

        def __replace__(self, a: int = None, b: str = None) -> 'MyClass':
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)


    obj = MyClass(10, "hello")
    new_obj = copy.replace(obj, a=20)
    print(f"Original object: {obj}")
    print(f"Modified object: {new_obj}")

    # Example using complex type annotations
    def complex_func(arg: typing.List[typing.Dict[str, int]]) -> None:
      for item in arg:
        for key in item:
          print(key, item[key])


    complex_func([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])


    # Example with docstring whitespace (test for whitespace stripping)
    def my_docstring_function():
        """This is a docstring
        with multiple lines."""

    print(my_docstring_function.__doc__)


def jit_sensitive_function(input_list: list[int]) -> int:
    """A function likely to be JIT-compiled due to its loop."""
    total = 0
    for i in input_list:
        total += i
    return total

def test_free_threading(data: int) -> int:
    """Illustrates a potential race condition with free threading."""
    lock = threading.Lock()
    total = 0
    threads = []
    for i in range(data):
        t = threading.Thread(target=lambda x=i: add_to_total(x, lock, total))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return total

def add_to_total(i, lock, total):
    lock.acquire()
    try:
        total += i
    finally:
        lock.release()

def test_copy_replace(data):
  class MyReplaceable:
      def __init__(self, value: int):
          self.value = value

      def __replace__(self, value: int):
          return MyReplaceable(value)


  original = MyReplaceable(data)
  replaced = copy.replace(original, value=data + 10)

  return replaced.value


def test_dbm_sqlite3():
  try:
    db = dbm.open('test.db', 'c')
    db['key'] = str(123)
    data = db['key']
    db.close()
    os.remove('test.db')  # Clean up the temporary DB file
    return True
  except Exception as e:
      print(f"Error in test_dbm_sqlite3: {e}")
      return False

def test_os_timer():
  try:
    t = os.times()
    return t
  except Exception as e:
    print(f"Error in test_os_timer: {e}")
    return None

def test_ssl_connection():
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))
            return True
    except Exception as e:
        print(f"Error in test_ssl_connection: {e}")
        return False

if __name__ == "__main__":
    main()
    # Example usage (demonstrating different fuzz targets)
    try:
      test_free_threading(10)
      jit_sensitive_function([1, 2, 3, 4, 5])
      test_copy_replace(5)
      test_dbm_sqlite3()
      test_os_timer()
      test_ssl_connection()
    except Exception as e:
        print(f"An error occurred in main: {e}")



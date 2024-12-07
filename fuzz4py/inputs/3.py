
import threading
import time
import copy
import os
import ssl
import typing


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

if __name__ == "__main__":
    main()

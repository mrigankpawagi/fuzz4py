
import threading
import copy
import time
import os
import ssl
import typing
import socket

def jit_sensitive_function(data: typing.List[int]) -> int:
    """A function likely to be JIT-compiled."""
    total = 0
    for i in range(len(data)):
        try:
            total += data[i]
        except IndexError:
            return -1  # Handle potential IndexError
    return total

def multithreaded_operation(data):
    """A multithreaded function demonstrating free-threading."""
    results = []
    for item in data:
        t = threading.Thread(target=jit_sensitive_function, args=(item,))
        results.append(t)
        try:
            t.start()
        except RuntimeError as e:
          print(f"Error starting thread: {e}")
          return [] #Return empty list to handle errors
    
    for result in results:
        try:
            result.join()
        except RuntimeError as e:
          print(f"Error joining thread: {e}")
          return [] #Return empty list to handle errors
    
    return [r.name for r in results]


def main():
    # Testing free-threading and JIT compiler
    data = [[i for i in range(100)] for _ in range(5)]
    results = multithreaded_operation(data)
    if results:
        print(f"Multithreaded results: {results}")
    
    # Testing the new replace protocol
    class MyClass:
        def __init__(self, a: int, b: str) -> None:
            self.a = a
            self.b = b

        def __replace__(self, a: int = None, b: str = None) -> "MyClass":
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

        def __repr__(self) -> str:
            return f"MyClass(a={self.a}, b='{self.b}')"
            

    original_object = MyClass(10, "test")
    try:
        replaced_object = copy.replace(original_object, a=20,b=None)  # Try replacing b with None
    except TypeError as e:
        print(f"Error with replace: {e}")
    else:
        print(f"Original: {original_object}")
        print(f"Replaced: {replaced_object}")
        
    #Testing os module timer functions
    try:
      start = time.perf_counter()
      os.times()
      end = time.perf_counter()
      print(f"OS time elapsed: {end-start:.4f} seconds")
    except Exception as e:
        print(f"Error with os.times(): {e}")

    #Example with complex typing and annotations
    def complex_function(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
        results = []
        for item in data:
          try:
            if isinstance(item, int):
              results.append(item)
          except Exception as e:
            print(f"Error processing item: {item}, Error:{e}")

        return results

    # Example usage
    complex_data = [1, "a", 2, "b", 3, None]  #Added None
    complex_results = complex_function(complex_data)
    print(f"Complex Function results: {complex_results}")

    #Testing ssl module
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443))
            print("SSL connection established.")
    except Exception as e:
        print(f"SSL connection failed: {e}")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

if __name__ == "__main__":
    main()

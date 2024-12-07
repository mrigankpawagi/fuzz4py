
import threading
import copy
import time
import os
import ssl
import typing

def jit_sensitive_function(data: typing.List[int]) -> int:
    """A function likely to be JIT-compiled."""
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total

def multithreaded_operation(data):
    """A multithreaded function demonstrating free-threading."""
    results = []
    for item in data:
        t = threading.Thread(target=jit_sensitive_function, args=(item,))
        results.append(t)
        t.start()

    for result in results:
        result.join()
    return [r.name for r in results]



def main():
    # Testing free-threading and JIT compiler
    data = [[i for i in range(100)] for _ in range(5)]
    multithreaded_operation(data)
    
    # Testing the new replace protocol
    class MyClass:
        def __init__(self, a: int, b: str) -> None:
            self.a = a
            self.b = b

        def __replace__(self, a: int = None, b: str = None) -> "MyClass":
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)

    original_object = MyClass(10, "test")
    replaced_object = copy.replace(original_object, a=20)


    print(f"Original: {original_object.a}, {original_object.b}")
    print(f"Replaced: {replaced_object.a}, {replaced_object.b}")

    #Testing os module timer functions
    start = time.perf_counter()
    os.times()
    end = time.perf_counter()
    print(f"OS time elapsed: {end-start:.4f} seconds")

    #Example with complex typing and annotations
    def complex_function(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
        results = []
        for item in data:
          if isinstance(item, int):
            results.append(item)
        return results


    # Example usage
    complex_data = [1, "a", 2, "b", 3]
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

if __name__ == "__main__":
    import socket
    main()

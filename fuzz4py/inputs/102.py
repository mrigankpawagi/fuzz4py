
import threading
import copy
import time
import ssl
import os
import typing

def threaded_function(data, context):
    # Simulate a potentially JIT-compiled function
    result = 0
    for _ in range(100000):
        result += data
    return result + len(data)

def main():
    # Test free-threading and GIL
    data = b"test" * 10000
    results = []
    threads = []

    for i in range(5):
        t = threading.Thread(target=threaded_function, args=(data, threading.get_ident()))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


    # Test copy.replace()
    class MyReplaceable(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, **changes):
            new_obj = copy.copy(self)
            for key, value in changes.items():
                setattr(new_obj, key, value)
            return new_obj

    obj = MyReplaceable(1, 2)
    new_obj = obj.__replace__(a=3)
    print(new_obj.a, new_obj.b)  # Output: 3 2


    # Test Docstring whitespace stripping
    def my_function():
        """
        This is a
        docstring.
        """
        pass

    print(my_function.__doc__)


    # Test annotation scopes
    AnnotationType = typing.List[int]
    result = sum([i for i in range(10) if i%2==0], start=0)

    # Example with complex annotation using PEP 696
    ComplexType = typing.List[typing.Union[int, str, typing.Callable[[int], bool]]]
    a_complex_variable : ComplexType = [1, "hello", lambda x: x > 5]


    # Test ssl.create_default_context()
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname="example.com") as s:
            s.connect(("example.com", 443))
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

    # Test os module timer function
    start_time = time.perf_counter()
    result = os.times()
    end_time = time.perf_counter()

    print(f"Time taken: {end_time-start_time:.4f}")
    print(result)



if __name__ == "__main__":
    import socket
    main()



import threading
import time
import copy
import os
import ssl
import typing
import random

def test_free_threading(num_threads: int = 10):
    shared_counter = 0
    
    def increment_counter():
        nonlocal shared_counter
        for _ in range(10000):
            shared_counter += 1
            # Introduce potential race condition by adding a sleep
            time.sleep(random.random() * 0.0001)  

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return shared_counter


def test_jit_compiler():
    # This example is designed to be a hot loop, therefore likely compiled
    count = 0
    for i in range(1000000):
        count += i % 7 
        count = count*2
        # Introduce a potentially JIT-targeted branch
        if random.random() < 0.01:
          count = -1 * count
    
    return count


def test_complex_annotation():
    Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
    
    def process_point(p: Point) -> int:
        return p.x + p.y
    
    #Fuzz with different data types, even if invalid.
    try:
        my_point = Point(5, 10)
        return process_point(my_point)
    except Exception as e:
      return str(e)
    

def test_copy_replace():
    class MyObject:
        def __init__(self, val1: int, val2: str):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, val1=None, val2=None):
            # Add a potential error case
            if val1 is None:
                return None
            return MyObject(val1 if val1 is not None else self.val1, val2 if val2 is not None else self.val2)
    
    myobj = MyObject(1, "hello")
    try:
        replaced_obj = copy.replace(myobj, val1=2)
        return replaced_obj.val1
    except Exception as e:
        return str(e)


# Example using ssl.create_default_context()
def test_ssl_context():
    try:
        context = ssl.create_default_context()
        #Simulates connection attempt, no actual connection needed
        #Introduce a potential error condition.
        invalid_cert = b"invalid" * 1024
        context.check_hostname = False  #Important for testing
        with context.wrap_socket(random.choice([socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET6, socket.SOCK_STREAM)]), server_hostname="example.com") as s:
            return True
    except ssl.SSLError as e:
        return str(e)
    except Exception as e:
        return str(e)
import socket

def main():
    try:
        print(test_free_threading())
        print(test_jit_compiler())
        print(test_complex_annotation())
        print(test_copy_replace())
        print(test_ssl_context())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

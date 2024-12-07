
import threading
import time
import copy
import os
import ssl
import typing

def test_free_threading(num_threads: int = 10):
    shared_counter = 0
    
    def increment_counter():
        nonlocal shared_counter
        for _ in range(10000):
            shared_counter += 1

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
        
    return count


def test_complex_annotation():
    Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
    
    def process_point(p: Point) -> int:
        return p.x + p.y
    
    my_point = Point(5, 10)
    return process_point(my_point)
    

def test_copy_replace():
    class MyObject:
        def __init__(self, val1: int, val2: str):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, val1=None, val2=None):
            return MyObject(val1 if val1 is not None else self.val1, val2 if val2 is not None else self.val2)
    
    myobj = MyObject(1, "hello")
    replaced_obj = copy.replace(myobj, val1=2)
    
    return replaced_obj.val1

# Example using ssl.create_default_context()
def test_ssl_context():
    try:
        context = ssl.create_default_context()
        #Simulates connection attempt, no actual connection needed
        return True
    except ssl.SSLError as e:
        return str(e)


def main():
    print(test_free_threading())
    print(test_jit_compiler())
    print(test_complex_annotation())
    print(test_copy_replace())
    print(test_ssl_context())


if __name__ == "__main__":
    main()

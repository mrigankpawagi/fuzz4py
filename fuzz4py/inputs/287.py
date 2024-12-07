
import threading
import time
import copy
import os
import ssl
import typing
import random
import socket

def test_free_threading(num_threads: int = 10):
    shared_counter = 0
    
    def increment_counter():
        nonlocal shared_counter
        for _ in range(10000):
            try:
                shared_counter += 1
            except TypeError:
                pass
            time.sleep(random.random() * 0.0001)
            try:
                global_var = random.randint(0,100)
            except NameError:
                pass
            if random.random() < 0.01:
                try:
                    shared_counter = -shared_counter
                except TypeError:
                    pass
            try:
                global some_global_var
                some_global_var = f"Fuzzing{random.randint(0,1000)}"
            except NameError:
                pass
            if random.random() < 0.0005:
                return
            if random.random() < 0.001:
                raise ValueError("Fuzzing Exception")
            invalid_types = [float('inf'), "not a number", None, random.random(), "abc", True, [1, 2, 3], {1: "a"}, (1, 2, 3), float('inf')]
            if random.random() < 0.005:
              shared_counter = random.choice(invalid_types)
              

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return shared_counter


def test_jit_compiler():
    count = 0
    for i in range(1000000):
        count += i % 7
        count *= 2
        if random.random() < 0.01:
            count = -count
        try:
            count = count / random.uniform(0.1, 10)
        except ZeroDivisionError:
            count = 0
        
        invalid_types = ["invalid" + str(random.randint(0,1000)), None]
        if random.random() < 0.05:
            count = random.choice(invalid_types)
        if random.random() < 0.01:
            count = [i for i in range(random.randint(1, 10))]
        if random.random() < 0.0005:
            try:
                count = lambda x: x * 2
            except TypeError:
                pass

    return count


def test_complex_annotation():
    Point = typing.NamedTuple('Point', [('x', int), ('y', int)])
    
    def process_point(p: Point) -> int:
        try:
            return p.x + p.y
        except AttributeError as e:
            return str(e)

    try:
        my_point = Point(5, 10)
        return process_point(my_point)
    except Exception as e:
        return str(e)
    return "Finished"


def test_copy_replace():
    class MyReplaceableClass:
        def __init__(self, value: int):
            self.value = value

        def __replace__(self, **changes):
            try:
                return MyReplaceableClass(changes.get('value', self.value))
            except TypeError:
              return None

    original = MyReplaceableClass(10)
    new = copy.replace(original, value=20)
    if new:
        return new.value
    else:
      return None

def test_ssl_context():
    try:
        context = ssl.create_default_context()
        context.check_hostname = False  #Important for testing
        try:
            invalid_cert = b"invalid" * 1024
            invalid_hostname = f"invalidhost{random.randint(0, 1000)}.com"
            sock_type = random.choice([socket.AF_INET, socket.AF_INET6])
            with context.wrap_socket(socket.socket(sock_type, socket.SOCK_STREAM), server_hostname=invalid_hostname) as s:
                return True
        except Exception as e:
            return str(e)
    except Exception as e:
        return str(e)


def main():
    try:
        print(test_free_threading(num_threads=random.randint(2,20)))
        print(test_jit_compiler())
        print(test_complex_annotation())
        print(test_copy_replace())
        print(test_ssl_context())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

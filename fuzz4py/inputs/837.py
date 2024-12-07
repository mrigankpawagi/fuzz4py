
import threading
import time
import copy
import os
import ssl
import dbm
import socket
import typing
import random

shared_data = 0
shared_var = 0

def threaded_function(arg):
    global shared_data
    time.sleep(random.uniform(0.05, 0.15))
    try:
        shared_data += arg
        shared_data += arg * 2
        if isinstance(arg, str):
            shared_data += int(arg)
        elif isinstance(arg, list):
            for item in arg:
                shared_data += item
        elif isinstance(arg, (int, float)):
            shared_data += arg * random.random()
        else:
            shared_data += 0
    except (TypeError, ValueError, OverflowError) as e:
        print(f"Caught exception in threaded_function: {e}")
    if random.random() < 0.1:
        raise ValueError("Simulated error in thread")
    try:
        shared_data += float(arg)
    except (ValueError, TypeError) as e:
        print(f"Could not convert arg to float: {e}")


def main():
    global shared_data, shared_var
    shared_data = 0
    shared_var = 0

    threads = []
    num_threads = random.randint(3, 7)
    for i in range(num_threads):
        input_list = [i, "str", 10.5, [1, 2, 3]]
        t = threading.Thread(target=threaded_function, args=(random.choice(input_list),))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Shared data after threads: {shared_data}")


    try:
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __replace__(self, **kwargs):
                if 'x' in kwargs:
                    try:
                        self.x = int(kwargs['x'])
                    except ValueError:
                        print("Error: x value not convertible to int")
                        return None

                if 'y' in kwargs:
                    try:
                        self.y = int(kwargs['y'])
                    except ValueError:
                        print("Error: y value not convertible to int")
                        return None

                return self

        p1 = Point(1, 2)
        p2 = copy.replace(p1, x=random.randint(5, 15))
        p3 = copy.replace(p1, y=random.random())
        p4 = copy.replace(p1, x="not a valid int")
        assert p1.x == 1
        assert p2.x == p2.x

        def my_function(arg: typing.List[int]) -> int:
            try:
                return sum(arg)
            except (TypeError, ValueError) as e:
                print(f"Caught error in my_function: {e}")
                return 0
            except Exception as e:
                print(f"Caught an unexpected error: {e}")
                return 0

        my_list = [1, 2, 3]
        result = my_function(my_list)
        print(f"Result: {result}")

        try:
            my_function("not a list")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

        try:
            my_function([1, 2, "3"])
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    except Exception as e:
        print(f"Exception caught in main: {e}")


    start_time = time.monotonic()
    time.sleep(random.uniform(0.3, 0.7))
    end_time = time.monotonic()
    print(f"Time elapsed (monotonic): {end_time - start_time}")

    try:
        context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            print("SSL connection successful")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")

def thread_func(x):
    global shared_var
    time.sleep(random.uniform(0.05, 0.15))
    try:
        shared_var += x
    except TypeError:
        print("Error in thread_func: Type error")
        return  

    if random.random() < 0.2:
        shared_var = 0


def jit_test(n):
    sum_val = 0
    for i in range(n):
        sum_val += i * 2
    return sum_val


def complex_function(data):
    try:
        if isinstance(data, list):
            return sum(data)
        elif isinstance(data, tuple):
            return int(data[1])
        elif isinstance(data, str):
            return int(data)
        else:
            return 0
    except (ValueError, TypeError) as e:
        print(f"Error in complex_function: {e}")
        return 0


if __name__ == "__main__":
    main()


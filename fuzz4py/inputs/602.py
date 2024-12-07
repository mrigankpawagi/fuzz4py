
import threading
import time
import copy
import os
import ssl
import typing
import random

def threaded_function(arg: int, context: ssl.SSLContext, some_random_data=None):
    """
    Demonstrates free-threading with potential race conditions.
    """
    try:
        if some_random_data:
            try:
                int(some_random_data)  # Attempt conversion to int, handle potential ValueError
            except ValueError:
                pass  # Ignore non-integer input
        with context:
            time.sleep(random.uniform(0.05, 0.15))
            print(f"Thread {threading.get_ident()} processed {arg} with {some_random_data}" if some_random_data else f"Thread {threading.get_ident()} processed {arg}")
    except Exception as e:
        print(f"Error in thread {threading.get_ident()}: {e}")


def main():
    # Fuzzing with varying contexts
    contexts = [
        ssl.create_default_context(),
        ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT),
        ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER),
        ssl.SSLContext(random.choice([ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLSv1_3, ssl.PROTOCOL_TLSv1_2]))
        for _ in range(3)
    ]

    args = [1, 2, 3, 4, 5] + [random.randint(-100, 100) for _ in range(5)]

    threads = []
    for arg in args:
        for context in contexts:
            some_random_data = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(random.randint(0, 20)))
            thread = threading.Thread(target=threaded_function, args=(arg, context, some_random_data))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()


    #Demonstrate copy.replace with a custom class:
    class MyReplaceable:
        def __init__(self, value: int):
            self.value = value
        def __replace__(self, **kwargs):
          try:
            if 'value' in kwargs:
              self.value = int(kwargs['value'])
            return self
          except ValueError:
            print("Invalid value type")
            return self  # Crucial to return self in case of error


    my_object = MyReplaceable(10)
    replaced_object = copy.replace(my_object, value="abc")
    try:
        replaced_object2 = copy.replace(my_object, value=10.5)
    except TypeError as e:
        print(f"Error during replace: {e}")


    print(f"Original object: {my_object.value}")
    print(f"Replaced object: {replaced_object.value if hasattr(replaced_object, 'value') else 'Replaced object does not have value attribute'}")
    print(f"Replaced object2: {replaced_object2.value if hasattr(replaced_object2, 'value') else 'Replaced object2 does not have value attribute'}")


if __name__ == "__main__":
    main()

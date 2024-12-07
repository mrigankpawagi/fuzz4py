
import threading
import time
import copy
import os
import ssl
import typing

def threaded_function(arg: int, context: ssl.SSLContext):
    """
    Demonstrates free-threading with potential race conditions.
    """
    try:
        with context as c:
            #Simulate work, potentially long-running
            time.sleep(0.1)
            print(f"Thread {threading.get_ident()} processed {arg}")
    except Exception as e:
        print(f"Error in thread {threading.get_ident()}: {e}")

def main():
    #Fuzzing with varying contexts (e.g., invalid certs, etc)
    contexts = [ssl.create_default_context(), ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)]  #Example: Create different SSL contexts


    #Illustrating various inputs
    args = [1, 2, 3, 4, 5]

    threads = []
    for arg in args:
        for context in contexts:  #Loop through various contexts

            thread = threading.Thread(target=threaded_function, args=(arg, context))
            threads.append(thread)
            thread.start()


    for thread in threads:
        thread.join()


    #Demonstrate copy.replace with a custom class:
    class MyReplaceable:
        def __init__(self, value: int):
            self.value = value
        def __replace__(self, **kwargs):
          if 'value' in kwargs:
              self.value = kwargs['value']
          return self


    my_object = MyReplaceable(10)
    replaced_object = copy.replace(my_object, value=20)
    print(f"Original object: {my_object.value}")  #Original should remain unchanged.
    print(f"Replaced object: {replaced_object.value}")


if __name__ == "__main__":
    main()


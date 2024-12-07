
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
            # Fuzzing - Introduce random data into the function
            try:
              int(some_random_data)
            except ValueError:
                pass

        with context as c:
            #Simulate work, potentially long-running
            time.sleep(random.uniform(0.05, 0.15)) #Random sleep times
            print(f"Thread {threading.get_ident()} processed {arg} with {some_random_data}" if some_random_data else f"Thread {threading.get_ident()} processed {arg}")
    except Exception as e:
        print(f"Error in thread {threading.get_ident()}: {e}")

def main():
    # Fuzzing with varying contexts (e.g., invalid certs, etc)
    contexts = [ssl.create_default_context(), ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT), ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)]  #Add a server context
    contexts.extend([ssl.SSLContext(random.choice([ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_TLSv1_3,ssl.PROTOCOL_TLSv1_2])) for _ in range(3)]) #Fuzz more protocols

    #Illustrating various inputs
    args = [1, 2, 3, 4, 5] + [random.randint(-100,100) for _ in range(5)] #Add some random values


    threads = []
    for arg in args:
        for context in contexts:  #Loop through various contexts
            # Fuzzing - Introduce random data
            some_random_data = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(random.randint(0,20)))

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
          if 'value' in kwargs:
              try:
                self.value = int(kwargs['value'])
              except ValueError:
                  print("Invalid value type")
                  pass
          return self


    my_object = MyReplaceable(10)
    replaced_object = copy.replace(my_object, value="abc")  #Fuzzing with a string value
    try:
      replaced_object2 = copy.replace(my_object, value=10.5) #Fuzzing with a float
    except TypeError as e:
      print(f"Error during replace: {e}")


    print(f"Original object: {my_object.value}")  #Original should remain unchanged.
    print(f"Replaced object: {replaced_object.value if hasattr(replaced_object,'value') else 'Replaced object does not have value attribute'}")
    print(f"Replaced object2: {replaced_object2.value if hasattr(replaced_object2,'value') else 'Replaced object2 does not have value attribute'}")


if __name__ == "__main__":
    main()

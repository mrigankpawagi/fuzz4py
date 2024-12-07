
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
            shared_counter += 1
            # Introduce potential race condition by adding a sleep
            time.sleep(random.random() * 0.0001)  
            # Introduce a potential error by changing a global variable
            global_var = random.randint(0,100)
            # Add a random attempt to set shared_counter to a negative value
            if random.random() < 0.01:
                shared_counter = -shared_counter
            # Introduce a random attempt to modify another global variable, if it exists
            try:
              global some_global_var
              some_global_var = "Fuzzing" + str(random.randint(0,1000))  # Add random string
            except NameError:
              pass
            #Introduce a random possibility to return
            if random.random() < 0.0005:
              return
            # Introduce a random chance of raising an exception
            if random.random() < 0.001:
              raise ValueError("Fuzzing Exception")
            # Introduce a random chance of modifying shared_counter with invalid types
            if random.random() < 0.005:
                try:
                    shared_counter = float("inf")
                except ValueError:
                    pass
            if random.random() < 0.005:
                try:
                    shared_counter = "not a number"
                except TypeError:
                    pass
            if random.random() < 0.005:
                try:
                    shared_counter = None
                except TypeError:
                    pass
            # Introduce a random chance of modifying shared_counter to a non-int value
            if random.random() < 0.0005:
                shared_counter = random.random()
    
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
        count = count*2
        # Introduce a potentially JIT-targeted branch
        if random.random() < 0.01:
          count = -1 * count
        # Introduce a potentially JIT-targeted, error prone assignment
        try:
          count = count/ random.uniform(0.1,10)
        except ZeroDivisionError:
          count = 0 # Handle potential zero division
        # Add a random assignment to an invalid type
        if random.random() < 0.05:
            count = "invalid" + str(random.randint(0,1000))  # Add random string
        if random.random() < 0.005:
          count = None
        if random.random() < 0.001:
          raise TypeError("Fuzzing Type Error") # Introduce random TypeError

        #Fuzz with different data types, even if invalid.
        if random.random() < 0.01:
            try:
                count = 1.23
            except ValueError:
                pass
    
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
    
    return "Finished" # Added to ensure a return value


def test_copy_replace():
    class MyObject:
        def __init__(self, val1: int, val2: str):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, val1=None, val2=None):
            if val1 is None:
                return None
            if not isinstance(val1, int):
                return f"Error: val1 must be an integer, got {type(val1)}"  # More informative error
            
            return MyObject(val1, val2 if val2 is not None else self.val2)
    
    myobj = MyObject(1, "hello")
    try:
        replaced_obj = copy.replace(myobj, val1=2)
        return replaced_obj.val1
    except Exception as e:
        return str(e)
    
    #Fuzz with different data types including invalid
    try:
        replaced_obj = copy.replace(myobj, val1=2.5)  # Fuzz with float
        return replaced_obj.val1
    except Exception as e:
        return str(e)

    #More fuzzing:
    try:
      replaced_obj = copy.replace(myobj, val1="not_an_int")
      return replaced_obj.val1
    except Exception as e:
      return str(e)

    try:
        replaced_obj = copy.replace(myobj, val2=10) #Fuzz with val2
        return replaced_obj.val2
    except Exception as e:
        return str(e)
    
    try:
      replaced_obj = copy.replace(myobj, val1=None)  # Include None case
      return replaced_obj.val1
    except Exception as e:
      return str(e)



# Example using ssl.create_default_context()
def test_ssl_context():
    try:
        context = ssl.create_default_context()
        #Simulates connection attempt, no actual connection needed
        context.check_hostname = False  #Important for testing

        invalid_cert = b"invalid" * 1024
        # Add random choices for socket families (AF_INET, AF_INET6)
        sock_type = random.choice([socket.AF_INET, socket.AF_INET6])
        try:
            with context.wrap_socket(socket.socket(sock_type, socket.SOCK_STREAM), server_hostname="invalidhost.com") as s:
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

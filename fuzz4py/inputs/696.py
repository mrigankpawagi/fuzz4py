
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def complex_function(arg1: typing.List[int], arg2: str = None) -> typing.Dict[str, int]:
    """
    This function demonstrates various features potentially impacted by Python 3.13 changes.
    """
    
    if arg2 is None:
        arg2 = ""

    # This loop is likely to be JIT compiled
    results = {}
    for i in range(1000):
        try:
            # Using complex type annotations and possible error scenarios
            # Introduce potential for IndexError and other errors
            idx = random.randint(0, len(arg1) -1)
            results[str(i)] = arg1[idx] * i
            #introduce a float value to cause type error
            results[str(i+1)] = arg1[idx] * random.random()
            # Introduce a None value
            results[str(i+2)] = arg1[idx] * None if i % 2 == 0 else arg1[idx] * 1.2
            # Introduce a custom exception
            if i % 7 == 0:
                raise ValueError("Custom exception at iteration " + str(i))

        except IndexError:
            results["Error"] = "Index out of range" + str(random.random())
            
        except Exception as e:
            results["Exception"] = str(e) + str(random.random()) + str(random.randint(0,100))
            
    return results

def multithreaded_example(data):
    threads = []
    for i in range(10):
        # Introduce random delays and timeouts
        time.sleep(random.random())
        t = threading.Thread(target=complex_function, args=(data,))
        t.daemon = True #important for exiting on main process exit.
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join(timeout = 2) #timeout to avoid indefinite blocking


# Example usage with potentially problematic data (fuzzing with various inputs)
data_len = random.randint(1, 2000)
data = [random.randint(0, 100) for _ in range(data_len)]  # Large list with random values
start_time = time.perf_counter()

# Attempting a race condition (potential issues with GIL)
multithreaded_example(data)

#Using new os timer functions (fuzzing with varied time values)
start = time.monotonic()
time.sleep(random.random())  # Introduce random sleep
end = time.monotonic()
difference = end-start
print(f"Monotonic Timer Difference: {difference}")

end2 = time.time()
start2 = time.time()
diff2 = end2 - start2
print(f"Standard Timer Difference {diff2}")

try:
    #Example with dbm.sqlite3 (new default) - fuzzing with malformed data
    db = dbm.open('mydatabase', 'c')  # 'c' for create mode.
    db['key'] = str(random.randint(0, 1000))
    db.close()
    # Malformed data
    db = dbm.open('mydatabase', 'c')
    db['key'] = b'\x00' * 1024  # Large binary data
    db.close()

except Exception as e:
    print("Error interacting with dbm.sqlite3:", e)


# Example using copy.replace (new replace protocol)
class MyClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b
    
    def __replace__(self, a = None, b = None) -> 'MyClass':
        return MyClass(a if a is not None else self.a, b if b is not None else self.b)

my_object = MyClass(1, "hello")

#Fuzzing with different types for a
try:
    replaced_object = copy.replace(my_object, a = None)
    print(replaced_object.a)
    replaced_object = copy.replace(my_object, a = "string")
    print(replaced_object.a)

except Exception as e:
    print(f"Error replacing object: {e}")
    
#Example with ssl for fuzzing certificates (new stricter defaults)
try:
  context = ssl.create_default_context()
  #  Fuzzing placeholder; would typically use a certificate with issues.
  random_cert = ''.join(random.choices('0123456789abcdef', k=128))
  print(f"Random certificate: {random_cert}")
  context.check_hostname = False  # disable hostname verification for testing
  context.verify_mode = ssl.CERT_NONE  # disable certificate verification for testing

except Exception as e:
  print(f"Error creating SSL context: {e}")


#Example usage with potentially problematic data
data = [1,2,3] * 100 #Large list 
start_time = time.perf_counter()

# Attempting a race condition (potential issues with GIL)
def multithreaded_example2(data):
    threads = []
    for i in range(10):
        t = threading.Thread(target=complex_function, args=(data,))
        t.daemon = True
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join(timeout = 2)

multithreaded_example2(data)

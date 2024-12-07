
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

    results = {}
    for i in range(1000):
        try:
            idx = random.randint(0, len(arg1) - 1)
            results[str(i)] = arg1[idx] * i
            results[str(i + 1)] = arg1[idx] * random.random()
            results[str(i + 2)] = arg1[idx] * (1.2 if i % 2 != 0 else None)
            if i % 7 == 0:
                raise ValueError(f"Custom exception at iteration {i}")
        except IndexError:
            results["Error"] = f"Index out of range {random.random()}"
        except Exception as e:
            results["Exception"] = f"{e} {random.random()} {random.randint(0, 100)}"
    return results

def multithreaded_example(data):
    threads = []
    for i in range(10):
        t = threading.Thread(target=complex_function, args=(data,))
        t.daemon = True
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join(timeout = 2)


# Example usage with potentially problematic data (fuzzing with various inputs)
data_len = random.randint(1, 2000)
data = [random.randint(0, 100) for _ in range(data_len)]  # Large list with random values
start_time = time.perf_counter()

multithreaded_example(data)

#Using new os timer functions (fuzzing with varied time values)
start = time.monotonic()
time.sleep(random.random())
end = time.monotonic()
difference = end - start
print(f"Monotonic Timer Difference: {difference}")

start2 = time.time()
time.sleep(random.random())
end2 = time.time()
diff2 = end2 - start2
print(f"Standard Timer Difference: {diff2}")


try:
    db = dbm.open('mydatabase', 'c')
    db['key'] = str(random.randint(0, 1000))
    db.close()
    db = dbm.open('mydatabase', 'c')
    db['key'] = b'\x00' * 1024
    db.close()
except Exception as e:
    print(f"Error interacting with dbm.sqlite3: {e}")


# Example using copy.replace (new replace protocol)
class MyClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b
    
    def __replace__(self, a = None, b = None) -> 'MyClass':
        return MyClass(a if a is not None else self.a, b if b is not None else self.b)

my_object = MyClass(1, "hello")

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
  random_cert = ''.join(random.choices('0123456789abcdef', k=128))
  print(f"Random certificate: {random_cert}")
  context.check_hostname = False
  context.verify_mode = ssl.CERT_NONE
except Exception as e:
  print(f"Error creating SSL context: {e}")


# Example with potentially problematic data
data = [1, 2, 3] * 100
multithreaded_example(data)

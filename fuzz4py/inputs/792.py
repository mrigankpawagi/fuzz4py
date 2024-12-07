
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import socket  # Import socket

def race_condition_test():
    shared_resource = 0
    lock = threading.Lock()

    def increment():
        nonlocal shared_resource
        with lock:
            shared_resource += 1
            time.sleep(0.01)  # Introduce a delay for potential race

    threads = [threading.Thread(target=increment) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return shared_resource

# Example using the replace protocol (Focus on copy)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, **changes):
        return Point(changes.get('x', self.x), changes.get('y', self.y))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

try:
  # Test DBM with sqlite3
  db = dbm.open('test.db', 'c')
  db['key'] = 'value'
  db.close()
  db = dbm.open('test.db', 'r')
  value = db['key']
  db.close()
  os.remove('test.db')
except Exception as e:
  print(f"Error during DBM test: {e}")

try:
    # Test ssl with different contexts (fuzzing).  Using a dummy socket.
    context = ssl.create_default_context()
    dummy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with context.wrap_socket(
        dummy_socket, server_hostname='example.com'
    ) as s:
        s.connect(('example.com', 443))  # Replace with a target
except Exception as e:
    print(f"Error during SSL test: {e}")


# Test complex type annotations (Focus on scope)
T = typing.TypeVar('T')
def annotated_func(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    return [x for x in data if isinstance(x, int)]

# Example usage for complex types with lambdas
# (Note the scope is a fuzzing target)

my_list: list[int] = annotated_func([1, 2, "a", 4, "b", 5])

# Docstring whitespace fuzzing
def my_function():
    """This is a docstring with varying
       indentation.
       """
    pass

# Example using new timer function (os module)
start_time = time.perf_counter()
# Replace with some computation
result = sum(range(1000000))  # Example computation
end_time = time.perf_counter()
print(f"Computation took {end_time - start_time} seconds")

print(race_condition_test())
print(my_list)

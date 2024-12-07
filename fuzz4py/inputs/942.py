
import threading
import copy
import dbm
import os
import ssl
import time
import typing

def threaded_function(data: int) -> int:
    """
    A simple threaded function that modifies a shared resource.
    """
    global shared_resource
    shared_resource += data
    return shared_resource

def main():
    global shared_resource
    shared_resource = 0
    threads = []
    num_threads = 5
    data_list = [i for i in range(num_threads)]

    for i in data_list:
        thread = threading.Thread(target=threaded_function, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    # Check if the shared resource was properly modified.
    print(f"Final shared resource: {shared_resource}")
    
    # Test copy.replace()
    class Replaceable:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b
        def __replace__(self, a=None, b=None):
            if a is not None: self.a = a
            if b is not None: self.b = b
            return self

    r1 = Replaceable(10, "hello")
    r2 = copy.replace(r1, a=20)
    print(f"r1.a: {r1.a}, r2.a: {r2.a}")

    # Test dbm.sqlite3 (create a dummy database)
    try:
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Error accessing dbm.sqlite3: {e}")

    # Test os.times()
    t = os.times()
    print(f"Time Information: {t}")

    # Test ssl.create_default_context() (simplified)
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error creating SSL context: {e}")

    # Example with complex typing (PEP 696, 702, etc)
    def my_function(arg: typing.Union[int, str]) -> typing.List[int]:
      if isinstance(arg, int):
        return list(range(arg))
      elif isinstance(arg, str):
        return [int(c) for c in arg if c.isdigit()]
      else:
        return []  # Or raise an exception
    
    result = my_function("123abc45")
    print(result)

if __name__ == "__main__":
    main()

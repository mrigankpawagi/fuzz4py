
import threading
import time
import copy
import dbm
import os
import ssl
import typing


def multithreaded_function(arg1: int, arg2: str) -> int:
    """
    A multithreaded function demonstrating the free-threading behavior.
    """
    result = arg1 * len(arg2)
    time.sleep(0.01)  # Introduce a delay to potentially cause race conditions.
    return result

def test_jit_compiler(arg):
    """
    A function to test the JIT compiler, likely to be JIT compiled
    """
    result = 0
    for i in range(1000000):
        result += i * arg
    return result

def main():

    # Free-threading testing
    threads = []
    for i in range(5):
        thread = threading.Thread(target=multithreaded_function, args=(i, str(i)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # JIT compiler test.
    result = test_jit_compiler(5)

    #Docstring whitespace stripping
    docstring_test = """
    Docstring with inconsistent indentation
      for testing
    """

    # Annotation scopes
    annotation = {
        (lambda x: x * 2): [x for x in range(3)] # Using lambda in annotation
    }
      
    # dbm.sqlite3
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        db.close()
    except Exception as e:
        print(f"Error opening/using dbm.sqlite3: {e}")

    # os module timer functions
    try:
        start_time = time.perf_counter()
        os.times()
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time}")
    except Exception as e:
        print(f"Error using os timer functions: {e}")

    # SSL testing.  This is illustrative and does not perform real SSL.
    context = ssl.create_default_context()

    # Example of replace protocol, using copy.
    class MyClass:
        def __init__(self, value):
            self.value = value
        def __replace__(self, value=None):
            return MyClass(value if value else self.value)
    
    obj1 = MyClass(10)
    obj2 = copy.replace(obj1, value=20)
    print(obj1.value)
    print(obj2.value)


if __name__ == "__main__":
    main()


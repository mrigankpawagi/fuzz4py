
import threading
import time
import copy
import os
import ssl
import typing
import dbm
import random
import sys


def my_function(arg1: int, arg2: str = "default") -> str:
    """
    This function demonstrates several Python 3.13 features.
    """
    try:
        # Test Free-threading and GIL with varying sleep times and thread counts
        thread_local_var = 0
        num_threads = random.randint(1, 10)
        sleep_time = random.uniform(0.01, 0.5)
        
        # Introduce potential race condition by directly modifying a global
        global_var = 0
        
        def worker():
            nonlocal thread_local_var
            
            thread_local_var += random.randint(-100, 100)
            time.sleep(sleep_time)
            # Adding a race condition
            global global_var
            global_var += 10
        
        threads = [threading.Thread(target=worker) for _ in range(num_threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Test annotation scopes, complex types with random inputs
        list_len = random.randint(1, 10)
        list1 = [random.randint(-1000, 1000) for _ in range(list_len)]  # Wider range
        list2 = [str(random.randint(-1000, 1000)) for _ in range(list_len)]  # Allow non-numeric strings
        result = [(x, y) for x, y in zip(list1, list2)]
        return f"Free Threading result: {thread_local_var} global_var: {global_var}"
    
    except Exception as e:
        return f"Error: {e}"
    

def main():
  
    # Testing docstring whitespace stripping (doctests) - more comprehensive fuzzing
    def test_docstrings():
        for i in range(3):
           docstring_example(random.randint(1,100), "test string")
           docstring_example(random.randint(1,100), None) # Test with None


    def docstring_example(indentation_level: int, test_str: str):
        indentation = "  " * indentation_level  
        docstring = f"""{indentation}This docstring has varying
{indentation}   whitespace to test doctest parser
           """
        pass

    # Testing copy.replace() with custom classes and various types
    class MyData:
        def __init__(self, val1, val2):
            self.val1 = val1
            self.val2 = val2

        def __replace__(self, **changes):
            if "val1" in changes:
                self.val1 = changes["val1"]
            return copy.copy(self)


    try:  # Add a try-except block
        data = MyData(1, 2)
        keys_to_modify = random.choice([['val1'], ['val1', 'val2'], []]) # allow empty
        new_data = copy.replace(data, **{k: random.randint(-100, 100) for k in keys_to_modify})
        print("copy.replace result:", new_data.val1)
    except Exception as e:
        print(f"copy.replace error: {e}")


    # Fuzzing dbm.sqlite3 with random keys and values including bytes.
    try:
        db = dbm.sqlite3.open("test.db", 'c')
        key = str(random.randint(0, 1000))
        value = str(random.randint(0, 10000))

        db[key] = bytes(value, 'utf-8') # Store as bytes
        db.close()
        db = dbm.sqlite3.open("test.db", 'r')
        if key in db:
            retrieved_value = db[key]
            print("retrieved value", retrieved_value.decode())  # Decode bytes
        db.close()
        os.remove("test.db") # Clean up
    except Exception as e:
        print(f"dbm.sqlite3 error: {e}")


    # Example with typing (complex annotations and type checkers) - more comprehensive
    def annotated_function(arg: typing.List[typing.Tuple[int, str]]) -> None:
        pass
    
    try:
        annotated_function([((random.randint(-100, 100), str(random.randint(-100, 100))), (random.randint(-100, 100), str(random.randint(-100, 100))))])
    except Exception as e:
        print(f"Typing error: {e}")
    

    try:
        print(my_function(random.randint(-100, 100)))
    except Exception as e:
        print(f"my_function error: {e}")


if __name__ == "__main__":
    main()

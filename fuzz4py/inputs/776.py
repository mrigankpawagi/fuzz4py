
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def worker(arg):
    # Simulate some work (potentially JIT-compilable)
    for _ in range(random.randint(10000, 20000)):  # Fuzz input range
        pass
    
    # Access locals() and potential race condition, now with fuzzing
    local_var = arg + random.randint(-100, 100) # Fuzz input
    local_var = random.randint(1, 100) #Fuzz value assignment
    return local_var


def main():
    # Demonstrate free-threading
    threads = []
    for i in range(random.randint(2, 10)): # Fuzz the number of threads
        arg = i
        thread = threading.Thread(target=worker, args=(arg,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    # Using dbm.sqlite3
    db_file = f"mydatabase_{random.randint(0, 100)}.dbm"  # Fuzz filename
    try:
        db = dbm.open(db_file, 'c')
        key = f"key{random.randint(1, 10)}"
        db[key] = f"value{random.randint(1, 100)}" # Fuzz data
        db.close()
    except Exception as e:
        print(f"Error with dbm.open: {e}")


    # Demonstrate replace protocol (potentially custom class)
    class MyClass:
        def __init__(self, val):
            self.val = val
            
        def __replace__(self, val=None):
           if val is not None:
               self.val = val
           return type(self)(self.val)

    myobj = MyClass(random.randint(1, 100))  # Fuzz initial value
    try:
        new_obj = copy.replace(myobj, val=random.randint(1, 100)) # Fuzz replacement value
        print(myobj.val)
        print(new_obj.val)
    except Exception as e:
        print(f"Error with copy.replace: {e}")

    # Interact with os.timer functions (using a placeholder)
    try:
        time_res = os.times()
        print(time_res)  # Print the result for demonstration
        #Adding fuzzing:
        os.nice(random.randint(-20,20)) # Fuzz os.nice()
    except (OSError, AttributeError) as e:
        print(f"Error with os.times(): {e}")

    # Demonstrating SSL connection (placeholder - add fuzzing)
    try:
        context = ssl.create_default_context()
        # Placeholder for connection - add fuzzing
        # ...
        # Example fuzzing the protocol
        protocol = random.choice(["TLSv1", "TLSv1.1","TLSv1.2"])
        if protocol in context.get_protocols(): # Prevent crash if protocol is not available
          context.set_ciphers(f"{protocol}")

        print("SSL context created successfully.")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

    # Docstring with whitespace issues (demonstrating) - fuzzing docstrings
    def my_function():
        """   This function does something with  variable indentation.   """  # Fuzz whitespace
        return 0


    # Complex type annotation - fuzzing types and values
    data_length = random.randint(1, 5)
    data: typing.List[typing.Tuple[str, typing.Union[int, float]]] = []
    for i in range(data_length):
      data.append((f"hello{i}", random.random())) # Using random floats, add string fuzzing
    print(data)


if __name__ == "__main__":
    main()



import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

# Initialize shared counter outside the function
shared_counter = 0

def worker(arg: int):
    # Simulate a long-running task
    time.sleep(arg / 10)
    # Acquire a lock before accessing the shared resource
    global shared_counter
    lock = threading.Lock()
    with lock:
        shared_counter += 1
    return shared_counter


def multi_threaded_example():
    global shared_counter
    shared_counter = 0
    threads = []
    for i in range(random.randint(2, 10)):  # Vary the number of threads
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Final counter value: {shared_counter}")


# Example usage of copy.replace (assuming a custom class)
class MyData:
    def __init__(self, value: int):
        self.value = value

    def __replace__(self, **kwargs):
        return type(self)(value=kwargs.get('value', self.value))

    def __str__(self):
        return str(self.value)


def copy_example():
    data = MyData(random.randint(1, 100)) # Vary the initial value
    try:
        replaced_data = copy.replace(data, value=random.randint(1, 1000)) # Larger range for value
        print(f"Original data: {data}, Replaced data: {replaced_data}")
    except Exception as e:
        print(f"Error in copy_example: {e}")


# Example usage of dbm.sqlite3
def dbm_example():
    try:
        db_name = f"mydatabase_{random.randint(1, 100)}.db" # Vary database name
        d = dbm.sqlite3.open(db_name, 'c')
        key = f"key{random.randint(1, 100)}" # Vary key
        value = f"value{random.randint(1, 100)}"  # Vary value
        d[key] = value
        d.close()
        print(f"Database '{db_name}' created successfully.")
    except Exception as e:
        print(f"Error with dbm operation: {e}")


#Example usage of os timer functions (simulated) - More varied input
def os_timer_example():
    try:
        start_time = time.perf_counter()
        time.sleep(random.uniform(0.5, 5))  # Vary sleep time
        end_time = time.perf_counter()
        print(f"Elapsed time: {end_time - start_time}")
    except Exception as e:
        print(f"Error with os timer example: {e}")


#Fuzzing docstring whitespace:
def indented_docstring():
    """
    This function has
        a docstring
        with
        multiple lines
    """
    return random.randint(1, 1000)  # Return a random integer


if __name__ == "__main__":
    multi_threaded_example()
    copy_example()
    dbm_example()
    os_timer_example()
    print(indented_docstring()) # Test Docstring whitespace
    
    #Example for PEP 667 (locals()): This is just a rudimentary example
    # The real fuzzing would target debugger/introspection tools with different
    # inputs and optimized scope conditions
    
    def test_locals():
        a = 10
        d = {'a': 20}
        b = locals() #Capture locals
        print(b)

    test_locals()

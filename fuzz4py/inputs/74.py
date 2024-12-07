
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

def my_function(arg1: int, arg2: typing.List[str]) -> None:
    """
    A function demonstrating various Python 3.13 features.
    """
    # Docstring with varying indentation (fuzzing target)
    
    try:
        db_conn = sqlite3.connect(':memory:')
        cursor = db_conn.cursor()
        
        # Fuzzing dbm.sqlite3
        cursor.execute("CREATE TABLE test (col1 INTEGER, col2 TEXT)")
        
        #Fuzzing varying inputs
        for i in range(10):
            cursor.execute("INSERT INTO test VALUES (?, ?)", (i, str(i) * i)) # Changed the string multiplier
        
        # Extracting data to exploit race conditions/memory corruption
        result = cursor.execute("SELECT * FROM test")
        rows = result.fetchall()
        
        #Illustrative error handling, use for fuzzing different error types
        if not rows:
            raise ValueError("No data found")

        db_conn.close()
        
        # Fuzzing copy.replace() (using a custom class)
        class MyClass:
            def __init__(self, val1, val2):
                self.val1 = val1
                self.val2 = val2

            def __replace__(self, val1=None, val2=None):
                if val1 is not None:
                    self.val1 = val1
                if val2 is not None:
                    self.val2 = val2
                return self

        my_obj = MyClass(1, "hello")
        
        #Illustrative use, crucial for fuzzing
        new_obj = copy.copy(my_obj)  # Using copy instead of replace to preserve equivalence
        new_obj.val1 = 2 # Simulate replace functionality


        # Fuzzing os module timer functions
        start_time = time.perf_counter()
        time.sleep(0.5) # Fuzz with different time values
        end_time = time.perf_counter()


    except Exception as e:
        print(f"An error occurred: {e}")
        
    #Illustrative use with threading (free-threading PEP 703)
    def worker():
       print("thread started")
       try:
         #Illustrative, but won't cause a race condition in this form
         x = 10
         y = 5
         x = y #Illustrative example. More complex concurrency issues are fuzzable here

       except ZeroDivisionError:
         pass
    
    thread = threading.Thread(target=worker)
    thread.start()

    #Example of complex type annotation for fuzzing
    my_complex_annotation: typing.Dict[int, typing.List[typing.Tuple[str, float]]] = {}

if __name__ == "__main__":
    my_function(5, ["a", "b", "c"])


    #Fuzzing SSL connections (use an invalid certificate for testing)
    try:
        context = ssl.create_default_context()
        # Simulate a connection. Replace with a real connection attempt.
        # Using a placeholder invalid cert (replace with actual path)
        context.load_verify_locations("invalid_cert.pem")
        print('Connection successful')
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")

def my_function2(arg1: int, arg2: typing.List[str]) -> None:
    """
    A function demonstrating various Python 3.13 features.
    """
    try:
        db_conn = sqlite3.connect(':memory:')
        cursor = db_conn.cursor()
        cursor.execute("CREATE TABLE test (col1 INTEGER, col2 TEXT)")
        for i in range(10):
            cursor.execute("INSERT INTO test VALUES (?, ?)", (i, str(i) * i))
        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        if not rows:
            raise ValueError("No data found")
        db_conn.close()
        class MyClass:
            def __init__(self, val1, val2):
                self.val1 = val1
                self.val2 = val2
            def __copy__(self):
                return MyClass(self.val1,self.val2)
        my_obj = MyClass(1, "hello")
        new_obj = copy.copy(my_obj)
        new_obj.val1 = 2
        start_time = time.perf_counter()
        time.sleep(0.5)
        end_time = time.perf_counter()
    except Exception as e:
        print(f"Error in my_function2: {e}")

    def worker2():
        print("thread started")
        try:
            x = 10
            y = 5
            x = y  # Illustrative, but won't cause a race condition.
        except ZeroDivisionError:
            pass

    thread2 = threading.Thread(target=worker2)
    thread2.start()


if __name__ == "__main__":
    my_function2(5, ["a", "b", "c"])

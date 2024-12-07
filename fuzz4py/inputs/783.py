
import threading
import copy
import os
import ssl
import sqlite3
import typing
import time

class MyReplaceableClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __replace__(self, a=None, b=None, **kwargs):
        new_obj = copy.copy(self)
        if a is not None:
            new_obj.a = a
        if b is not None:
            new_obj.b = b
        return new_obj

    def __str__(self):
        return f"My object: {self.a}, {self.b}"


def worker(obj):
    try:
        new_obj = obj.__replace__(a=10, b="bad")  #introduce a potential error
        print(new_obj)
    except Exception as e:
        print(f"Error in worker thread: {e}")


def main():
    obj = MyReplaceableClass(1, 2)
    
    threads = []
    for _ in range(3):
        t = threading.Thread(target=worker, args=(obj,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mytable WHERE id = ?", (1,)) #potential error if the table is missing.
        result = cursor.fetchone()
        if result:
            print("Database entry found:", result)
        else:
            print("Database entry not found.")
    except sqlite3.Error as e:
        print(f"Error in database operation: {e}")
    except Exception as e:
      print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()

    context = ssl.create_default_context()  # Using the default context
    try:
        context.check_hostname = False  # Important: allow self-signed certs for testing
        context.verify_mode = ssl.CERT_NONE  # Important: allow self-signed certs for testing
        
        #fuzzing with invalid cert
        context.verify_mode = ssl.CERT_REQUIRED # introduce a different mode
        context.load_verify_locations(cafile=None) # potential error
        
        print("SSL connection test successful (using default context).")
    except ssl.SSLError as e:
        print(f"Error during SSL connection: {e}")
    except Exception as e:
        print(f"Error in SSL handling: {e}")



    try:
        start_time = os.times()
        print("os.times() result:", start_time)
        #fuzzing os.times() with None
        other_time = os.times(None)  #potential error in this use case
        print("os.times(None) result:", other_time)
    except Exception as e:
        print(f"Error during os.times(): {e}")



    try:
        def annotate_function(input: typing.List[int]) -> typing.List[str]:
            return [str(i) for i in input]

        result = annotate_function([1, 2, 3])
        print(result)
        #fuzzing with invalid input type
        result2 = annotate_function("string")
        print(result2)
    except Exception as e:
        print(f"Error in annotate_function: {e}")


if __name__ == "__main__":
    main()


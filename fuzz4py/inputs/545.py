
import threading
import time
import copy
import ssl
import typing
import os
import dbm
import sys

def multithreaded_function(arg: int, context: ssl.SSLContext) -> str:
    """
    A multithreaded function that demonstrates free-threading and SSL usage.
    """
    
    # Demonstrate the use of locals() in a threaded context
    local_var = 10  
    try:
        result = str(arg) + str(local_var) + " using " + str(context.options)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function for fuzzing multithreading and SSL.
    """
    
    # Fuzzing SSLContext with various options
    ctx = ssl.create_default_context()
    ctx_options =  ctx.options
    try:
        ctx_options =  {'options': 0}
    except Exception as e:
        print(f"Error creating modified SSL context options: {e}")


    threads = []
    for i in range(5):
        thread = threading.Thread(target=multithreaded_function, args=(i, ctx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Fuzzing dbm.sqlite3 (example, with more varied inputs)
    try:
        db_filename = 'mydatabase'
        db_mode = 'c'
        db = dbm.open(db_filename, db_mode)

        
        # Fuzzing with different data types
        db['key1'] = b'value1'  
        db['key2'] = 123  
        db['key3'] = True  
        db.close()

        db = dbm.open(db_filename, 'r')
        key_to_find = 'key1'
        value = db.get(key_to_find)
        
        if value is not None:
          print(f"Found value for key '{key_to_find}': {value}")

        db.close()

    except Exception as e:
        print(f"Error with dbm.sqlite3: {e}")
        
    # Fuzzing os timer functions (with invalid input)
    try:
        start_time = time.monotonic()
        time_to_sleep = float(input("Enter a time to sleep (seconds): "))
        try:
            time.sleep(time_to_sleep)
        except ValueError:
            print("Invalid input. Please enter a number.")
        end_time = time.monotonic()
        print(f"Time taken: {end_time - start_time}")
    except Exception as e:
        print(f"Error with os timers: {e}")

    # Demonstrating copy.replace() (including error handling and various types)
    class MyObject:
        def __init__(self, a: int, b: typing.Union[str, int]):
            self.a = a
            self.b = b

        def __replace__(self, a: int = None, b: typing.Union[str, int] = None) -> 'MyObject':
            return MyObject(a or self.a, b or self.b)


    try:
        obj = MyObject(1, "hello")
        new_obj = copy.replace(obj, b=123) #Try replacing with an int
        print(f"Original object: {obj.a}, {obj.b}")
        print(f"New object: {new_obj.a}, {new_obj.b}")
    except Exception as e:
        print(f"Error with copy.replace(): {e}")

if __name__ == "__main__":
    main()

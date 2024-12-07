
import threading
import time
import copy
import os
import ssl
import typing
import random

def test_replace(obj):
    """
    Tests the replace protocol on a given object.
    """
    try:
        new_obj = copy.replace(obj)
        return new_obj
    except TypeError:
        return None

def threaded_function(input_data):
    """A threaded function demonstrating free-threading."""
    #Simulate some work
    time.sleep(random.uniform(0.05, 0.15))  # Introduce randomness
    
    try:
      result = int(input_data) * 2
      if result > 1000:
        raise OverflowError("Result too large") # Introduce error condition
    except (ValueError, OverflowError) as e:
      print(f"Thread Error: {e}")
      result = -1
    return result



def main():
    """Main function to demonstrate fuzzing scenarios."""
    
    # Test with free threading and varying inputs
    data_list = [1, 2, "abc", 4.5, b'byte', 1001, 100000, -5, 0, "12345", "1000"]
    threads = []
    for data in data_list:
        thread = threading.Thread(target=threaded_function, args=(data,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    # ... (rest of the code is the same)
    # Example usage of copy.replace() (with a custom class)
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __replace__(self, **changes):
            if 'value' in changes:
                return MyClass(changes['value'])
            return None
        
        def __eq__(self, other):
            return self.value == other.value

    obj = MyClass(10)
    new_obj = copy.replace(obj, value=20)
    print(f"Original object: {obj.value}, new object: {new_obj.value if new_obj else 'None'}")


    # Test dbm.sqlite3 (simplified - more robust)
    try:
        import dbm
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        db['key2'] = b'binary data'
        db['key3'] = 123
        db['key4'] = None  # Test None value
        db['key5'] = ''  # Test empty string
        db.close()
        print("Database operation successful.")
    except Exception as e:
        print(f"DBM Error: {e}")

    #Example with os.timer_function (more comprehensive)
    try:
        time_results = os.times()
        print(f"Time results from os.times(): {time_results}")
    except Exception as e:
        print(f"Error in OS timer: {e}")
        
    # Testing ssl
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully")
        # Testing certificate issue (simplified)
        # Avoid relying on external certificate files for fuzzing.
        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        print("SSL context created successfully with client auth")

    except Exception as e:
        print(f"Error creating SSL context: {e}")

if __name__ == "__main__":
    main()


import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

def jit_test_function(input_list):
    """
    A function that likely will be JIT compiled due to the loop.
    """
    result = 0
    for i in range(len(input_list)):
        # Introduce potential JIT optimization issues
        try:
            result += input_list[i] * random.random()  
        except IndexError as e:
            print(f"IndexError in jit_test_function: {e}")
            return -1 # Handle potential errors robustly.
    return result

class MyClass:
    __static_attributes__ = {"some_static": "value"}

    def __init__(self, value):
        self.value = value
        self.my_list = [1, 2, 3, 4, 5]
        self.replaced_value = value  #Simplified to avoid copy.copy

    def __replace__(self, new_value):
        self.replaced_value = new_value
        return self
    def __getitem__(self, index): # Add __getitem__ for fuzzing
        return self.my_list[index]


def test_threading():
    input_data = [1,2,3,4,5]
    input_data.extend([None, True, "a string"]) #Adding more data types
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    try:
        temp_dbm = dbm.open("test_dbm", 'c')
        # Fuzzing with malformed data
        temp_dbm["key"] = str(input_data[0]) + chr(random.randint(0,255)) #Adding random char
        temp_dbm.close()  
    except Exception as e:
      print(f"Error opening/writing to dbm: {e}")

    try:
        myobj = MyClass(10)
        new_obj = copy.replace(myobj, new_value=20)
        print(new_obj.replaced_value)  
        # Fuzz with invalid input
        new_obj2 = copy.replace(myobj, new_value=None)
        print(new_obj2.replaced_value) 
    except Exception as e:
        print(f"Error during replace: {e}")

    try:
      # Fuzz with very large time values.
      print(os.times())
      os.times()
      try:
        os.times(random.randint(0,1000))
      except Exception as e:
        print(f"Error with os.times(random): {e}")
    except Exception as e:
        print(f"Error with os.times(): {e}")
    
    try:
        ctx = ssl.create_default_context()
        # Fuzz with invalid certificate data (string,int).
        ctx.check_hostname = random.choice([True, False])
        print(ctx)
        ssl_data = random.choice([1, 2, 3, "invalid cert"])
        ssl.SSLContext(random.choice([ssl.PROTOCOL_TLS_CLIENT, ssl.PROTOCOL_TLS_SERVER])).load_verify_locations(ssl_data)
    except Exception as e:
        print(f"Error with SSL creation: {e}")

def main():
    test_threading()

if __name__ == "__main__":
    main()

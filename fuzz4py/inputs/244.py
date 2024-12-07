
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def complex_function(arg1: typing.List[int], arg2: typing.Dict[str, float]) -> int:
    """
    A function that demonstrates potential concurrency issues.
    """
    result = 0
    for i in arg1:
        result += i
        time.sleep(0.001)
    for key, value in arg2.items():
        result *= value
    return result


def main():
    # Test with and without the GIL
    data1 = [1, 2, 3, 4, 5]
    data2 = {'a': 2.5, 'b': 3.0, 'c': 1.5}
    
    
    # Free-threading test case, potentially prone to race conditions
    result_thread = []
    for _ in range(5): # Create 5 threads
        thread = threading.Thread(target=complex_function, args=([1,2,3,4,5],{'a':2.5,'b':3.0,'c':1.5}))
        thread.start()
        result_thread.append(thread)

    for thread in result_thread:
      thread.join()


    # Test with a custom class implementing __replace__
    class MyCustomClass(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        def __replace__(self, a=None, b=None):
          return MyCustomClass(a if a is not None else self.a, b if b is not None else self.b)
    
    obj = MyCustomClass(10, 20)
    new_obj = copy.replace(obj, a=30)
    
    # Test dbm.sqlite3
    try:
        db = dbm.open('test.db', 'c')
        db['key'] = 'value'
        value = db['key']
        db.close()
    except Exception as e:
        print(f"dbm error: {e}")

    # Test ssl
    try:
      context = ssl.create_default_context()
      context.check_hostname = False #Bypass verification for fuzzing
      context.verify_mode = ssl.CERT_NONE
    except Exception as e:
        print(f"SSL Error: {e}")


    print("Test completed.")

if __name__ == "__main__":
    main()


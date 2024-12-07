
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(i, data):
    time.sleep(0.1)  # Simulate some work
    data[i] += 1
    return


def test_free_threading():
    data = [0] * 10
    threads = []

    for i in range(10):
        t = threading.Thread(target=worker, args=(i, data))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Data after threading:", data)

    #Test with GIL OFF (not fully possible in a simple example)
    # ... (Add code for testing without GIL if applicable for the specific target interpreter/platform.)


def test_dbm_sqlite3():
    try:
        db = dbm.open('test.db', 'c')  # 'c' for create
        db['key1'] = 'value1'
        db.close()
        
        db = dbm.open('test.db')
        value = db['key1']
        db.close()
        print("DBM access successful:", value)
    except Exception as e:
        print(f"DBM error: {e}")
    finally:
        try:
            os.remove('test.db')
        except OSError:
            pass  # Ignore if file doesn't exist

def test_complex_annotation():
    def inner_func(x: typing.List[int]) -> typing.List[int]:
        return [i * 2 for i in x]
    
    annotation_example :typing.Callable[[typing.List[int]], typing.List[int]] = inner_func
    print(annotation_example([1, 2, 3]))



# Example of testing replace protocol on a custom class
class MyClass:
    def __init__(self, value):
        self.value = value

    def __replace__(self, **kwargs):
        new_obj = copy.copy(self)  # Important to avoid changing original object
        if 'value' in kwargs:
            new_obj.value = kwargs['value']
        return new_obj

obj = MyClass(5)
new_obj = obj.__replace__(value=10)
print(obj.value, new_obj.value)


# Example with ssl.create_default_context (Basic demonstration)
context = ssl.create_default_context()
try:
  print("SSL context created.")
except Exception as e:
    print(f"Error creating SSL context: {e}")

# Test complex functions
test_free_threading()
test_dbm_sqlite3()
test_complex_annotation()


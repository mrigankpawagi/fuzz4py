
import threading
import time
import copy
import dbm
import os
import ssl
import typing


def threaded_function(arg: int) -> int:
    """
    A simple function that takes an integer argument and returns it
    after a delay.
    """
    time.sleep(0.1)
    return arg


def main():
    try:
        # Test free-threading
        threads = []
        for i in range(5):
            thread = threading.Thread(target=threaded_function, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Test dbm.sqlite3
        try:
            db = dbm.open('test.db', 'c')
            db['key1'] = 'value1'
            db.close()
        except Exception as e:
            print(f"Error opening/closing db: {e}")

        # Test os module timer functions
        start_time = time.perf_counter()
        try:
            result = os.times()
            end_time = time.perf_counter()
            print("os.times() execution time:", end_time - start_time)
        except Exception as e:
            print(f"Error using os.times: {e}")


        # Test SSL with default context
        try:
            context = ssl.create_default_context()  # using default context
            # ... (rest of the SSL testing logic, potentially using context) ...
        except Exception as e:
          print(f"Error creating SSL context: {e}")


        # Example of complex type annotations with lambdas and comprehensions
        MyType = typing.List[typing.Union[int, str]]

        def my_func(data: MyType) -> MyType:
           return [x if isinstance(x,int) else str(x) for x in data]

        data = my_func([1,2, '3'])
        print(data)


        # Test copy.replace()
        class MyClass:
            def __init__(self, a: int, b: str):
                self.a = a
                self.b = b

            def __replace__(self, a: int, b: str):  
                return MyClass(a, b)  # this is necessary for copy.replace

        obj = MyClass(1, 'hello')
        try:
            new_obj = copy.replace(obj, a=2, b='world')
            print(new_obj.a, new_obj.b)
        except Exception as e:
            print(f"Error using copy.replace: {e}")



        # testing `__static_attributes__` and `__firstlineno__` (metaprogramming)
        class TestMeta(type):
            __static_attributes__ = {'name': 'test'}

        class MyClass(metaclass=TestMeta):
            def __init__(self):
                self.val = 1

        obj2 = MyClass()
        try:
            print(obj2.__static_attributes__)
        except Exception as e:
            print(f"Error accessing __static_attributes__: {e}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up the DB file (crucial for fuzzing)
        try:
            os.remove('test.db')
        except OSError:
            pass


if __name__ == "__main__":
    main()

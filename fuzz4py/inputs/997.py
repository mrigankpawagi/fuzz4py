
import threading
import time
import copy
import os
import ssl
import typing

def my_threaded_function(arg):
    # Simulate a potentially JIT-compiled hot loop
    result = 0
    for _ in range(100000):
        result += arg

    return result

def main():
    # Demonstrate free-threading
    threads = []
    for i in range(5):
        thread = threading.Thread(target=my_threaded_function, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Test the replace protocol
    class MyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __replace__(self, a=None, b=None):
            return MyClass(a if a is not None else self.a, b if b is not None else self.b)


    obj = MyClass(1,2)
    new_obj = copy.replace(obj, a=3)

    #Test dbm.sqlite3 (simplified)
    try:
      import dbm
      db = dbm.open('test.db', 'c')
      db['key'] = 'value'
      value = db['key']
      db.close()
    except Exception as e:
      print(f"Error in dbm.sqlite3 test: {e}")

    #Test os.times()
    try:
        t = os.times()
        print(t)
    except Exception as e:
        print(f"Error in os.times(): {e}")

    #Test ssl.create_default_context() (simplified)
    try:
        context = ssl.create_default_context()
        print("Default SSL context created successfully")
    except Exception as e:
        print(f"Error in SSL test: {e}")


    #Complex type annotation
    def process_data(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
        results = []
        for item in data:
            if isinstance(item, int):
                results.append(item)
            elif isinstance(item, str):
                try:
                    results.append(int(item))
                except ValueError:
                    pass
        return results
    
    #Example usage
    data = [1, "2", 3, "abc", 4]
    processed_data = process_data(data)
    print(processed_data)


if __name__ == "__main__":
    main()


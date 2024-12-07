
import threading
import time
import copy
import os
import ssl
import dbm
import typing

def test_free_threading(n: int):
    """Test free-threading with a shared resource."""
    shared_resource = 0
    lock = threading.Lock()

    def increment():
        nonlocal shared_resource
        with lock:
            shared_resource += 1
            
    threads = []
    for _ in range(n):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return shared_resource

def test_jit_compiler(n: int):
    """Test JIT compiler with tight loop."""
    result = 0
    for i in range(n):
        result += i * 2
    return result

def test_annotation_scope():
    """Test complex annotation scope."""
    my_function: typing.Callable[[int], int] = lambda x: x * x
    return my_function(5)

def test_os_timer():
    """Test os module timer functions."""
    start_time = time.perf_counter()
    result = os.times()
    end_time = time.perf_counter()
    return end_time - start_time

def test_replace_protocol():
    """Test replace protocol."""
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __replace__(self, value=None):
            return MyClass(value if value is not None else self.value)

    my_object = MyClass(10)
    replaced_object = copy.replace(my_object, value=20)
    return replaced_object.value

def test_dbm_sqlite3():
    """Test dbm.sqlite3."""
    try:
        db = dbm.open('test.db', 'c')  # c for create
        db['key1'] = 'value1'
        result = db['key1']
        db.close()
        return result
    except Exception as e:
        return str(e)


def main():
    try:
        result1 = test_free_threading(5)
        result2 = test_jit_compiler(1000000)
        result3 = test_annotation_scope()
        result4 = test_os_timer()
        result5 = test_replace_protocol()
        result6 = test_dbm_sqlite3()
        print(f"Free threading result: {result1}")
        print(f"JIT compiler result: {result2}")
        print(f"Annotation scope result: {result3}")
        print(f"OS timer result: {result4}")
        print(f"Replace protocol result: {result5}")
        print(f"dbm.sqlite3 result: {result6}")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()

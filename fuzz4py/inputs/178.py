
import threading
import copy
import os
import ssl
import typing
import time

# Fuzzing the free-threading model
def thread_func(data):
    global shared_data
    shared_data += data
    time.sleep(0.01)


def test_free_threading():
    global shared_data
    shared_data = 0
    threads = []
    for i in range(10):
        thread = threading.Thread(target=thread_func, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return shared_data


# Fuzzing JIT compiler (using a loop likely to be JIT-compiled)
def jit_loop(n):
    result = 0
    for i in range(n):
        result += i * 2
    return result


# Fuzzing replace protocol
class MyReplaceableObject:
    def __init__(self, value):
        self.value = value

    def __replace__(self, value=None):
        if value is not None:
            self.value = value
        return self

def test_replace_protocol():
    obj = MyReplaceableObject(10)
    replaced_obj = copy.replace(obj, value=20)
    return replaced_obj.value, obj.value


# Fuzzing docstring whitespace
def my_function():
    """This is a docstring with varying\nindentation levels
    
    """


# Fuzzing complex type annotations
def annotated_function(data: typing.List[typing.Union[int, str, float]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item)
    return result


if __name__ == "__main__":
    try:
        result = test_free_threading()
        print(f"Free-threading result: {result}")

        result = jit_loop(100000)
        print(f"JIT loop result: {result}")

        replace_result, original_result = test_replace_protocol()
        print(f"Replace protocol result: {replace_result}, original: {original_result}")


        annotated_data = [1, 2, "3", 4.5]  # Mix of types
        result = annotated_function(annotated_data)
        print(f"Annotated function result: {result}")


    except Exception as e:
        print(f"An error occurred: {e}")


    # Example demonstrating the new `ssl.create_default_context()`
    try:
        context = ssl.create_default_context()
        # ... further SSL operations ...
        print("SSL context creation successful")
    except Exception as e:
        print(f"An SSL error occurred: {e}")


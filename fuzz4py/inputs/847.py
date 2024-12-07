
import threading
import time
import copy
import os
import ssl
import typing


def my_function(arg1: int, arg2: str, arg3: typing.List[int] = None) -> str:
    """
    This function demonstrates a complex type annotation and free-threading.
    """
    if arg3 is None:
        arg3 = []  # Initialize to avoid errors

    result = ""
    for i in range(len(arg3)):
        try:
            result += str(arg3[i] * arg1)
        except Exception as e:
            result += str(e)  #Handle potential errors for robustness


    return result + arg2


def test_function():
    """Testing function with complex type annotations and threading."""

    #Demonstrate new copy replace functionality.
    my_list = [1, 2, 3]
    new_list = copy.copy(my_list)
    try:
        new_list.replace(0, 10)
    except Exception as e:
        print(f"Error using replace: {e}")


    #Using threading with the free-threading model
    threads = []
    for i in range(5):
        thread = threading.Thread(target=lambda: my_function(i + 1, "hello" + str(i)), args=(i +1, "hello" + str(i), [i, i + 2, i + 5]))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    try:
        # Attempting to access a potentially dynamically allocated variable outside its scope
        # to trigger errors that could occur with the free-threading model.
        print(locals()['result'])
    except KeyError as e:
        print(f"Error in the scope: {e}")




if __name__ == "__main__":
    test_function()

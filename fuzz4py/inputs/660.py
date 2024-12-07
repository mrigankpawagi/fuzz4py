
import threading
import time
import copy
import dbm
import os
import ssl
import random
import typing


def jit_test_function(input_list):
    """
    A function that likely will be JIT compiled due to the loop.
    """
    result = 0
    for i in range(len(input_list)):
        try:
            if input_list[i] is not None:
                if isinstance(input_list[i], (int, float)):  # Added type check
                    result += input_list[i] * random.random()
                else:
                    try:  # Handle non-numeric types
                        result += float(input_list[i]) * random.random()
                    except ValueError:
                        print(f"Non-numeric value encountered: {input_list[i]}")
                        return -1
        except (IndexError, TypeError) as e:
            print(f"Error in jit_test_function: {e}")
            return -1
    return result


class MyClass:
    __static_attributes__ = {"some_static": "value"}

    def __init__(self, value):
        self.value = value
        self.my_list = [1, 2, 3, 4, 5]
        self.replaced_value = value
        self.another_value = "a string"  # Added new attribute
        self.non_numeric_list = ["a", "b", 1, 2]

    def __replace__(self, new_value):
        if new_value is not None and not isinstance(new_value, int):  # Added type check
            try:
                new_value = int(new_value)
            except ValueError:
                print("Invalid replacement value. Must be int.")
                return self
        self.replaced_value = new_value
        return self

    def __getitem__(self, index):
        try:
            return self.my_list[index]
        except IndexError:
            print(f"Error accessing list: Index out of range")
            return None
        
    def __setitem__(self, key, value):  # Added __setitem__
        try:
            self.my_list[key] = value
        except (IndexError, TypeError) as e:
            print(f"Error setting list item: {e}")

    def __str__(self):
        return str(self.__dict__)


def test_threading():
    input_data = [1, 2, 3, 4, 5]
    input_data.extend([None, True, "a string", 10.5, [1, 2], -10, 3.14, object()])  # Added object()
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda x=input_data: jit_test_function(x), args=())
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    try:
        db = dbm.sqlite3.open("test_dbm", 'c')
        db["key"] = str(input_data[0]) + chr(random.randint(0, 255))
        db.close()
    except (dbm.error, TypeError, ValueError) as e:
        print(f"Error with dbm: {e}")

    try:
        myobj = MyClass(10)
        new_obj = copy.copy(myobj)
        new_obj.replaced_value = 20
        print(new_obj.replaced_value)
        new_obj2 = copy.copy(myobj)
        new_obj2 = new_obj2.__replace__("not an int")
        print(new_obj2.replaced_value)
        print(str(myobj))

        # Test __setitem__
        myobj[0] = 100
        print(myobj.my_list)
        
        new_obj3 = copy.deepcopy(myobj)  # Added deep copy test
        new_obj3.replaced_value = 30
        print(new_obj3.replaced_value)  # Output of deep copy test

        # Test with different data types in the list for __replace__ and __getitem__.
        new_obj4 = MyClass(None)
        new_obj4.__replace__(12.34)  # Will handle float.
        print(new_obj4.replaced_value)
        try:
            x = new_obj4[10]  # Accessing an out of bounds index.
        except IndexError as e:
            print(f"Exception caught: {e}")

    except (TypeError, AttributeError, Exception) as e:
        print(f"Error during replace: {e}")

def complex_function(input_data):
    # ... (rest of the function is the same)


def process_data(data_point):
    try:
        time.sleep(data_point / 100 if data_point else 0)
        return data_point
    except (TypeError, ZeroDivisionError, Exception) as e:
        print(f"Error processing data: {e}")
        return None

if __name__ == "__main__":
    test_threading()


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
                result += input_list[i] * random.random()
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

    def __replace__(self, new_value):
        self.replaced_value = new_value
        return self

    def __getitem__(self, index):
        try:
            return self.my_list[index]
        except IndexError:
            print(f"Error accessing list: Index out of range")
            return None


def test_threading():
    input_data = [1, 2, 3, 4, 5]
    input_data.extend([None, True, "a string"])
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
    except (dbm.error, TypeError) as e:
        print(f"Error with dbm: {e}")

    try:
        myobj = MyClass(10)
        new_obj = copy.copy(myobj)
        new_obj.replaced_value = 20
        print(new_obj.replaced_value)
        new_obj2 = copy.copy(myobj)
        new_obj2.replaced_value = None
        print(new_obj2.replaced_value)
    except (TypeError, AttributeError) as e:
        print(f"Error during replace: {e}")

    try:
        print(os.times())
        try:
            os.times()
        except Exception as e:
            print(f"Error with os.times(random): {e}")
    except (TypeError, OSError) as e:
        print(f"Error with os.times(): {e}")

    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = random.choice([True, False])
        print(ctx)
        ssl_data = random.choice([1, 2, 3, "invalid cert", b"invalid cert"])
        try:
            ctx.load_verify_locations(ssl_data)
        except Exception as e:
            print(f"Error loading SSL cert: {e}")
    except Exception as e:
        print(f"Error with SSL creation: {e}")


def complex_function(input_data):
    if not isinstance(input_data, list) or not all(isinstance(x, int) for x in input_data):
        raise TypeError("Input must be a list of integers")
    results = []
    threads = []
    for i in input_data:
        t = threading.Thread(target=process_data, args=(i,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    return results


def process_data(data_point):
    try:
        time.sleep(data_point / 100 if data_point else 0)
        return data_point
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error processing data: {e}")
        return None


def test_dbm(db_name, data):
    try:
        db = dbm.sqlite3.open(db_name, 'c')
        for key, value in data.items():
            try:
                db[key] = str(value)
            except (TypeError, ValueError) as e:
                print(f"Error inserting into DB: {e}")
        db.close()
    except (dbm.error, FileNotFoundError) as e:
        print(f"Error in test_dbm: {e}")


def test_ssl():
    try:
        ctx = ssl.create_default_context()
        return "SSL context created"
    except Exception as e:
        return f"Error creating SSL context: {e}"


def main():
    test_threading()
    try:
        complex_function("not a list")
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")
    try:
        complex_function([1, "a", 3])
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")
    try:
        complex_function(list(range(1000)))
    except Exception as e:
        print(f"Caught exception during large thread test: {e}")
    test_dbm("test.db", {"key1": 1, "key2": "a", "key3": 2})
    print(test_ssl())
    test_dbm("another_db.db", {"key1": 1, "key2": 2})


if __name__ == "__main__":
    main()

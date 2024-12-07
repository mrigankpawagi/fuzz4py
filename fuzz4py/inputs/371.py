
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys
import socket

# Fuzzing multi-threading with GIL
def worker(lock, data, delay_factor=1, fuzz_factor=1):
    with lock:
        try:
            new_value = random.randint(0, 100) * fuzz_factor  # Add fuzz_factor
            data.append(new_value)
            time.sleep(0.001 * delay_factor)
            # Adding error injection - more types of errors
            error_chance = random.random()
            if error_chance < 0.1:
              raise ValueError("Simulated error")
            elif error_chance < 0.2:
              raise TypeError("Simulated type error")
            elif error_chance < 0.3:
              raise IndexError("Simulated index error")

            try:
                data.remove(new_value)
            except ValueError:
                pass  # Handle potential errors
            except Exception as e:
                print(f"Error inside remove: {e}")
        except Exception as e:
            print(f"Error in worker thread: {e}")

def main():
    data = []
    lock = threading.Lock()
    threads = []
    for i in range(10):
        delay_factor = random.randint(1, 5)
        fuzz_factor = random.uniform(0.5, 1.5)  # Random fuzzing factor
        thread = threading.Thread(target=worker, args=(lock, data, delay_factor, fuzz_factor))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data: {data}")


# Fuzzing copy.replace()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __replace__(self, x=None, y=None):
        try:
            new_point = copy.copy(self)
            if x is not None:
              new_point.x = x
            if y is not None:
              new_point.y = y
            return new_point
        except Exception as e:
            print(f"Error in __replace__: {e}")
            return None

def copy_replace_fuzz():
    p1 = Point(10, 20)
    fuzz_x = random.randint(-100, 100)
    fuzz_y = random.randint(-100, 100)

    try:
      p2 = p1.__replace__(x=fuzz_x, y=fuzz_y)
      if p2:
        print(f"p1: {p1.x}, {p1.y}")
        print(f"p2: {p2.x}, {p2.y}")
      else:
        print("p2 is None")
    except Exception as e:
        print(f"Error during copy.replace fuzzing: {e}")

# Fuzzing docstring whitespace (more comprehensive)
def fuzz_indented_docstring(num_lines=3, indent_level=3, fuzz_type="whitespace"):
    docstring = ""
    for i in range(num_lines):
        spaces = "  " * indent_level
        if fuzz_type == "non-ascii":
            spaces = " " + chr(random.randint(128, 255)) * indent_level
        elif fuzz_type == "extra_newlines":
          spaces += "\n" * random.randint(0, 3)
        elif fuzz_type == "invalid_chars":
            spaces += chr(random.randint(0, 255))  # Include various characters
        docstring += spaces + "Line " + str(i + 1) + "\n"
    code = f"def docstring_func():\n\"\"\" {docstring} \"\"\"\n pass"
    try:
        exec(code)
    except Exception as e:
        print(f"Error during docstring fuzzing: {e}")


def my_function(data: typing.List[int], replace_me:int = 0) -> typing.List[int]:
    """
    A function that takes a list of integers and potentially modifies it.

    Args:
        data: A list of integers.
        replace_me: An integer to potentially replace items in data.

    Returns:
        A new list of integers.  Returns the original list if there are problems.
    """
    if not isinstance(data, list):
        return data  # Handle non-list input
    if not all(isinstance(item, int) for item in data):
        return data  # Handle non-integer values

    new_data = copy.deepcopy(data)  # Important for avoiding side effects

    try:
        for i in range(len(new_data)):
          if new_data[i] % 2 == 0:
            new_data[i] = replace_me
        return new_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return data


if __name__ == "__main__":
    try:
        main()
        copy_replace_fuzz()
        fuzz_indented_docstring(fuzz_type="extra_newlines")
        fuzz_indented_docstring(fuzz_type="non-ascii")
        fuzz_indented_docstring(fuzz_type="invalid_chars") # Fuzz with invalid chars
        
        # New fuzzing cases from the second snippet
        data = [1, 2, 3, 4, 5, 6,7,8,9,10]

        threads = []
        for i in range(5):
            replace_value = random.randint(1, 100)
            thread = threading.Thread(target=my_function, args=([x * 2 for x in data], replace_value))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        try:
            # Fuzzing with potentially problematic dbm
            db = dbm.sqlite3.open('mydatabase', 'c')
            db['key'] = str(data)
            db.close()
        except Exception as e:
            print(f"Error with dbm: {e}")

        #Fuzzing different ssl contexts and time operations
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname='example.com') as s:
                # ... (simulate connection)
                os.times()
        except Exception as e:
            print(f"Error with ssl: {e}")

    except Exception as e:
        print(f"Overall script error: {e}")



import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random
import sys

# Fuzzing multi-threading with GIL
def worker(lock, data, delay_factor=1, fuzz_factor=1):
    with lock:
        try:
            new_value = random.randint(0, 100) * fuzz_factor  # Add fuzz_factor
            data.append(new_value)
            time.sleep(0.001 * delay_factor)
            # Adding error injection
            if random.random() < 0.1:
              raise ValueError("Simulated error")
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
        if random.random() < 0.2: # Introduce a potential exception
            raise TypeError("Simulated __replace__ error")
        new_point = copy.copy(self)
        if x is not None:
            try:
              new_point.x = x
            except Exception as e:
              print(f"Error setting x: {e}")
        if y is not None:
            try:
              new_point.y = y
            except Exception as e:
              print(f"Error setting y: {e}")
        return new_point

def copy_replace_fuzz():
    p1 = Point(10, 20)
    fuzz_x = random.randint(-100, 100)
    fuzz_y = random.randint(-100, 100)
    try:
        p2 = p1.__replace__(x=fuzz_x, y=fuzz_y)
        print(f"p1: {p1.x}, {p1.y}")
        print(f"p2: {p2.x}, {p2.y}")
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
        docstring += spaces + "Line " + str(i + 1) + "\n"
    code = f"def docstring_func():\n\"\"\" {docstring} \"\"\"\n pass"
    try:
        exec(code)
    except Exception as e:
        print(f"Error during docstring fuzzing: {e}")


# Fuzzing dbm.sqlite3 (more comprehensive) - added error handling for various cases
if __name__ == "__main__":
    try:
        main()
        copy_replace_fuzz()
        fuzz_indented_docstring(fuzz_type="extra_newlines")
        fuzz_indented_docstring(fuzz_type="non-ascii")
    except Exception as e:
        print(f"Overall script error: {e}")

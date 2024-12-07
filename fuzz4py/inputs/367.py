
import threading
import time
import copy
import dbm
import os
import ssl
import typing
import random

# Fuzzing multi-threading with GIL
def worker(lock, data, delay_factor=1):
    with lock:
        try:
            new_value = random.randint(0, 100)
            data.append(new_value)
            time.sleep(0.001 * delay_factor)
            try:
                data.remove(new_value)
            except ValueError:
                pass  # Handle potential errors
        except Exception as e:
            print(f"Error in worker thread: {e}")


def main():
    data = []
    lock = threading.Lock()
    threads = []
    for i in range(10):
        delay_factor = random.randint(1, 5)
        thread = threading.Thread(target=worker, args=(lock, data, delay_factor))
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
        return copy.copy(self)  # Return a copy instead of modifying in place.  Crucial for preventing accidental mutation
        # return copy.replace(self, x=x if x is not None else self.x, y=y if y is not None else self.y)
        # Avoid __replace__ using original copy.replace, as fuzzing is needed, and we already do that in the correct way


def copy_replace_fuzz():
    p1 = Point(10, 20)
    fuzz_x = random.randint(-100, 100)
    fuzz_y = random.randint(-100, 100)
    try: # Handle Potential Errors
        p2 = p1.__replace__(x=fuzz_x, y=fuzz_y)
        print(f"p1: {p1.x}, {p1.y}")
        print(f"p2: {p2.x}, {p2.y}")
    except Exception as e:
        print(f"Error during copy.replace fuzzing: {e}")

# Fuzzing docstring whitespace
def indented_docstring():
    """
    This docstring
      has some
        indentation.
    """
    pass


def fuzz_indented_docstring(num_lines=3, indent_level=3):
    docstring = ""
    for i in range(num_lines):
        spaces = "  " * indent_level
        docstring += spaces + "Line " + str(i + 1) + "\n"
    code = f"def docstring_func():\n\"\"\" {docstring} \"\"\"\n pass"
    try:
        exec(code)
    except Exception as e:
        print(f"Error during docstring fuzzing: {e}")


# Fuzzing dbm.sqlite3 (more comprehensive)
try:
    db_name = f"test_{random.randint(1, 100)}.db"
    db = dbm.open(db_name, 'c')
    db['key1'] = str(random.randint(1, 100))
    db.close()
    db = dbm.open(db_name, 'r')
    try:
        print(db['key1'])
    except KeyError as e:
        print(f"KeyError during db access: {e}")
    except Exception as e:
        print(f"Unexpected Error during dbm access: {e}")
    db.close()
    os.remove(db_name)

except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")



if __name__ == "__main__":
    main()
    copy_replace_fuzz()
    fuzz_indented_docstring()

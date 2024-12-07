
import threading
import time
import copy
import dbm
import os
import ssl
import sqlite3
import typing
import random
import sys

def jit_test_function(input_list):
    """A function likely to be JIT compiled."""
    result = 0
    for item in input_list:
        result += item * 2
    return result

def test_threading(data):
    """Test multi-threading with a focus on race conditions."""
    lock = threading.Lock()
    shared_var = 0

    def worker(local_data):  # Using a local copy of data
        nonlocal shared_var
        with lock:
            for i in local_data:
                shared_var += i
                # Introduce potential race condition (simplified)
                time.sleep(random.random() * 0.01)  # Random delay
    
    threads = []
    for i in range(5):
        # Create a copy of the data for each thread
        local_data = data[:]  # Crucial for preventing race conditions
        t = threading.Thread(target=worker, args=(local_data,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return shared_var

def test_copy_replace(obj):
    """Test copy.replace()."""
    if hasattr(obj, '__replace__'):
        try:  # Add try-except for robustness
          replaced_obj = copy.replace(obj, attr1=random.randint(1, 100), attr2=str(random.randint(1,1000))) # Varying inputs
          return replaced_obj
        except Exception as e:
          return f"Error in replace: {e}"
    return None

def test_dbm_sqlite(data, key):
    """Test the dbm.sqlite3 module."""
    try:
        db = dbm.open('mydatabase', 'c')
        db[key] = data
        # Fuzz with different data types
        return db[key]
    except dbm.error as e:
        return f"DBM Error: {e}"
    except Exception as e:
        return f"General Error: {e}"
    finally:
        if 'db' in locals() and isinstance(db, dbm.open):
            try:
                db.close()
            except Exception as e:
                return f"Error closing DB: {e}"
  
def worker_sqlite(db_conn, lock, data):
    with lock:
        cursor = db_conn.cursor()
        try:
            # Fuzz with various data types (including None)
            cursor.execute("INSERT INTO mytable VALUES (?, ?)", (random.randint(1, 100), data if data is not None else 'NULL',))
            db_conn.commit()
        except sqlite3.Error as e:
            print(f"Error in worker: {e}")


def main():
    # Example data for fuzzing.  More diverse inputs are needed
    data = [random.randint(-100, 100) for _ in range(20)]
    result = test_threading(data)
    print(f"Threading result: {result}")
    
    # Example of fuzzing copy.replace()
    class MyClass:
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2
        def __replace__(self, attr1=None, attr2=None):
            return MyClass(attr1 if attr1 is not None else self.attr1, attr2 if attr2 is not None else self.attr2)

    obj = MyClass(10, "hello")
    replaced_obj = test_copy_replace(obj)
    print(f"Copy Replace result: {replaced_obj}")
    
    # Fuzzing for dbm.sqlite3. (combined)
    dbm_data = str(random.randint(1, 10000))
    dbm_key = str(random.randint(1, 10000))
    dbm_result = test_dbm_sqlite(dbm_data, dbm_key)
    print(f"dbm result: {dbm_result}")


    # Second function (sqlite3 with free-threading)
    try:
        db_conn = sqlite3.connect('mydatabase.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return

    cursor = db_conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mytable (
            id INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')

    lock = threading.Lock()
    data_list = [str(random.randint(1, 1000)) for i in range(10)] # More varied string data
    data_list.extend([None] * 5) # Add some None values for fuzzing

    threads = []
    for data in data_list:
        thread = threading.Thread(target=worker_sqlite, args=(db_conn, lock, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All sqlite threads finished.")
    cursor.close()
    db_conn.close()

if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import sqlite3
import typing
import random

def race_condition_example(data: int, lock: threading.Lock) -> None:
    """
    This function demonstrates a potential race condition.
    """
    lock.acquire()
    try:
        global_data = data * (random.random() * 10)  # Introducing a variable multiplier, potentially causing unexpected results
        time.sleep(0.1 + data * 0.01 + random.random() * 0.05) # introduce random delay variations
        print(f"Thread {threading.get_ident()} calculated: {global_data}")
    except Exception as e:
        print(f"Error in race_condition_example: {e}")

    finally:
        lock.release()


def main():
    global_data = 10
    lock = threading.Lock()
    
    threads = []
    for i in range(5):
        try:
          thread = threading.Thread(target=race_condition_example, args=(global_data + random.randint(-5, 5), lock)) #Random variation in input
          threads.append(thread)
          thread.start()
        except Exception as e:
          print(f"Error creating/starting thread: {e}")
        
    for thread in threads:
        try:
          thread.join()
        except Exception as e:
          print(f"Error joining thread: {e}")

    
    try:
        class MyData:
            def __init__(self, value: int = 0):
                self.value = value

            def __replace__(self, **kwargs):
                if "value" in kwargs:
                    try:
                        new_value = int(kwargs["value"])
                        if new_value < 0 or new_value > 100:  # More strict constraint
                            raise ValueError("Value out of range")  
                        return type(self)(new_value)
                    except (ValueError, TypeError) as e:
                        print(f"Error in __replace__: {e}")
                        return self
        
        data = MyData(10)
        try:
            #fuzzing with a list as input (and non-integer)
            replaced_data = copy.replace(data, value=random.randint(0, 101)) # Fuzz with integer in range
            replaced_data2 = copy.replace(data, value="invalid") #Fuzz with non-integer
            replaced_data3 = copy.replace(data, value=None) #Fuzz with None
            assert replaced_data.value == 20  # Assert for a valid input
            print("copy.replace() successful (Integer)")
        except (AssertionError, Exception) as e:
            print(f"copy.replace() error (Integer): {e}")


        try:
             replaced_data = copy.replace(data, value="invalid") #Fuzz with non-integer
             assert replaced_data.value == 10 #Assert for a non-valid input
             print("copy.replace() successful (invalid input)")
        except (AssertionError, Exception) as e:
            print(f"copy.replace() error (invalid input): {e}")

    except Exception as e:
        print(f"copy.replace() error: {e}")
        


    #  Simple database interaction (using dbm.sqlite3)
    try:
        db = sqlite3.connect(":memory:")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, value TEXT)")
        # Malformed data insertion
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", (random.randint(0, 1000),)) # Inserting random integer
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", (random.random(),))  #Inserting float
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", (None,)) #insert None
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", (b'binary_data',)) #inserting bytes
        cursor.execute("INSERT INTO mytable (value) VALUES (?)", ('string with single quote\'s',))

        result = cursor.execute("SELECT value FROM mytable").fetchall()
        for row in result:
            try:
              print(f"Database data: {row[0]}")
            except Exception as e:
              print(f"Error printing database data: {e}")

        db.close()
    except Exception as e:
        print(f"Database interaction error: {e}")



    try:
        # Fuzzing the os module timer function
        try:
            time_taken = os.times()[random.randint(-10, 10)]  # Random index access (more negative values!)
            print(f"Time taken: {time_taken}")
        except IndexError as e:
            print(f"Error accessing os.times(): {e}")
        except Exception as e:
            print(f"Unknown error accessing os.times(): {e}")
        
        # fuzzing with large values
        try:
            time.sleep(random.random() * 10000)  # Sleep for a very long time
            print("Sleep successful.")
        except Exception as e:
            print(f"Error in sleep function: {e}")
    except Exception as e:
        print(f"Time measurement error: {e}")


if __name__ == "__main__":
    main()


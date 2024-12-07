
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

# Fuzzing example focusing on free-threading and dbm.sqlite3
# This example attempts to create a race condition using free-threading and sqlite3

def worker(db_conn, lock, data):
    with lock:
        cursor = db_conn.cursor()
        try:
            cursor.execute("INSERT INTO mytable VALUES (?)", (data,))
            db_conn.commit()
        except sqlite3.Error as e:
            print(f"Error in worker: {e}")


def main():
    # Establish a database connection
    try:
        db_conn = sqlite3.connect('mydatabase.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return


    # Create a table if it doesn't exist.
    cursor = db_conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mytable (
            id INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')

    lock = threading.Lock()


    threads = []
    data_list = ['fuzz' + str(i) for i in range(10)]

    for data in data_list:
        thread = threading.Thread(target=worker, args=(db_conn, lock, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")

    cursor.close()
    db_conn.close()




if __name__ == "__main__":
    main()


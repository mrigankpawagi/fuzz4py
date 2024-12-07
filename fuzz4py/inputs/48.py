
import threading
import time
import os
import copy
import ssl
import dbm
import typing

def worker(i):
    try:
        # Simulate some work, potentially interacting with C extensions
        time.sleep(0.1) 
        return i * 2
    except Exception as e:
        print(f"Error in thread {i}: {e}")
        return None

def multithreaded_example():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    results = []
    for thread in threads:
        thread.join()
        # Potential race condition: accessing shared memory without locks
        try:
          result = thread.result()  
          if result:  
              results.append(result)
        except Exception as e:
           print(f"Error retrieving thread result: {e}")
    return results

def test_complex_annotations():
    # Testing annotation scopes and type checking
    Point = typing.NamedTuple("Point", [("x", int), ("y", int)])
    def add_points(p1: Point, p2: Point) -> Point:
        return Point(p1.x + p2.x, p1.y + p2.y)
        
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    return add_points(p1, p2)

def test_dbm_sqlite():
    try:
        db = dbm.open('test.db', 'c')
        db['key1'] = 'value1'
        db.close()
        return True
    except Exception as e:
        print(f"Error in dbm.sqlite3: {e}")
        return False

def test_ssl_connection():
    try:
      context = ssl.create_default_context()
      # Replace with appropriate certificate paths in a fuzzing scenario
      with context.wrap_socket(socket.socket(), server_hostname='localhost') as s:
          s.connect(('localhost', 443))
          return True
    except Exception as e:
        print(f"SSL connection error: {e}")
        return False

if __name__ == "__main__":
    results = multithreaded_example()
    print(f"Multithreaded results: {results}")
    
    complex_annotation_result = test_complex_annotations()
    print(f"Complex annotation result: {complex_annotation_result}")
    
    dbm_result = test_dbm_sqlite()
    print(f"dbm.sqlite3 result: {dbm_result}")
    
    import socket 
    ssl_result = test_ssl_connection()
    print(f"SSL connection result: {ssl_result}")

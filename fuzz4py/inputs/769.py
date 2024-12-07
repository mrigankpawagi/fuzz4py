
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def worker(arg: int, lock: threading.Lock):
    lock.acquire()
    try:
        time.sleep(arg)  # Potential race condition
        print(f"Thread {threading.current_thread().name} finished with arg: {arg}")
    finally:
        lock.release()


def main():
    lock = threading.Lock()
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, lock))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    # Example with copy.replace()
    class MyObject:
        def __init__(self, value):
            self.value = value

        def __replace__(self, value=None):
            return MyObject(value or self.value)

    obj = MyObject(5)
    new_obj = copy.replace(obj)  # Testing replace protocol
    print(new_obj.value)
    
    # Example with dbm.sqlite3
    try:
        db = dbm.open('mydatabase', 'c')
        db['key'] = 'value'
        value = db['key']
        print(value)
        db.close()
    except Exception as e:
        print(f"Error with dbm: {e}")


    try:
        # Example with os.times()
        t = os.times()
        print(f"CPU times: {t}")
    except Exception as e:
        print(f"Error with os.times(): {e}")
    

    # Testing ssl.create_default_context()
    try:
        context = ssl.create_default_context()
        print("SSL context created successfully.")
    except Exception as e:
        print(f"Error with ssl.create_default_context(): {e}")



    # Complex type annotation example
    def annotated_function(arg: typing.List[typing.Tuple[int, str]]) -> typing.Dict[str, int]:
        return {x: x[0] for x in arg}
    result = annotated_function([(1, 'a'), (2, 'b')])
    print(result)


if __name__ == "__main__":
    main()

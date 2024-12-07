
import threading
import time
import copy
import ssl
import dbm
import os
import typing

def worker(arg: int):
    # Simulate a potentially JIT-compiled hot loop
    for i in range(1000000):
        if arg % 2 == 0:
            pass
        else:
            time.sleep(0.001)

    return arg

def main():
    try:
        # Test free threading and GIL
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            
        # Test os module timer functions.  Potentially race-condition prone.
        start = time.perf_counter()
        result = os.times()
        end = time.perf_counter()
        print("os.times() took:", end - start)

        #Test dbm.sqlite3
        db = dbm.open('mydatabase', 'c')
        db['key1'] = 'value1'
        value = db['key1']
        db.close()
        
        #Test copy module with replace protocol
        class MyClass:
            def __init__(self, val: int):
                self.val = val

            def __replace__(self, **kwargs):
                return copy.replace(self, **kwargs)

        obj = MyClass(10)
        new_obj = copy.replace(obj, val=20)

        #Test SSL connections
        context = ssl.create_default_context()
        with context.wrap_socket(
            socket.socket(), server_hostname='example.com'
        ) as s:
            s.connect(('example.com', 443))


    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()

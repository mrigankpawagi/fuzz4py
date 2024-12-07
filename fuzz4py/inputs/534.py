
import threading
import copy
import os
import ssl
import typing
import dbm

def worker(data: typing.List[int], lock):
    try:
        for i in data:
            # Potential race condition, intentionally not using copy.deepcopy
            temp_data = [x for x in data]  
            lock.acquire()
            try:
                dbm.open("test.db", "c").close() # Use dbm
            except Exception as e:
                print(f"Error in dbm: {e}")
                
            lock.release()

    except Exception as e:
        print(f"Error in worker: {e}")

def main():
    data = list(range(10))
    lock = threading.Lock()
    threads = []
    
    for i in range(5):
        thread = threading.Thread(target=worker, args=(data, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    

    # Example using copy.replace (and relying on its behavior)
    obj = {"a": 1, "b": 2}
    new_obj = copy.replace(obj, a=42)
    
    # Example of using os.times()
    t = os.times()

    # Example of ssl.create_default_context
    context = ssl.create_default_context()


if __name__ == "__main__":
    main()




import threading
import time
import copy
import dbm
import ssl
import typing

def worker(data, lock):
    try:
        lock.acquire()
        # Simulate a potentially long operation
        time.sleep(0.1)  # Simulate work
        # Simulate data modification
        data.append(data[-1] + 1)

        # Attempt to use sqlite3 backend
        db = dbm.open('mydatabase', 'c')  
        db['key'] = str(data[-1]) 
        db.close()


    except Exception as e:
        print(f"Error in worker thread: {e}")
    finally:
        lock.release()


def main():
    data = [1]
    lock = threading.Lock()

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(copy.deepcopy(data), lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final data: {data}")


    #Testing SSL - Likely would be a part of a larger program
    try:
        context = ssl.create_default_context()
        #replace with certificate handling
        with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
            s.connect(('example.com', 443)) 
            print('Connection established with example.com')
    except Exception as e:
        print("Error during SSL connection:", e)

    #Test the new replace protocol for copy module 
    class MyData(typing.NamedTuple):
        x: int
        y: str
    d = MyData(1, 'hello')
    d2 = copy.replace(d, x=2)
    print(d)
    print(d2)

if __name__ == "__main__":
    main()


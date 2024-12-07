
import threading
import copy
import dbm
import os
import ssl
import time
import typing

def worker(data: typing.List[int], lock: threading.Lock):
    """
    A worker thread that modifies a shared list.
    """
    for i in data:
        lock.acquire()
        try:
          # Potential race condition here with the JIT compiler
          data[i] = data[i] + i  # this operation can trigger JIT compilation
        finally:
          lock.release()
          


def main():
    data = list(range(100))
    lock = threading.Lock()
    threads = []
    
    #Creating threads with a wide range of data
    for i in range(20):
        threads.append(threading.Thread(target=worker, args=([i*2,i*3,i*5], lock))) # Fuzzing with different input types

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Data after modification:", data)


if __name__ == "__main__":
    main()



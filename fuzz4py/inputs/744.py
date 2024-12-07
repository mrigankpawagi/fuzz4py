
import threading
import copy
import os
import ssl
import typing
import dbm
import time
import random


def complex_operation(data: typing.List[int], replace_flag: bool = False) -> typing.List[int]:
    """
    A complex operation with potential for race conditions.
    """
    
    if replace_flag:
        try:
            data_copy = data[:]  # Create a shallow copy
            data_copy.append(random.randint(1, 1000))
            
            data = [x + random.randint(-10, 10) for x in data_copy]  # Example modification

            if random.randint(1, 100) % 2 == 0 and random.randint(1, 100) % 2 == 0:
                raise ValueError("Error during replacement")
            
        except Exception as e:
            return [str(e)]
    
    try:
        result = sum(data)
        thread_local_value = threading.local()
        thread_local_value.value = random.randint(-100, 100)

        with threading.Lock():
            result += thread_local_value.value
            if random.random() < 0.2:
                raise ZeroDivisionError("Simulated zero division error")
        if random.random() < 0.1:
          raise ValueError("Simulated error")
        return [result]
    except Exception as e:
        return [str(e)]


def main():
    data = [1, 2, 3, 4, 5]
    
    results = complex_operation(data, True)
    print(f"Results with replace: {results}")
    
    results = complex_operation(data, False)
    print(f"Results without replace: {results}")
    
    data2 = list(range(random.randint(1000, 10000)))
    results2 = complex_operation(data2, True)
    print(f"Results with large data and replace: {results2}")


    try:
        db_key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        db_value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20))
        db = dbm.open('test.db', 'c')
        if random.random() < 0.2:
            raise ValueError("Database error")
        db[db_key] = db_value
        db.close()
        
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            if random.random() < 0.5:
                raise ConnectionRefusedError("Simulated connection refused")
            
            # Placeholder for actual SSL connection
            
        except Exception as e:
            print(f"SSL Error: {e}")
        
        delay = random.uniform(0.1, 5)
        start_time = time.perf_counter()
        if random.random() < 0.2:
            raise IOError("Simulated I/O error during sleep")
        time.sleep(delay)
        end_time = time.perf_counter()
        print(f"Elapsed time: {end_time - start_time}")
        
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()

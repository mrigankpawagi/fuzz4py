
import threading
import copy
import os
import ssl
import typing
import dbm
import time


def complex_operation(data: typing.List[int], replace_flag: bool = False) -> typing.List[int]:
    """
    A complex operation with potential for race conditions.
    """
    
    if replace_flag:
        #Using copy.replace()
        data = data[:]  # Create a shallow copy
        data.append(100)
        try:
            data = [x if x != 100 else 200 for x in data]  #replace
        except:
            return [0]
            
    try:
        result = sum(data)
        #Simulate a C extension that might cause thread issues.
        thread_local_value = threading.local()
        thread_local_value.value = 2

        with threading.Lock():
            result += thread_local_value.value
    except Exception as e:
        return [0]
    return [result]


def main():
    # Fuzzing different inputs and replace flag
    data = [1,2,3,4,5]
    
    #Test copy.replace()
    results = complex_operation(data, True)
    print(f"Results with replace: {results}")
    
    #Test without replace flag (default behavior)
    results = complex_operation(data, False)
    print(f"Results without replace: {results}")
    
    #Test large data
    data2 = list(range(10000))
    results2 = complex_operation(data2, True)
    print(f"Results with large data and replace: {results2}")


    try:
        # Test dbm.sqlite3
        db = dbm.open('test.db', 'c')  # Create a new database
        db['key1'] = 'value1'
        db.close()
        
        #Test ssl
        context = ssl.create_default_context()
        
        #Test os module timer
        start_time = time.perf_counter()
        time.sleep(2) #Example use case of timer
        end_time = time.perf_counter()
        print(f"Elapsed time: {end_time - start_time}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

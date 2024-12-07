
import threading
import copy
import os
import ssl
import typing
import dbm

def multithreaded_function(data: typing.List[int]) -> typing.List[int]:
    """
    A multithreaded function that potentially modifies data.
    """
    results = []
    threads = []
    
    for i in data:
        thread = threading.Thread(target=process_item, args=(i, results))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

    return results

def process_item(item: int, results: typing.List[int]) -> None:
    """
    Simulates a thread-safe operation, but has potential race condition.
    """
    try:
        # Simulate some operation with potential failure
        if item % 2 == 0:
            raise ValueError("Even numbers cause error")
        
        results.append(item * 2)
    except ValueError as e:
        print(f"Error in thread: {e}")

def main():
    # Test data with various types.
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
      results = multithreaded_function(data)
      print(f"Results: {results}")
    except Exception as e:
        print(f"Main function failed: {e}")
    
    # Testing with complex typing (PEP 696, 702, 705, 742)
    complex_data: typing.List[typing.Tuple[int, str]] = [(1, "a"), (2, "b")]
    try:
      _ = multithreaded_function(list(map(lambda x: x[0], complex_data))) #accessing only integer part
    except Exception as e:
        print(f"Complex data processing failed: {e}")

    # Example using dbm.sqlite3 (PEP 475)
    try:
        db = dbm.open('mydatabase', 'c') # Open a dbm in creation mode
        db['key1'] = 'value1'
        db.close()
    except Exception as e:
        print(f"Database operation failed: {e}")

    #Example using ssl (PEP 487) and os.
    try:
        context = ssl.create_default_context()
        #Simulate a connection.  Replace with actual SSL usage.
        context.check_hostname = False
        _ = context.get_ca_certs()
        print(os.getcwd()) # testing os module
        print(os.times()) # testing os module, and potential for very long running processes on systems with multiple cores
    except Exception as e:
        print(f"SSL/os operations failed: {e}")
    
if __name__ == "__main__":
    main()


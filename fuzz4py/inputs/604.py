
import threading
import time
import copy
import os
import ssl
import typing

def worker(arg: int, context: ssl.SSLContext) -> str:
    """
    This function simulates a worker thread doing something.

    Args:
        arg: An integer argument.
        context: An SSL context.

    Returns:
        A string representing the result.
    """

    # Simulate some work
    time.sleep(arg % 2)
    
    # Test dbm operations (if available)
    try:
        import dbm
        db = dbm.open('test.dbm', 'c')
        db[str(arg)] = str(arg * 2)
        db.close()
    except ImportError:
        pass

    # Test copy.replace()
    try:
        data = copy.copy([arg, "data"])
        new_data = copy.replace(data, 0, "new_data")
        return str(new_data)
    except Exception as e:
        return f"Error in copy.replace: {e}"
    

def main():
    """
    Main function for demonstration.
    """
    args = [1, 2, 3, 4, 5]
    threads = []
    ctx = ssl.create_default_context()  # Create an SSL context
    for arg in args:
        thread = threading.Thread(target=worker, args=(arg, ctx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for each thread to finish

    try:
        import dbm
        db = dbm.open('test.dbm', 'r')
        for key in db:
            print(f"Key: {key}, Value: {db[key]}")
        db.close()
        try:
            os.remove('test.dbm') #Clean up
        except OSError as e:
            print(f"Error removing dbm file: {e}")  # Catch potential errors


    except ImportError:
        print("dbm module not available")
    except FileNotFoundError:
        print("dbm file not found")

if __name__ == "__main__":
    main()

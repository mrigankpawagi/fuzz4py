
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def complex_function(data: typing.List[int], sleep_time: float = 0.1) -> typing.List[int]:
    """
    A function that performs some operations on a list, potentially causing race conditions.
    """
    try:
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        
        # Simulate some time-consuming operation
        time.sleep(sleep_time)

        results = []
        for item in data:
            results.append(item * 2)
        
        # Simulate a race condition (potential problem to find)
        # This is NOT a good way to simulate race conditions, but demonstrates the idea.
        results[0] = -1  # This is highly dependent on the interpreter's threading model
        return results
    except TypeError as e:
        print(f"Error in complex_function: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error in complex_function: {e}")
        raise

# Example usage (potentially triggering JIT and free-threading)

data = list(range(10))


threads = []
for i in range(5):
    thread = threading.Thread(target=complex_function, args=(copy.copy(data),)) # Important copy to avoid shared state errors.
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


# Example with a potentially problematic type annotation (fuzz testing)
def problematic_annotation(a: typing.Union[int, str, complex]) -> typing.Union[int, str, complex]:
    return a



# Example using the new dbm module (fuzz testing)

try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = 'value1'
    db.close()
    
    db = dbm.open('mydatabase', 'r')
    value = db['key1']
    db.close()

except Exception as e:
    print(f"Error in dbm example: {e}")

# Example using os module timer functions (fuzz testing)
try:
    start_time = os.times()[4]
    time.sleep(0.2)
    end_time = os.times()[4]
    print(f"Time taken: {end_time - start_time}")
except Exception as e:
    print(f"Error in os module example: {e}")

# Example using ssl (fuzz testing)
# This example is incomplete and needs a certificate, but shows the idea.
try:
    context = ssl.create_default_context()
    # ... (Code to establish a connection with a certificate) ...
except Exception as e:
    print(f"Error in ssl example: {e}")



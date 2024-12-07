
import threading
import copy
import dbm
import os
import ssl
import typing
import time

# Fuzzing target: copy.replace() with custom class
class MyObject:
    def __init__(self, value):
        self.value = value

    def __replace__(self, **kwargs):
        if 'value' in kwargs:
            self.value = kwargs['value']
        return self


# Fuzzing target: dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = b'value1'
    db['key2'] = b'\x00\x01\x02' #fuzz with a malformed key
    db.close()
    db = dbm.open('mydatabase', 'r')
    print(db['key1'].decode())
    db.close()
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")



# Fuzzing target: os.times() and threading
def worker():
	try:
		start_time = time.perf_counter()
		result = os.times()
		end_time = time.perf_counter()
		print(f"Worker thread: {result}, duration: {end_time-start_time}")
	except Exception as e:
		print(f"Error in worker thread: {e}")

threads = []
for _ in range(5):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Fuzzing target: complex type annotations
def process_data(data: typing.List[typing.Union[int, str, MyObject]]) -> typing.List[int]:
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, str):
            try:
                result.append(int(item))
            except ValueError:
                pass  # Ignore non-integer strings
        elif isinstance(item, MyObject):
            if isinstance(item.value, int):
                result.append(item.value)
    return result

my_data = [1, 2, '3', 4, 'abc', MyObject(5), MyObject('6')]
processed_data = process_data(my_data)
print(processed_data)


# Fuzzing target: ssl
try:
  context = ssl.create_default_context()
  print("Default SSL context created successfully.")
except Exception as e:
  print(f"Error creating SSL context: {e}")


#Example of using __replace__()
obj = MyObject(10)
new_obj = copy.replace(obj, value=20)
print(obj.value) # Original object remains unchanged
print(new_obj.value) # The new object has the updated value


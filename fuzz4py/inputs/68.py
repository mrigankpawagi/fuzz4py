
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

	def __repr__(self):
		return f"MyObject({self.value})"


# Fuzzing target: dbm.sqlite3
try:
    db = dbm.open('mydatabase', 'c')
    db['key1'] = b'value1'
    db['key2'] = b'\x00\x01\x02' #fuzz with a malformed key
	db['key3'] = b'\x00' * 1024  #fuzz with a very large key
    db.close()
    db = dbm.open('mydatabase', 'r')
    print(db['key1'].decode())
    try:
        print(db['key4'].decode()) #test for non-existent key
    except KeyError as e:
        print(f"KeyError: {e}")
    db.close()
    os.remove('mydatabase')  #Clean up
except Exception as e:
    print(f"Error with dbm.sqlite3: {e}")



# Fuzzing target: os.times() and threading
def worker():
	try:
		start_time = time.perf_counter()
		result = os.times()
		end_time = time.perf_counter()
		print(f"Worker thread: {result}, duration: {end_time-start_time}")
		#introducing a potential race condition
		time.sleep(0.01)

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
				#Adding more sophisticated error handling
                print(f"Warning: Non-integer string '{item}' encountered.")
                result.append(-1)  # Add a marker for error
        elif isinstance(item, MyObject):
            if isinstance(item.value, (int,float)):
                result.append(item.value)
			#Added a check for potential TypeError
            else:
                print(f"Warning: MyObject value '{item.value}' is not an int or float.")
                result.append(-2)  # More specific error marker


    return result

my_data = [1, 2, '3', 4, 'abc', MyObject(5), MyObject(6.7),MyObject("notanumber")]
processed_data = process_data(my_data)
print(processed_data)


# Fuzzing target: ssl
try:
  context = ssl.create_default_context()
  #adding a test with a dummy cert for fuzzing
  context.load_verify_locations(cafile="dummy_cert.pem")  #replace with dummy certificate path
  print("Default SSL context created successfully.")
except Exception as e:
  print(f"Error creating SSL context: {e}")


#Example of using __replace__()
obj = MyObject(10)
new_obj = copy.replace(obj, value=20)
print(obj) # Original object remains unchanged
print(new_obj) # The new object has the updated value
print(copy.deepcopy(obj)) # demonstrate another copy method
obj.value = 100
print(new_obj.value) #Check if copy was truly independent

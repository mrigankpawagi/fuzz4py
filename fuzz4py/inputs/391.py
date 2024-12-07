
import threading
import copy
import os
import time
import ssl
import typing
import dbm
import socket
import random

def race_condition_example(data: typing.List[int]) -> typing.List[int]:
    """
    Demonstrates a potential race condition (with a simplified example).
    """
    result = []
    lock = threading.Lock()
    
    threads = []
    for item in data:
        # Introduce a random delay for fuzzing
        delay = random.uniform(0, 0.01)  
        
        #Fuzzing: Introduce a wider range of potential None values and various types
        if random.random() < 0.1:
            item = None
        elif random.random() < 0.1:
          item = "string" #fuzzing with non-integer value
        elif random.random() < 0.1:
          item = 1.234 #fuzzing with float
        elif random.random() < 0.1:
          item = True #fuzzing with boolean
        elif random.random() < 0.1:
          item = [1, 2, 3] #Fuzzing with list
        elif random.random() < 0.1:
          item = {"a": 1} # Fuzzing with dictionary


        #Fuzzing: Introduce a thread-specific delay variation
        delay += 0.001 * threading.get_ident() % 3 #fuzzing with delay for each thread

        t = threading.Thread(target=process_item, args=(item, result, lock, 0 if item % 2 == 0 else 1, delay))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return result


def process_item(item: int, result: list, lock: threading.Lock, flag: int, delay: float):
    with lock:
        # Simulate some work.  Introduce potential error.
        if item is not None and isinstance(item, (int, float)):  # Handle None and type checking (includes float)
            time.sleep(delay + 0.001 * flag)  # Add random delay for fuzzing
            result.append(item)
            try:
                if isinstance(item, int):
                    result.append(item * item)  # Error prone line, fuzzing for this condition
                #fuzzing: add more random exceptions
                if random.random() < 0.1:
                    raise ZeroDivisionError("Simulate ZeroDivisionError")
                elif random.random() < 0.1:
                  raise TypeError("Simulate TypeError")
                elif random.random() < 0.1:
                  raise ValueError("Simulate ValueError")
                elif random.random() < 0.1:
                  raise AttributeError("Simulate AttributeError")

            except (ZeroDivisionError, TypeError, ValueError, AttributeError) as e:
                print(f"Error during item appending: {e}")
            except Exception as e:
                print(f"Error during item appending {e}")
        elif item is not None:
            result.append(item)
            if random.random() < 0.1:
                raise ValueError("Simulated error")
        else:
            result.append(-1) # Indicate a missing item


def test_replace_protocol(data: typing.List[int]):
    """Demonstrates the replace protocol."""
    class MyData(copy.namedtuple("MyData", ["value", "flag"])):
        def __replace__(self, **kwargs):
            new_value = kwargs.get("value", self.value)
            new_flag = kwargs.get("flag", self.flag)
            
            # Fuzzing: wider range of error conditions and potential types
            if not isinstance(new_value, (int, float, type(None))):
                raise TypeError(f"Invalid type for new_value: {type(new_value)}")
            if new_value < -10000 or new_value > 10000:
                raise ValueError(f"Error in value {new_value}")
            if new_flag < -10000 or new_flag > 10000:
                raise ValueError(f"Error in flag {new_flag}")


            if random.random() < 0.1:
              new_value = None #fuzzing, set value to none or other types
            elif random.random() < 0.1:
              new_value = "string" # fuzzing non-int
            elif random.random() < 0.1:
              new_value = 1.234  # fuzzing float

            return super()._replace(value=new_value, flag=new_flag)


    replaced_data = []
    for i in data:
        d = MyData(i, 1)
        try:
            replaced_data.append(d._replace(value=i * 2, flag=i))
        except Exception as e:
            print(f"Error replacing data {e}")
    return replaced_data


def test_ssl():
  """Demonstrates SSL connection with stricter default context"""
  try:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0) # increase timeout for fuzzing

    #Fuzzing: Invalid host, non-existent hosts, numerical host, etc
    server_hostname = "localhost"  # default
    if random.random()<0.5:  #50% chance to change host name
      server_hostname = str(random.randint(1, 10000))

    with context.wrap_socket(sock, server_hostname=server_hostname) as s:
        s.connect(("localhost", 443)) # Default connection attempt
        return True
  except (ssl.SSLError, socket.timeout, ValueError, OSError) as e:  
    print(f"SSL/Socket error: {e}")
    return False



#Example Usage (unchanged)
data = list(range(10))
try:
    result = race_condition_example(data)
    print("Race condition result:", result)

    replaced_data = test_replace_protocol(data)
    print("Replace protocol result:", replaced_data)
    
    if test_ssl():
        print("Successful SSL connection")
    else:
        print("Failed SSL connection")
except Exception as e:
  print(f"An error occurred: {e}")

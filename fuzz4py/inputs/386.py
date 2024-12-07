
import threading
import copy
import os
import time
import ssl
import typing
import dbm

def race_condition_example(data: typing.List[int]) -> typing.List[int]:
    """
    Demonstrates a potential race condition (with a simplified example).
    """
    result = []
    lock = threading.Lock()
    
    threads = []
    for item in data:
        t = threading.Thread(target=process_item, args=(item, result, lock, 0 if item % 2 else 1))  # Added a flag to distinguish the odd even case
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return result


def process_item(item: int, result: list, lock: threading.Lock, flag):
    with lock:
        # Simulate some work.
        if item % 2 == 0:
            time.sleep(0.001*flag)  # Introduce a delay. Flagged delay.
            result.append(item)
        else:
            result.append(item)


def test_replace_protocol(data: typing.List[int]):
    """Demonstrates the replace protocol."""
    class MyData(copy.namedtuple("MyData", ["value", "flag"])):  # Added flag
        def __replace__(self, **kwargs):
            new_value = kwargs.get("value", self.value)
            new_flag = kwargs.get("flag", self.flag)  # Added flag
            return super()._replace(value=new_value, flag=new_flag)

    replaced_data = []
    for i in data:
        d = MyData(i, 1) #Initial Flag
        replaced_data.append(d._replace(value=i*2, flag= i)) #Changed the flag value
    return replaced_data

def test_ssl():
  """Demonstrates SSL connection with stricter default context"""

  try:
    context = ssl.create_default_context()
    context.check_hostname = False #disable hostname validation for testing
    context.verify_mode = ssl.CERT_NONE #disable certificate validation for testing
    with context.wrap_socket(socket.socket(), server_hostname="localhost") as s: #create a socket
        s.connect(("localhost", 443)) #Connect to a host and port
        return True
  except ssl.SSLError as e:
    print(f"SSL error: {e}")
    return False
import socket
#Example Usage
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


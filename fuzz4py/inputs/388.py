
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
        t = threading.Thread(target=process_item, args=(item, result, lock, 0 if item % 2 == 0 else 1, delay))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return result


def process_item(item: int, result: list, lock: threading.Lock, flag: int, delay: float):
    with lock:
        # Simulate some work.  Introduce potential error.
        if item % 2 == 0:
            time.sleep(delay + 0.001 * flag)  # Add random delay for fuzzing
            result.append(item)
            try:
                result.append(item*item)  # Error prone line, fuzzing for this condition
            except Exception as e:
                print(f"Error during item appending {e}")
        else:
            result.append(item)
            if random.random() < 0.1:
                raise ValueError("Simulated error")


def test_replace_protocol(data: typing.List[int]):
    """Demonstrates the replace protocol."""
    class MyData(copy.namedtuple("MyData", ["value", "flag"])):
        def __replace__(self, **kwargs):
            new_value = kwargs.get("value", self.value)
            new_flag = kwargs.get("flag", self.flag)
            # Potentially corrupted data
            if new_value < 0:
              raise ValueError("Error in negative value")
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
    # Introduce potential error in socket operation
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # Set a timeout
    with context.wrap_socket(sock, server_hostname="localhost") as s:
        s.connect(("localhost", 443))
        return True
  except (ssl.SSLError, socket.timeout) as e:
    print(f"SSL/Socket error: {e}")
    return False


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

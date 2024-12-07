
import threading
import time
import copy
import dbm
import os
import ssl
import typing

def test_free_threading(n: int) -> None:
    """
    Tests free-threading by creating multiple threads and updating a shared variable.
    """
    shared_var = 0
    
    def worker(i: int) -> None:
        nonlocal shared_var
        time.sleep(0.1) # Introduce some randomness
        shared_var += i
        
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(n)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"Shared variable after {n} threads: {shared_var}")

def test_jit(n: int) -> None:
    """A potentially JIT-compilable loop"""
    result = 0
    for i in range(n):
        result += i * i * 2.0
    return result

def test_docstring_whitespace():
  """This is a docstring with varying indentation
    that has a multi-line example.
        
      example = """
        
        def do_something(x): return x+1
      """
      """
  pass

def test_complex_annotations(data: typing.List[typing.Union[str, int]]) -> typing.Dict[str, int]:
  """Tests complex annotations"""
  result: typing.Dict[str, int] = {}
  for item in data:
      if isinstance(item, str):
          result[item] = len(item)
      elif isinstance(item, int):
          result[str(item)] = item * 2
      else:
          raise TypeError("Invalid data type")
  return result


def main():
  test_free_threading(5)
  result = test_jit(100000)
  print(f"JIT result: {result}")
  test_docstring_whitespace()
  data = ["hello", 123, "world", 456]
  try:
    result = test_complex_annotations(data)
    print(f"Complex annotation result: {result}")
  except TypeError as e:
    print(f"Caught TypeError: {e}")

  #test ssl with a dummy certificate.  (Important to remove in real fuzzing)
  try:
    context = ssl.create_default_context()
    with context.wrap_socket(
        socket.socket(), server_hostname="localhost"
    ) as s:
        print(f"SSL connection: {s}")
  except Exception as e:
    print(f"SSL error: {e}")


if __name__ == "__main__":
  import socket
  main()


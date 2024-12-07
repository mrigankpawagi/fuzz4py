
import threading
import copy
import os
import ssl
import time
import typing
import dbm
import functools


def complex_function(arg1: typing.List[int], arg2: str) -> int:
    """
    This function demonstrates the use of complex types and annotations.  It does not handle exceptions well for testing purposes.
    """
    try:
        result = sum(arg1) * len(arg2)
        return result
    except (TypeError, ValueError):
        return -1  # Indicates an error


def test_free_threading(num_threads: int = 5):
    """
    Example of a free-threading function.
    """
    shared_list = []
    
    def worker(i):
        # Potential race condition.
        shared_list.append(i)
        time.sleep(0.1) # Introduces some timing variation


    threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return shared_list


def test_jit_and_locals():
    """
    Example of a function potentially JIT-compiled, with locals semantics.
    """
    a = 10
    b = [1,2,3,4]
    locals_dict = locals()
    return (a, locals_dict["b"])


def test_complex_annotations():
    """
    Fuzzing with complex type annotations.
    """
    complicated_annotation: typing.List[typing.Union[int, str]] = [1, 2, "3", 4]


#Fuzzing with new dbm backend
def test_dbm_sqlite3(db_name="test.db"):
  """
  Fuzzer for dbm.sqlite3
  """
  db = dbm.open(db_name, 'c')
  try:
    db['key1'] = 'value1'
    db['key2'] = 123
    
    # Attempt to write malformed data.
    db['key3'] = 'malformed\x00data'
  finally:
    db.close()

    db = dbm.open(db_name, 'r')
    try:
        key_found = db.get('key1')
    finally:
        db.close()



def main():
    """
    Entry point to run the various fuzzing tests.
    """
    test_free_threading()
    test_jit_and_locals()
    test_complex_annotations()
    test_dbm_sqlite3()

    print("Fuzzing tests complete.")


if __name__ == "__main__":
    main()

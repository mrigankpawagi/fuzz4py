
import threading
import time
import copy
import dbm
import os
import ssl
import typing


def jit_target_function(data: list[int]) -> int:
    """
    A function likely to be JIT compiled.  Calculates the sum of integers in a list.
    """
    total = 0
    for value in data:
        total += value
    return total


def test_free_threading():
    """Tests free-threading and the GIL."""
    data = [i for i in range(1000)]
    threads = []

    for i in range(5):
        t = threading.Thread(target=jit_target_function, args=(copy.deepcopy(data),))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def test_dbm_sqlite3():
    """Test dbm.sqlite3 with various inputs."""
    try:
        db = dbm.open('test.db', 'c')  # 'c' for create
        db['key1'] = b'some\x00data'  # Test with null bytes
        db['key2'] = b'\xff' * 1024  # Test large data
        db.close()
        db = dbm.open('test.db', 'r')
        value = db['key1']
        db.close()
    except Exception as e:
        print(f"Error in dbm.sqlite3 test: {e}")
    os.remove("test.db")


def test_ssl_create_default_context():
    """Test SSL with various certificates."""
    try:
        context = ssl.create_default_context()
        # Replace with your test certificate paths
        with open("test_certificate.pem", "rb") as f:
            context.load_verify_locations(cafile=f.read())
        # Simulate an SSL connection (replace with your actual code)
    except Exception as e:
        print(f"Error in SSL test: {e}")



def main():
    """Entry point to test various features."""
    test_free_threading()
    test_dbm_sqlite3()
    test_ssl_create_default_context()
    

if __name__ == "__main__":
    main()

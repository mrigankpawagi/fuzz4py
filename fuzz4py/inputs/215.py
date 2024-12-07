
import threading
import time
import copy
import os
import ssl
import sqlite3
import typing

def race_condition_example(data: int, num_threads: int = 5):
    """
    Illustrates a potential race condition.  Intended for fuzzing with free-threading.
    """
    shared_data = 0
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_data, args=(shared_data,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return shared_data

def increment_data(shared_data):
    """
    Increments shared data.
    """
    for _ in range(1000):
        shared_data[0] += 1
        time.sleep(0.001) # Introducing a delay to potentially trigger race conditions

def test_os_timer(num_calls: int = 10):
    """
    Tests os timer functions.
    """
    for _ in range(num_calls):
        start_time = time.monotonic()
        os.times()
        end_time = time.monotonic()
        time_taken = end_time - start_time
        if time_taken < 0:  # Check for potential negative values
            raise ValueError("Negative time taken by os.times()")

def test_ssl(host: str = "example.com", port: int = 443):
    """
    Tests SSL connections.
    """
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(
            socket.socket(), server_hostname=host
        ) as ssock:
            ssock.connect((host, port))
            ssock.recv(1024)
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
        raise

import socket

def main():
    # Example using a list to simulate mutable shared data
    data_to_increment = [0]
    try:
        result = race_condition_example(data_to_increment)
        print("Race Condition Result:", result)
    except Exception as e:
        print(f"Race Condition Example Error: {e}")
        
    try:
        test_os_timer()
        print("OS Timer Test passed")
    except Exception as e:
        print(f"OS Timer Test Error: {e}")

    # Example, testing SSL.  Needs a proper target host.
    try:
        test_ssl()
        print("SSL Test Passed")
    except Exception as e:
        print(f"SSL Test Error: {e}")


if __name__ == "__main__":
    main()

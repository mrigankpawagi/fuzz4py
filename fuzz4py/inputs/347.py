
import threading
import time
import random

# Focus on free-threading and potential JIT compiler impact
def worker(data, lock, jit_flag, thread_id):
    if jit_flag:
        # Simulate a hot loop likely to be JIT-compiled
        total = 0
        for _ in range(1000000):
            total += data
            if random.random() < 0.05:
                time.sleep(0.001)

        with lock:  # Use a context manager for lock
            print(f"Thread {thread_id} calculated {total} (JIT)")
            return total
    else:
        # Similar operation without JIT
        total = 0
        for _ in range(1000000):
            total += data
            if random.random() < 0.05:
                time.sleep(0.001)

        with lock:
            print(f"Thread {thread_id} calculated {total}")
            return total


def main():
    data = random.randint(-100, 100)  # Introduce random data
    lock = threading.Lock()
    threads = []
    results = []

    start_time = time.perf_counter()

    for i in range(5):
        jit_flag = (i % 2 == 0)  # Alternate JIT and non-JIT
        thread_id = f"Thread-{i + 1}"  # More descriptive thread ID
        t = threading.Thread(target=worker, args=(data, lock, jit_flag, thread_id))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        try:
            result = t.get_result()  # Correct way to get return value if available
            results.append(result)
        except AttributeError:
            pass  # Handle cases where result is not available; likely not needed here

    end_time = time.perf_counter()
    print(results)

    # Fuzzing docstring whitespace stripping: Demonstrates multithreading
    # with optional JIT compilation
    print(f"Execution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()

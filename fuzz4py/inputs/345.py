
import threading
import time

# Focus on free-threading and potential JIT compiler impact
def worker(data, lock, jit_flag):
    if jit_flag:
        # Simulate a hot loop likely to be JIT-compiled
        total = 0
        for _ in range(1000000):
            total += data
        lock.acquire()
        print(f"Thread {threading.get_ident()} calculated {total} (JIT)")
        lock.release()
    else:
        # Similar operation without JIT
        total = 0
        for _ in range(1000000):
            total += data
        lock.acquire()
        print(f"Thread {threading.get_ident()} calculated {total}")
        lock.release()


def main():
    data = 1
    lock = threading.Lock()
    threads = []

    start_time = time.perf_counter()

    for i in range(5):
        jit_flag = (i % 2 == 0)  # Alternate JIT and non-JIT
        t = threading.Thread(target=worker, args=(data, lock, jit_flag))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.perf_counter()

    # Fuzzing docstring whitespace stripping: Demonstrates multithreading
    # with optional JIT compilation
    print(f"Execution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()

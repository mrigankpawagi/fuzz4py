
import threading
import time
import copy
import os
import ssl
import dbm
import random
import sys
import typing


def thread_func(x, ctx, seed):
    try:
        db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
        try:
            db = dbm.open(db_filename, 'c')
            key = str(x) if random.random() < 0.5 else str(x) + 'bad_key'
            db[key] = str(x * 2 + random.randint(0, 100) * random.random())
            if random.random() < 0.2:
                db[key] = "CORRUPTED_DATA"
            db.close()
        except (Exception, dbm.error) as e:
            print(f"Database error in thread {x}: {e}")
            raise

        result = 0
        for i in range(10000 + random.randint(-500, 500)):
            try:
                result += i * x + random.randint(-10, 10)
                if random.random() < 0.05 and x == 0:
                    raise ZeroDivisionError
            except ZeroDivisionError as e:
                print(f"ZeroDivisionError in thread {x}: {e}")
                raise


        a = copy.copy([1, 2, 3, random.random(), random.randint(-100, 100)])
        try:
            replacement_data = random.choice([
                [4, 5, random.randint(-100, 100)],
                42,
                "string",
                None
            ])
            b = copy.replace(a, replacement_data)
            if b is not a:
                print(f"Thread {x}: Replace works correctly")
            else:
                print(f"Thread {x}: Replace failed unexpectedly")
        except Exception as e:
            print(f"Thread {x}: Copy.replace error: {e}")
            raise



        try:
            ctx2 = copy.copy(ctx)
            ctx2.check_hostname = bool(random.getrandbits(1))
            ctx2.verify_mode = random.choice([ssl.CERT_NONE, ssl.CERT_REQUIRED, ssl.CERT_OPTIONAL])

            cert_file = random.choice(["bad_certificate.pem", "mycert.pem", "nonexistent.pem"])
            ctx2.load_verify_locations(os.path.abspath(cert_file))
            ctx2.wrap_socket(None, server_hostname="localhost")

            print(f"Thread {x}: connected successfully (insecure) using context {ctx2}")

        except Exception as e:
            print(f"Thread {x}: SSL connection failed: {e}")

    except Exception as e:
        print(f"Thread {x} failed: {e}, seed: {seed}")
    finally:
        try:
            db_filename = f'mydatabase_{x}_{random.randint(0, 100)}'
            if os.path.exists(db_filename):
                os.remove(db_filename)
        except Exception as e:
            print(f"Error during cleanup in thread {x}: {e}")


def race_condition_test(data):
    shared_resource = 0
    def increment():
        nonlocal shared_resource
        shared_resource += data
        time.sleep(0.001)
    threads = [threading.Thread(target=increment) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return shared_resource


def jit_test():
    i = 0
    while i < 1000000:
        result = 2 * i + 1
        i += 1
    return result


def complex_annotation_test(data: typing.List[typing.Union[int, str]]) -> typing.List[int]:
    results = []
    for item in data:
        try:
            if isinstance(item, int):
                results.append(item * 2)
            elif isinstance(item, str):
                results.append(int(item))
        except ValueError:
            print("Error converting string to integer.")
            results.append(-1)
    return results


def test_replace(data):
  class MyData:
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __replace__(self, *, a=None, b=None):
      return type(self)(a if a is not None else self.a, b if b is not None else self.b)

  original_data = MyData(1, 2)
  new_data = copy.replace(original_data, a=3)
  return new_data.a


def main():
    print(f"Race condition test: {race_condition_test(10000)}")
    print(f"JIT test result: {jit_test()}")

    complex_data = [1, 2, "3", 4, "5", "abc"]
    results = complex_annotation_test(complex_data)
    print(f"Complex annotation results: {results}")

    print(f"Replace test result: {test_replace(1)}")

    try:
        timer_result = os.times()
        print(f"Timer result: {timer_result}")
    except AttributeError as e:
        print(f"AttributeError: {e}")


if __name__ == "__main__":
    main()


import threading
import time
import copy
import os
import ssl
import typing
import random
import socket

def worker(arg: int) -> None:
    # Simulate a resource-intensive operation
    try:
        time.sleep(arg/10 if arg >= 0 else 0)  # Handle potential negative input gracefully
        if arg % 2 == 0:
            # Simulate some kind of side-effect
            with open("testfile.txt", "a") as f:
                f.write(str(arg) + "\n") #Added newline for easier file reading
        elif arg % 2 == 1 and arg > 10:
            raise ValueError("Negative sleep time or invalid input")
        elif arg == -1:  #Add a specific error case
            raise Exception("Intentionally raising an exception")
        elif arg is None:
            pass #Handle None gracefully
        
        elif isinstance(arg, float):
            print(f"Worker thread {threading.get_ident()} received a float value") #Log float input
        elif arg is True or arg is False:
            print(f"Worker thread {threading.get_ident()} received a boolean value {arg}")
    except ValueError as e:
        print(f"Worker thread {threading.get_ident()} encountered error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in worker: {e}")
    

def multithreaded_example(num_threads: int, data: typing.List[int]) -> None:
    threads = []
    for i in range(num_threads):
        try:
            thread = threading.Thread(target=worker, args=(data[i],))
            threads.append(thread)
            thread.start()
        except (IndexError, TypeError, ValueError, AttributeError) as e:
            print(f"Error creating thread {i}: {e}")
            #Handle the error, better error handling. Log the exception
            import traceback
            traceback.print_exc()
    for thread in threads:
        thread.join()


def main():
    try:
        #Fuzzing -  complex list of integers, including potential errors
        data = [random.randint(-100, 100) for i in range(10)]  # Example data with potential negatives
        num_threads = len(data)
        multithreaded_example(num_threads, data)


        # Fuzzing -  different threading usage patterns, wider range
        num_threads = 5
        data = [random.randint(0, 20) for _ in range(num_threads*2)] #Wider range, more values
        multithreaded_example(num_threads, data)
        data = [None, 1, 2, 3]  # Test with None
        multithreaded_example(4, data)


        # Fuzzing -  different data types
        num_threads = 5
        data = [i*3 for i in range(num_threads) if i % 2 == 0]
        multithreaded_example(num_threads, data)
        data = [i for i in range(num_threads)]
        data.append(10.5)  # Different type
        multithreaded_example(num_threads, data)
        data = [True, False]  # Boolean values
        multithreaded_example(2, data)
        data = [-1]
        multithreaded_example(1,data)
        data = [1.5, 2.7]  #Adding floating-point values
        multithreaded_example(2, data)




        # Huge input - Crucial for fuzzing.
        data = [random.randint(0, 500) for _ in range(1000)] 
        multithreaded_example(50, data[:50])  # Limit to 50 threads for large input


        # copy module example - (unchanged)
        my_list = [1, 2, 3]
        new_list = copy.deepcopy(my_list)
        new_list[0] = 10
        print(f"Original list: {my_list}")
        print(f"New list: {new_list}")

        # Demonstrating ssl - placeholder for more extensive fuzzing later
        context = ssl.create_default_context()
        try:
            # Simulate a connection with varying data
            with context.wrap_socket(socket.socket(), server_hostname='example.com') as s:
                s.sendall(b"some data")
                response = s.recv(1024)
                print(response.decode())
        except ssl.SSLError as e:
           print(f"SSL error: {e}")
        except OSError as e:
            print(f"OS Error during SSL connection: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc() #More detailed exception handling

    finally:
        try:
            os.remove("testfile.txt")
        except OSError:
            pass


if __name__ == "__main__":
    main()


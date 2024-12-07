
import threading
import copy
import os
import ssl
import typing

def complex_function(data: typing.List[int], replace_value: int = 0) -> typing.List[int]:
    """
    A function demonstrating the use of copy.replace() and potentially complex
    behavior to trigger a race condition.
    """
    
    # Create a local copy to modify in a separate thread
    local_copy = copy.deepcopy(data)
    
    def worker():
        try:
            # Introduce a potential race condition by modifying the local copy
            local_copy[0] = replace_value
        except IndexError:
            print("Index Error caught, likely due to input data issues.")
        
    # Start a separate thread to execute the function
    thread = threading.Thread(target=worker)
    thread.start()

    # Simulate other operations
    return local_copy


def main():
  # Example usage:
  input_data = [1, 2, 3]
  result = complex_function(input_data)
  print(f"Original data: {input_data}")
  print(f"Modified data: {result}")


if __name__ == "__main__":
    main()


import threading
import copy
import os
import ssl
import typing

def complex_function(data: typing.List[int], replace_value: int = 0) -> typing.List[int]:
    """
    A function demonstrating the use of copy.deepcopy() and potentially complex
    behavior.  This version avoids a potential race condition.
    """
    
    # Create a local copy to modify
    local_copy = copy.deepcopy(data)
    
    try:
        # Modify the local copy outside of a thread
        local_copy[0] = replace_value
    except IndexError:
        print("Index Error caught, likely due to input data issues.")
    
    # Simulate other operations, but we return immediately.
    return local_copy


def main():
  # Example usage:
  input_data = [1, 2, 3]
  result = complex_function(input_data)
  print(f"Original data: {input_data}")
  print(f"Modified data: {result}")


if __name__ == "__main__":
    main()


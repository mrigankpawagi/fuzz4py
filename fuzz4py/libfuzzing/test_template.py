import os
import pickle
import sys
import typing

# imports for APIs
import codecs
import email

test_index = int(sys.argv[1])
NAME = '{app_name}'

# script path
base_path = os.path.dirname(os.path.realpath(__file__))

# load test inputs
try:
    with open(os.path.join(base_path, 'test_cases', NAME + '.bin'), 'rb') as f:
        test_cases = pickle.load(f)
        test_case = test_cases[test_index]
except Exception:
    exit(0)

try:
    {app}
except Exception:
    exit(0)

try:
    test(*test_case)
except (RecursionError, MemoryError) as e:
    print(e.__class__.__name__, file=sys.stderr)
    print(test_case, file=sys.stderr)
    exit(1)
except Exception:
    exit(0)

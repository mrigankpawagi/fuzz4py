import os
import pickle
import sys

try:
    {import}
    NAME = '{full_name}'
except:
    exit(0)

test_index = int(sys.argv[1])

# script path
base_path = os.path.dirname(os.path.realpath(__file__))

# load test inputs
try:
    with open(os.path.join(base_path, 'test_cases', NAME + '.bin'), 'rb') as f:
        test_cases = pickle.load(f)
except Exception:
    exit(0)

try:
    {full_name}(*test_cases[test_index])
except (RuntimeError, MemoryError) as e:
    print(e.__class__.__name__, file=sys.stderr)
    print(test_cases[test_index], file=sys.stderr)
    exit(1)
except Exception:
    pass

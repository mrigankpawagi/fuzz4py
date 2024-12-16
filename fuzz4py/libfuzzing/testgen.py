import os
import json
import pickle
from ghAIstwriter.ghaistwriter import generate_strategy
from tqdm import tqdm
from hypothesis import settings, strategies, given
import random

RETRY_BUDGET = 5

# script path
script_path = os.path.dirname(os.path.realpath(__file__))

# check that the directory documentation/distilled exists
os.makedirs(os.path.join(script_path, "documentation", "distilled"), exist_ok=True)

# walk over the documentation/distilled directory and collect all APIs
apis = []
for root, dirs, files in os.walk(os.path.join(script_path, "documentation", "distilled")):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file)) as f:
                apis.extend(json.load(f)["apis"])

print(f"Found {len(apis)} APIs")
print("Generating test cases using ghAIstwriter")


def test_cases_from_strategy(strategy, n=10):
    test_cases = []
    
    @settings(max_examples=n)
    @given(strategies.tuples(*strategy))
    def test(args):
        nonlocal test_cases
        test_cases.append(args)

    test()
    return test_cases


# shuffle the APIs list
random.shuffle(apis)
os.makedirs(os.path.join(script_path, "tests", "test_cases"), exist_ok=True)
for api in tqdm(apis):
    test_case_file_path = os.path.join(script_path, "tests", "test_cases", f"{api['name']}.bin")
    if os.path.exists(test_case_file_path): continue # skip if test cases already exist
    
    try:
        # generate strategy and then test cases
        strategy = generate_strategy("\n".join([api["name"], api["signature"], api["description"]]))
        test_cases = test_cases_from_strategy(strategy, n=1000)

        # write test cases to file
        with open(test_case_file_path, "wb") as f:
            pickle.dump(test_cases, f)
            tqdm.write(f"Generated test cases for {api['name']}")
        
    except Exception as e: tqdm.write(f"Could not generate strategy for API: {api['name']}")

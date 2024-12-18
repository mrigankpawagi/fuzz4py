import os
import json
import pickle
from ghAIstwriter.ghaistwriter import generate_strategy
from tqdm import tqdm
from hypothesis import settings, strategies, given
from hashlib import sha256
import random

STRATEGY_BUDGET = 3

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

print(f"Found {len(apis)} APIs.")
print("Generating test cases using ghAIstwriter.")


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
    api_name = sha256(api["signature"].encode()).hexdigest() # hash the signature to get a unique name
    for app_index in range(len(api["apps"])):
        test_case_file_path = os.path.join(script_path, "tests", "test_cases", f"{api_name}_{app_index}.bin")
        if os.path.exists(test_case_file_path): continue # skip if test cases already exist
        
        tqdm.write(f"Generating strategies for {api["signature"]}.\nApp {app_index + 1} of {len(api['apps'])}.")
        all_test_cases = []

        for strategy_attempt in range(STRATEGY_BUDGET):
            tqdm.write(f"{strategy_attempt + 1}/{STRATEGY_BUDGET}", end=" ")  
            try:
                # generate strategy and then test cases
                strategy = generate_strategy("\n".join([api["signature"], api["description"], api["apps"][app_index]]))
                test_cases = test_cases_from_strategy(strategy, n=15000)

                all_test_cases.extend(test_cases)

                # save test cases
                with open(test_case_file_path, "wb") as f:
                    pickle.dump(all_test_cases, f)

                tqdm.write(f"Generated strategy and saved test cases.")

            except Exception as e: tqdm.write(f"Could not generate strategy:\n{e}")

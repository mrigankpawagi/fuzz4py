import os
from hashlib import sha256
import json
import ast

# script path
script_path = os.path.dirname(os.path.realpath(__file__))

# load the template
with open(os.path.join(script_path, "test_template.py")) as f:
    template = f.read()

# check that the directory documentation/distilled exists
os.makedirs(os.path.join(script_path, "documentation", "distilled"), exist_ok=True)

# walk over the documentation/distilled directory and collect all APIs
all_apis = []
for root, dirs, files in os.walk(
    os.path.join(script_path, "documentation", "distilled")
):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file)) as f:
                all_apis.extend(json.load(f)["apis"])


# check that the directory tests/test_cases exists
os.makedirs(os.path.join(script_path, "tests", "test_cases"), exist_ok=True)

# write test files
for api in all_apis:
    api_name = sha256(api["signature"].encode()).hexdigest() # hash the signature to get a unique name
    for app_index in range(len(api["apps"])):
        test_case_file_path = os.path.join(script_path, "tests", "test_cases", f"{api_name}_{app_index}.bin")
        
        if not os.path.exists(test_case_file_path):
            continue # skip if test cases do not exist
        
        # check that the app has no syntax errors
        app_code = api["apps"][app_index]
        try:
            ast.parse(app_code)
        except SyntaxError:
            continue # skip if syntax error

        # write the test file
        test_file_path = os.path.join(script_path, "tests", f"{api_name}_{app_index}.py")
        with open(test_file_path, "w") as f:
            f.write(
                template.format(
                    **{
                        "app_name": f"{api_name}_{app_index}",
                        "app": "\n".join([f"    {line}" for line in app_code.split("\n")]),
                        # indent the code for try-except block^
                    }
                )
            )

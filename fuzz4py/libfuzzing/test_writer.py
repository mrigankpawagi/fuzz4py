import os
import subprocess
import json

# script path
script_path = os.path.dirname(os.path.realpath(__file__))


def resolve_package_name(full_name):
    prefixes = []
    parts = full_name.split(".")
    for part in parts:
        if not prefixes:
            prefixes.append(part)
        else:
            prefixes.append(f"{prefixes[-1]}.{part}")
        
    for prefix in prefixes:
        # import the prefix and check if the full_name is in the scope
        process = subprocess.Popen(["python", "-c", f"import {prefix}; f = {full_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        retcode = process.wait()
        
        if retcode == 0:
            return prefix

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
    test_case_file_path = os.path.join(
        script_path, "tests", "test_cases", f"{api['name']}.bin"
    )
    test_file_path = os.path.join(script_path, "tests", f"test_{api['name']}.py")

    if os.path.exists(test_case_file_path):
        full_name = api["name"]
        
        ### EXCEPTIONS ###
        if full_name.startswith("reprlib.Repr."):
            full_name = full_name.replace("reprlib.Repr.", "reprlib.Repr().")
        ### END EXCEPTIONS ###
        
        package_name = resolve_package_name(full_name)
        if not package_name:
            print("Could not resolve package name for", full_name)

        with open(test_file_path, "w") as f:
            f.write(
                template.format(
                    **{
                        "import": f"import {package_name}",
                        "full_name": full_name,
                        "timeout": 1,
                    }
                )
            )

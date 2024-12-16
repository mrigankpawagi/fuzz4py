import os
import subprocess
import argparse
import tqdm
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# script path
script_path = os.path.dirname(os.path.realpath(__file__))
script_path_rel = os.path.relpath(script_path, os.getcwd())

parser = argparse.ArgumentParser(description="Fuzz4Py Libfuzzing: Fuzz Python Libraries.")
parser.add_argument("executable", type=str, help="Path to the python executable.")
parser.add_argument("--inputs", type=int, default=1000, help="Number of test inputs per API.")
parser.add_argument("--timeout", type=int, default=5, help="Timeout for each test input in seconds.")
args = parser.parse_args()

# check that the directory tests exists
os.makedirs(os.path.join(script_path, "tests"), exist_ok=True)
test_files = [x for x in os.listdir(os.path.join(script_path, "tests")) if x.startswith("test_") and x.endswith(".py")]

# make directory for storing results (include timestamp in the directory name)
results_dir = os.path.join(script_path, "results" + str(time.time()))
os.makedirs(results_dir, exist_ok=True)


def run_program(executable: str, input_file: str, test_index: int):
    """run "{args.executable} {input_file}" and capture the return code and stdout, stderr."""
    process = subprocess.Popen([executable, input_file, str(test_index)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd())
    stdout, stderr = process.communicate()
    return_code = process.returncode

    return return_code, stdout.decode(), stderr.decode()

def process_input_file(test_file: str, test_index: int):
    return_code, stdout, stderr = run_program(args.executable, os.path.join(script_path, "tests", test_file), test_index)
    return return_code, stdout, stderr, test_file, test_index

with ProcessPoolExecutor() as executor:
    futures = [executor.submit(process_input_file, test_file, test_index) for test_file in test_files for test_index in range(args.inputs)]
    for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
        try:
            return_code, stdout, stderr, test_file, test_index = future.result(timeout=args.timeout)

            # record crashes
            if return_code != 0:
                with open(os.path.join(results_dir, "crashs.txt"), "a") as f:
                    f.write(f"{test_file}::{test_index}\n")
                    f.write(f"{stdout}\n{stderr}\n" + "-"*80 + "\n")
                    
        except TimeoutError as e:
            # record hangs
            with open(os.path.join(args.output, "results", "timeout.txt"), "a") as f:
                f.write(f"{test_file}::{test_index}\n")

        except Exception as e:
            # record other errors
            with open(os.path.join(args.output, "results", "error.txt"), "a") as f:
                f.write(f"{test_file}::{test_index}\n")

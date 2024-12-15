import os
import shutil
import subprocess
import argparse
import tqdm
import random
import shlex
from concurrent.futures import ProcessPoolExecutor, as_completed

# script path
script_path = os.path.dirname(os.path.realpath(__file__))
script_path_rel = os.path.relpath(script_path, os.getcwd())

parser = argparse.ArgumentParser(description="Fuzz4Py: Fuzz a python executable.")
parser.add_argument("executable", type=str, help="Path to the python executable to be fuzzed.")
parser.add_argument("--inputs", type=str, default=os.path.join(script_path_rel, "inputs"), help="Path to the directory containing the input files.")
parser.add_argument("--output", type=str, default=os.path.join(script_path, "resources"), help="Path to the directory where the output logs will be stored.")
parser.add_argument("--timeout", type=int, default=60, help="Timeout (in seconds) for each input file.")
args = parser.parse_args()

# get the list of all input files
input_files = [x for x in os.listdir(args.inputs) if x.endswith(".py")]
random.shuffle(input_files) # shuffle the input files

os.makedirs(os.path.join(args.output, "results"), exist_ok=True)
shutil.rmtree(os.path.join(args.output, "results", "temp"), ignore_errors=True)
os.makedirs(os.path.join(args.output, "results", "temp"), exist_ok=True)

# see which input files have been processed already
processed_files = []
if os.path.exists(os.path.join(args.output, "results", "done.txt")):
    with open(os.path.join(args.output, "results", "done.txt"), "r") as f:
        processed_files = list(map(str.strip, f.readlines()))
input_files = list(filter(lambda x: x.split(".")[0] not in processed_files, input_files))

def run_program(executable: str, input_file: str):
    """run "{args.executable} {input_file}" and capture the return code and stdout, stderr."""
    process = subprocess.Popen([*shlex.split(executable), input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd())
    stdout, stderr = process.communicate()
    return_code = process.returncode

    return return_code, stdout.decode(), stderr.decode()

def process_input_file(input_file):
    input_id = input_file.split('.')[0]

    # create a temporary file for the input
    open(os.path.join(args.output, "results", "temp", input_id), "w").close()

    return_code, stdout, stderr = run_program(args.executable, os.path.join(args.inputs, input_file))
    
    # remove the temporary file
    os.remove(os.path.join(args.output, "results", "temp", input_id))

    return return_code, stdout, stderr, input_id

with ProcessPoolExecutor() as executor:
    futures = [executor.submit(process_input_file, input_file) for input_file in input_files]
    for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
        try:
            return_code, stdout, stderr, input_id = future.result(timeout=args.timeout)

            # record crashes
            if any(msg in stderr.lower() + stdout.lower() for msg in ["segmentation fault", "core dumped", "recursion", "memoryerror", "killed"]):
                with open(os.path.join(args.output, "results", f"crash.txt"), "a") as f:
                    f.write(f"{input_id}\n")
                print(f"Crash: {input_id}")
        except TimeoutError as e:
            # record hangs
            with open(os.path.join(args.output, "results", "timeout.txt"), "a") as f:
                f.write(f"{input_id}\n")
            print(f"Timeout: {input_id}")
        except Exception as e:
            # record other errors
            with open(os.path.join(args.output, "results", "error.txt"), "a") as f:
                f.write(f"{input_id}\n")
            print(f"Error: {input_id}")
        finally:
            # mark as done
            with open(os.path.join(args.output, "results", f"done.txt"), "a") as f:
                f.write(f"{input_id}\n")

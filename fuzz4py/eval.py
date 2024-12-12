import os
import shutil
import subprocess
import argparse
import tqdm
import random
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
input_files = os.listdir(args.inputs)
input_files.remove("log.txt") # ignore the log file
random.shuffle(input_files) # shuffle the input files

os.makedirs(os.path.join(args.output, "results"), exist_ok=True)
shutil.rmtree(os.path.join(args.output, "results", "temp"), ignore_errors=True)
os.makedirs(os.path.join(args.output, "results", "temp"), exist_ok=True)
os.makedirs(os.path.join(args.output, "results_summaries"), exist_ok=True)

# see which input files have been processed already
processed_files = [x.split('_', 1)[1] for x in os.listdir(os.path.join(args.output, "results")) if x.startswith("result_")]
input_files = list(filter(lambda x: x not in processed_files, input_files))

def run_program(executable: str, input_file: str):
    """run "{args.executable} {input_file}" and capture the return code and stdout, stderr."""    
    process = subprocess.Popen([executable, input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd())
    stdout, stderr = process.communicate()
    return_code = process.returncode

    return return_code, stdout.decode(), stderr.decode()

def process_input_file(input_file):
    input_id = input_file.split('.')[0]
    output_path = os.path.join(args.output, "results", "result_" + input_file)

    # create a temporary file for the input
    open(os.path.join(args.output, "results", "temp", input_id), "w").close()

    return_code, stdout, stderr = run_program(args.executable, os.path.join(args.inputs, input_file))
    
    # remove the temporary file
    os.remove(os.path.join(args.output, "results", "temp", input_id))

    return return_code, stdout, stderr, output_path, input_id

with ProcessPoolExecutor() as executor:
    futures = [executor.submit(process_input_file, input_file) for input_file in input_files]
    for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
        try:
            return_code, stdout, stderr, output_path, input_id = future.result(timeout=args.timeout)
            with open(output_path, "w") as f:
                f.write(f"Return Code: {return_code}\n")
                f.write(f"Stdout: {stdout}\n")
                f.write(f"Stderr: {stderr}\n")
            with open(os.path.join(args.output, "results_summaries", f"return_{return_code}.txt"), "a") as f:
                f.write(f"{input_id}\n")
            
            err_name_pos = stderr.rfind("Error:")
            err_name = "Error"
            if err_name_pos != -1:
                for i in range(err_name_pos-1, 0, -1):
                    if not stderr[i].isalnum():
                        break
                    err_name = stderr[i] + err_name
                for i in range(err_name_pos + 5, len(stderr)):
                    if not stderr[i].isalnum():
                        break
                    err_name += stderr[i]
                err_msg = stderr[i:]
                with open(os.path.join(args.output, "results_summaries", f"errors_{err_name}.txt"), "a") as f:
                    f.write(f"{input_id}\n{err_msg}\n\n")
            else:
                if return_code != 0:
                    with open(os.path.join(args.output, "results_summaries", "errors_other.txt"), "a") as f:
                        f.write(f"{input_id}\n")
                        f.write(f"{stderr}\n\n")

        except TimeoutError as e:
            with open(output_path, "w") as f:
                f.write(f"Timeout: {args.timeout} seconds\n")
            with open(os.path.join(args.output, "results_summaries", "timeout.txt"), "a") as f:
                f.write(f"{input_id}\n")
        except Exception as e:
            with open(output_path, "w") as f:
                f.write(f"Error: {e}\n")
            with open(os.path.join(args.output, "results_summaries", "error.txt"), "a") as f:
                f.write(f"{input_id}\n")

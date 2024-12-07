import os
import subprocess
import argparse
import signal

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
input_files.sort(key=lambda x: int(x.split('.')[0])) # sort the input files by their id

# clear the ouput files
try:
    os.rmdir(os.path.join(args.output, "results"))
except FileNotFoundError: pass
try:
    os.rmdir(os.path.join(args.output, "results_summaries"))
except FileNotFoundError: pass

os.makedirs(os.path.join(args.output, "results"), exist_ok=True)
os.makedirs(os.path.join(args.output, "results_summaries"), exist_ok=True)

def run_program(executable: str, input_file: str):
    """run "{args.executable} {input_file}" and capture the return code and stdout, stderr."""    
    process = subprocess.Popen([executable, input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd())
    stdout, stderr = process.communicate()
    return_code = process.returncode

    return return_code, stdout, stderr

for input_file in input_files:
    input_id = input_file.split('.')[0]
    output_path = os.path.join(args.output, "results", "result_" + input_file)
    try:
        signal.signal(signal.SIGALRM, lambda s, f: exec("raise TimeoutError()"))
        signal.alarm(args.timeout)
        return_code, stdout, stderr = run_program(args.executable, os.path.join(args.inputs, input_file))
        signal.alarm(0)
        with open(output_path, "w") as f:
            f.write(f"Return Code: {return_code}\n")
            f.write(f"Stdout: {stdout}\n")
            f.write(f"Stderr: {stderr}\n")
        with open(os.path.join(args.output, "results_summaries", f"return_{return_code}.txt"), "a") as f:
            f.write(f"{input_id}\n")
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

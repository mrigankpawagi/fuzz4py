import os
import random
import argparse
import tqdm
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from google.api_core.exceptions import GoogleAPICallError
from dotenv import load_dotenv

load_dotenv()
api_keys = os.getenv("GENAI_API_KEYSTORE").split(",")
api_key_idx = 0
genai.configure(api_key=api_keys[api_key_idx])

# script path
script_path = os.path.dirname(os.path.realpath(__file__))


class Fuzzer:
    operators = [
        "GEN", # generate a new input
        "EQU", # generate semantically equivalent input to the last input
        "MUT", # mutate the last input
        "COM", # combine the last two inputs 
    ]

    def __init__(self, system_prompt: str, inputs_directory: str = os.path.join(script_path, "inputs"), budget: int = 10):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.model_params = {
            "model_name": "gemini-1.5-flash-8b",
            "generation_config": self.generation_config,
            "system_instruction": system_prompt,
        }
        self.model = genai.GenerativeModel(**self.model_params)
        self.inputs_directory = inputs_directory
        self.budget = budget

        self.count = 0 # number of generated inputs
        self.previous_inputs = [] # list of previous inputs as (i, input) tuples where i is the input number
        
        # check if the inputs directory exists and 
        # update the count by taking the maximum of the file names
        # and also update the last input
        if os.path.exists(self.inputs_directory):
            inputs_dir_files = os.listdir(self.inputs_directory)
            if "log.txt" in inputs_dir_files: inputs_dir_files.remove("log.txt") # remove the log file from the list
            if inputs_dir_files:
                max_file = max(map(lambda x: int(x.split(".")[0]), inputs_dir_files))
                self.count = max_file + 1

                # populate the previous inputs list
                for file in inputs_dir_files:
                    with open(os.path.join(self.inputs_directory, file)) as f:
                        self.previous_inputs.append((int(file.split(".")[0]), f.read()))

                self.previous_inputs.sort(key=lambda x: x[0])
        else:
            os.makedirs(self.inputs_directory, exist_ok=True) # create the inputs directory

    def __step(self):
        """
        Perform a single step of the fuzzer.
        """
        # if no inputs have been generated, generate a new input
        if not self.previous_inputs:
            prompt = self.__generate_new_input()
            operator = "GEN"
        else:
            # choose an operator
            while True:
                operator = random.choice(Fuzzer.operators)
                try:
                    match operator:
                        case "GEN":
                            prompt = self.__generate_new_input()
                        case "EQU":
                            prompt = self.__generate_equivalent_input()
                        case "MUT":
                            prompt = self.__mutate_input()
                        case "COM":
                            prompt = self.__combine_inputs()
                    break
                except ValueError:
                    continue
        
        prompt += "\n" + "Wrap the code in ```python and ```."

        try:
            chat_session = self.model.start_chat(history=[])
            response = chat_session.send_message(prompt)
            completion = response.text.split("```python", 1)[1].split("```")[0]

            # save the input
            input_path = os.path.join(self.inputs_directory, f"{self.count}.py")
            with open(input_path, "w") as f:
                f.write(completion)

            # log the generation of the input
            with open(os.path.join(self.inputs_directory, "log.txt"), "a") as f:
                f.write(f"{self.count}: {operator}\n")

            # update the previous inputs list
            self.previous_inputs.append((self.count, completion))

            # increment the count
            self.count += 1
        except GoogleAPICallError as e:
            # check if the error is due to ResourceExhausted or QuotaExceeded
            if "429 " in str(e):
                global api_key_idx
                print(f"API key {api_keys[api_key_idx]} has been exhausted. Switching to the next API key.")
                api_key_idx += 1
                if api_key_idx >= len(api_keys):
                    raise ValueError("All API keys have been exhausted.")
                genai.configure(api_key=api_keys[api_key_idx])
                self.model = genai.GenerativeModel(**self.model_params)

            return None

    def __generate_new_input(self):
        return "Generate a new python program."

    def __generate_equivalent_input(self):
        seed = random.choice(self.previous_inputs[-10:])[1] # choose a seed from the last 10 inputs
        return f"Generate a semantically equivalent python program to the following.\n```python\n{seed}\n```"

    def __mutate_input(self):
        seed = random.choice(self.previous_inputs[-10:])[1] # choose a seed from the last 10 inputs
        return f"Mutate the following python program.\n```python\n{seed}\n```"

    def __combine_inputs(self):
        if len(self.previous_inputs) < 2:
            raise ValueError("Not enough inputs to combine.")

        seed1, seed2 = random.choices(self.previous_inputs[-10:], k=2) # choose two seeds from the last 10 inputs
        seed1, seed2 = seed1[1], seed2[1]
        return f"Combine the following python programs.\n```python\n{seed1}\n```\n```python\n{seed2}\n```"

    def fuzz(self):
        """
        Start the fuzzer.
        """
        pbar = tqdm.tqdm(total=self.budget)
        pbar.update(self.count)
        while self.count < self.budget:
            old_count = self.count
            self.__step()
            if self.count > old_count:
                pbar.update(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, help="Path to the input prompt.", default=os.path.join(script_path, "resources", "prompt.txt"))
    parser.add_argument("--budget", type=int, help="The budget for the fuzzer.", default=100)
    args = parser.parse_args()

    # read the prompt from resources/prompt.txt
    with open(args.prompt) as f:
        distilled_prompt = f.read()

    system_prompt = "You are a fuzzer that generates Python programs that expose segmentation faults and unexpected timeouts in builtin Python functions. Keep in mind the following before fuzzing. Focus on one feature at a time and do not make obvious errors like syntax errors, undefined use of variables or use of files without first creating them.\n\n" + distilled_prompt

    fuzzer = Fuzzer(system_prompt, budget=args.budget)
    fuzzer.fuzz()

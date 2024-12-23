import os
import random
import argparse
import tqdm
import time
import json
from fuzz4py.larker import random_grammar_excerpt
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from google.api_core.exceptions import GoogleAPICallError
from dotenv import load_dotenv

load_dotenv()
api_keys = os.getenv("GENAI_API_KEYSTORE").split(",")
api_key_idx = 0
genai.configure(api_key=api_keys[api_key_idx])
MODELS = ["gemini-1.5-flash-8b", "gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp", "gemini-exp-1206"]
MODEL_INDEX = 0
RETRIES = 0
RETRY_LIMIT = 10

# script path
script_path = os.path.dirname(os.path.realpath(__file__))


class Fuzzer:
    operators = [
        "GEN", "GEN", # generate a new input (x3 probability)
        "EQU", # generate semantically equivalent input to the last input
        "MUT", # mutate the last input
        "COM", # combine the last two inputs
    ]
    LOOKBEHIND = 25 # number of previous inputs to look behind

    def __init__(self, system_prompt: str, inputs_directory: str = os.path.join(script_path, "inputs"), budget: int = 10):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type = content.Type.OBJECT,
                properties = {
                "codes": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                    type = content.Type.STRING,
                    ),
                ),
                },
            ),
            "response_mime_type": "application/json",
        }
        self.model_params = {
            "model_name": MODELS[MODEL_INDEX],
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
            inputs_dir_files = [file for file in os.listdir(self.inputs_directory) if file.endswith(".py")]
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
            signature = ""
        else:
            # choose an operator
            while True:
                operator = random.choice(Fuzzer.operators)
                signature = ""
                try:
                    match operator:
                        case "GEN":
                            prompt = self.__generate_new_input()
                        case "EQU":
                            prompt, parent = self.__generate_equivalent_input()
                            signature = str(parent)
                        case "MUT":
                            prompt, parent = self.__mutate_input()
                            signature = str(parent)
                        case "COM":
                            prompt, parent1, parent2 = self.__combine_inputs()
                            signature = f"({parent1}, {parent2})"
                    break
                except ValueError:
                    continue
        
        prompt += "\n" + "Wrap the code in ```python and ```."

        try:
            chat_session = self.model.start_chat(history=[])
            response = json.loads(chat_session.send_message(prompt).text)
            
            for completion in response["codes"][:5]: # don't use more than 5 completions 
                completion = completion.split("```python", 1)[-1].split("```")[0]

                # save the input
                input_path = os.path.join(self.inputs_directory, f"{self.count}.py")
                with open(input_path, "w") as f:
                    f.write(completion)

                # log the generation of the input
                with open(os.path.join(self.inputs_directory, "log.txt"), "a") as f:
                    f.write(f"{self.count}: {operator} {signature}\n")

                # update the previous inputs list
                self.previous_inputs.append((self.count, completion))

                # increment the count
                self.count += 1
        except GoogleAPICallError as e:
            print(e)
            # check if the error is due to ResourceExhausted or QuotaExceeded
            if "429" in str(e) and "Resource" in str(e):
                global api_key_idx, MODEL_INDEX, RETRIES

                if RETRIES < RETRY_LIMIT:
                    # do nothing and try again (this may be due to rate limiting)
                    RETRIES += 1
                    time.sleep(2) # wait for 2 seconds and try again
                else:
                    RETRIES = 0
                    
                    print(f"API key {api_keys[api_key_idx]} has exhausted {MODELS[MODEL_INDEX]}.")
                    
                    # try changing the model
                    if MODEL_INDEX < len(MODELS) - 1:
                        MODEL_INDEX += 1
                        print("Changing model to", MODELS[MODEL_INDEX])
                        self.model_params["model_name"] = MODELS[MODEL_INDEX]
                    
                    # now try changing the API key
                    else:
                        if api_key_idx >= len(api_keys) - 1:
                            raise ValueError("All API keys have been exhausted.")
                        api_key_idx += 1
                        print("Changing API key to", api_keys[api_key_idx])
                        
                        genai.configure(api_key=api_keys[api_key_idx])
                        MODEL_INDEX = 0
                    
                    self.model = genai.GenerativeModel(**self.model_params)
            if "429" in str(e) and "QuotaExceeded" in str(e):
                if RETRIES < RETRY_LIMIT:
                    # do nothing and try again (this may be due to rate limiting)
                    RETRIES += 1
                    time.sleep(2) # wait for 2 seconds and try again
                else:
                    RETRIES = 0

            return None
        except Exception as e:
            print(e)
            return None

    def __generate_new_input(self):
        grammar_excerpt = random_grammar_excerpt(5)
        return "Generate a new python program. You can use the following excerpt from the python grammar.\n\n" + grammar_excerpt

    def __generate_equivalent_input(self):
        n = len(self.previous_inputs)
        seed_index = random.choice(range(max(0, n - Fuzzer.LOOKBEHIND), n))
        seed = self.previous_inputs[seed_index][1]

        return f"Generate another python program that is semantically similar to the following.\n```python\n{seed}\n```", seed_index

    def __mutate_input(self):
        n = len(self.previous_inputs)
        seed_index = random.choice(range(max(0, n - Fuzzer.LOOKBEHIND), n))
        seed = self.previous_inputs[seed_index][1]

        return f"Mutate the following python program.\n```python\n{seed}\n```", seed_index

    def __combine_inputs(self):
        if len(self.previous_inputs) < 2:
            raise ValueError("Not enough inputs to combine.")

        
        n = len(self.previous_inputs)
        seed1_index = random.choice(range(max(0, n - Fuzzer.LOOKBEHIND), n))
        seed2_index = random.choice(tuple(set(range(max(0, n - Fuzzer.LOOKBEHIND), n)).difference({seed1_index}))) # choose without replacement
        seed1, seed2 = self.previous_inputs[seed1_index][1], self.previous_inputs[seed2_index][1]

        return f"Combine the following python programs.\n```python\n{seed1}\n```\n```python\n{seed2}\n```", seed1_index, seed2_index

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
                pbar.update(self.count - old_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, help="Path to the input prompt or the prompt itself.", default=os.path.join(script_path, "resources", "prompt.txt"))
    parser.add_argument("--inputs-directory", type=str, help="Path to the directory to store the generated inputs.", default=os.path.join(script_path, "inputs"))
    parser.add_argument("--budget", type=int, help="The budget for the fuzzer.", default=10)
    args = parser.parse_args()

    # read the prompt from args.prompt if it is a valid path
    if not os.path.exists(args.prompt):
        distilled_prompt = args.prompt
    else:
        with open(args.prompt) as f:
            distilled_prompt = f.read()

    system_prompt = "\n\n".join(["You are a fuzzer used to find bugs in python parsers. Please generate python programs which use language features in a complex way. These programs will not be executed and so focus on structures rather than actually working code. Do NOT run ast or exec on your own. You should use unnatural constructs, complicated type annotations, weird characters, badly formatted comments, etc. Prefer very short programs and generate as many as you can."] + ([distilled_prompt] if distilled_prompt else []))

    fuzzer = Fuzzer(system_prompt, inputs_directory=args.inputs_directory, budget=args.budget)
    fuzzer.fuzz()

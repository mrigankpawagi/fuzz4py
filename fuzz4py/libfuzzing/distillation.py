import os
import json
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

RETRY_BUDGET = 5

# script path
script_path = os.path.dirname(os.path.realpath(__file__))

# Create the model
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        enum=[],
        required=["apis"],
        properties={
            "apis": content.Schema(
                type=content.Type.ARRAY,
                items=content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["description", "signature", "name"],
                    properties={
                        "description": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "signature": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "name": content.Schema(
                            type=content.Type.STRING,
                        ),
                    },
                ),
            ),
        },
    ),
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are an expert python programmer. Look at the following excerpt from the official Python documentation and for each function (API), provide a very brief description, a signature (with argument types), and the fully qualified name.",
)

chat_session = model.start_chat(history=[])

# create prompt from documentation
# read documentation/index.txt for the list of files to be used in a logical order
with open(os.path.join(script_path, "documentation", "index.txt")) as f:
    doc_files = f.read().splitlines()

docs = dict()
for doc_file in doc_files:
    with open(os.path.join(script_path, "documentation", doc_file)) as f:
        docs[doc_file] = f.read()

# send the prompts to the model and save the responses
for doc in tqdm(docs):
    result_file_name = doc.split(".")[0] + ".json"
    result_file_path = os.path.join(script_path, "documentation", "distilled", result_file_name)
    os.makedirs(os.path.dirname(result_file_path), exist_ok=True)
 
    if os.path.exists(result_file_path): continue # skip if already exists

    for _ in range(RETRY_BUDGET):
        try:
            response = chat_session.send_message(docs[doc]).text
            json_obj = json.loads(response)
            with open(result_file_path, "w") as f:
                f.write(json.dumps(json_obj, indent=4))
            break
        except Exception as e: tqdm.write(f"Error: {e}. Retrying...")
    else: tqdm.write(f"Could not distill {doc}. Skipping...")

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# script path
script_path = os.path.dirname(os.path.realpath(__file__))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are an expert python programmer with extensive experience in writing documentation. Please summarize provided documentation to highlight important technical points concisely.",
)

chat_session = model.start_chat(history=[])

# create prompt from documentation
# read documentation/index.txt for the list of files to be used in a logical order
with open(os.path.join(script_path, "documentation", "index.txt")) as f:
  doc_files = f.read().splitlines()

docs = []
for doc_file in doc_files:
  with open(os.path.join(script_path, "documentation", doc_file)) as f:
    docs.append(f.read())

prompt = "\n\n".join(docs)
response = chat_session.send_message(prompt).text

# save the distilled prompt
prompt_path = os.path.join(script_path, "resources", "prompt.txt")
os.makedirs(os.path.dirname(prompt_path), exist_ok=True)
with open(prompt_path, "w") as f:
    f.write(response)

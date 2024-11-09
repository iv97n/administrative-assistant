from groq import Groq
import base64
import html
import json
import os
from dotenv import load_dotenv

load_dotenv()


groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def parse_document(doc):
    # Decode the base64 content
    binary_content = base64.b64decode(doc["content"]["$binary"]["base64"])
    # Convert to a string (assuming UTF-8 encoding) and return it
    text_content = binary_content.decode("utf-8")
    text_content = html.unescape(text_content)
    
    return text_content

file_paths = ['data/acreditacio_idiomes.json', 'data/nota_mitjana.json', 'data/devolucio_preus_publics.json']

# Load the context from the files
context = ""
for file_path in file_paths:
    with open(file_path, "r") as file:
        doc = json.load(file)
        text_content = parse_document(doc)
        context += text_content + "\n"

def groq_prompt(prompt):
    convo = [
        {'role': 'system', 'content': ''+ context},  # Context provided here
        {'role': 'user', 'content': prompt}
    ]
    chat_response = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_response.choices[0].message

    return response.content

prompt = input('USER: ')
response = groq_prompt(prompt)
print(response)
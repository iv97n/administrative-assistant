import requests
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer


load_dotenv()

class SalamandraClient(object):

    def __init__(self, model_name="BSC-LT/salamandra-7b-instruct-aina-hack"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.HF_TOKEN = os.getenv("HF_TOKEN")
        self.BASE_URL = os.getenv("BASE_URL")
        

        self.headers = {
            "Accept" : "application/json",
            "Authorization": f"Bearer {self.HF_TOKEN}",
            "Content-Type": "application/json"
        }

    def query_model(self, text):
        system_prompt = "you are a helpful assistant"
        message = [ { "role": "system", "content": system_prompt} ]
        message += [ { "role": "user", "content": text } ]
        prompt = self.tokenizer.apply_chat_template(
            message,
            tokenize=False,
            add_generation_prompt=True,
        )

        payload = {
        "inputs": prompt,
        "parameters": {}
        }
        api_url = self.BASE_URL + "/generate"
        response = requests.post(api_url, headers=self.headers, json=payload)
        return response.json()


    def summarize_text(self, text):
        text = f"""
        Cohesiona el següent document.

        Document:
        {text}
        """
        return self.query_model(text)

"""

file_path = './src/summarizer/data/output_acreditacio-de-coneixements-d-idiomes.data'


with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


client = SalamandraClient()

print(client.summarize_text(file_content))
"""
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

    def query_model(self, text, context=None):

        if isinstance(text, list):
        # Concatenate the "role" and "content" fields into a single prompt string
            text = "\n".join([f"{entry['role']}: {entry['content']}" for entry in text])


        # System prompt for model setup
        system_prompt = "You are a helpful assistant."
        message = [{"role": "system", "content": system_prompt}]

        # If context is provided, add it as part of the system message for model context
        if context:
            context_message = f"Context: {context}"
            message.append({"role": "system", "content": context_message})

        # Add the main user query as usual
        message.append({"role": "user", "content": text})

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
    

    def givePrediction(self, instruction, context=None):
       
        if isinstance(instruction, list):
        # Concatenate the "role" and "content" fields into a single prompt string
            instruction = "\n".join([f"{entry['role']}: {entry['content']}" for entry in context])

        # System prompt for model setup
        system_prompt = "You are a helpful assistant."
        message = [{"role": "system", "content": system_prompt}]

        # If context is provided, add it as part of the system message for model context
        if context:
            context_message = f"Context: {context}"
            message.append({"role": "system", "content": context_message})

        # Add the main user query as usual
        message.append({"role": "user", "content": instruction})

        prompt = self.tokenizer.apply_chat_template(
            message,
            tokenize=False,
            add_generation_prompt=True,
        )
        # Prepare payload for the API request
        payload = {
            "inputs": prompt,
            "parameters": {}
        }   

        # Make the API request
        api_url = self.BASE_URL + "/generate"
        response = requests.post(api_url, headers=self.headers, json=payload)

        # Check for successful response and extract answer
        if response.status_code == 200:
            response_json = response.json()
            generated_text = response_json["generated_text"]
            answer = generated_text.split("Context")[0].strip()
            return answer
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    

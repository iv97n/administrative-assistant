from groq import Groq

class GroqClient(object):
    def __init__(self, api_key):
        self.groq_client = Groq(api_key=api_key)

    def generate_response(self, prompt, context):

        language_instruction = "Contesta sempre en català."

        # Prepare the conversation with the provided context and the user prompt
        convo = [
            {'role': 'system', 'content': context},  # Pass the context directly
            {'role': 'system', 'content': language_instruction},  # Language instruction
            {'role': 'user', 'content': prompt}
        ]
        
        # Make the request to the Groq API with the context and prompt
        chat_response = self.groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
        
        # Extract and return the response from the Groq API
        response = chat_response.choices[0].message
        return response.content